"""Parse PROBLEM.md: metadata, and the ``## Examples`` section into cases.

Examples come in two families:

* function-style::

      Input:  nums = [-1, 0, 3, 5, 9, 12], target = 9
      Output: 4

* class-op-style (design problems)::

      Input:
        ["KthLargest", "add", "add"]
        [[3, [4, 5, 8, 2]], [3], [5]]
      Output:
        [null, 4, 5]

The function-style ``Input:`` line is a comma-separated list of ``name = value``
assignments; we keep the parsed values as an ordered dict so a caller can bind
them to a function signature. The class-op-style is returned as an op-sequence.
JSON-ish ``null``/``true``/``false`` tokens are normalized before literal-eval.
"""

from __future__ import annotations

import ast
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

_DIFFICULTY_RE = re.compile(r"^\*\*Difficulty:\*\*\s*(.+?)\s*$", re.MULTILINE)
_SOURCE_RE = re.compile(r"^\*\*Source:\*\*\s*(.+?)\s*$", re.MULTILINE)
_TITLE_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)


@dataclass
class FunctionExample:
    inputs: Dict[str, Any]  # ordered name -> value
    output: Any
    output_parsed: bool
    raw_input: str = ""
    raw_output: str = ""


@dataclass
class OpSequenceExample:
    ops: List[str]
    args: List[list]
    outputs: List[Any]
    outputs_parsed: bool = True


@dataclass
class ProblemDoc:
    title: str = ""
    difficulty_raw: str = ""
    source_raw: Optional[str] = None
    function_examples: List[FunctionExample] = field(default_factory=list)
    opseq_examples: List[OpSequenceExample] = field(default_factory=list)
    has_examples_section: bool = False


def _normalize_jsonish(text: str) -> str:
    """Turn JSON tokens into Python literals for ``ast.literal_eval``."""
    # Whole-word replacements only.
    text = re.sub(r"\bnull\b", "None", text)
    text = re.sub(r"\btrue\b", "True", text)
    text = re.sub(r"\bfalse\b", "False", text)
    return text


def _literal(text: str) -> Tuple[bool, Any]:
    try:
        return True, ast.literal_eval(_normalize_jsonish(text.strip()))
    except (ValueError, SyntaxError):
        return False, None


def _split_top_level_commas(text: str) -> List[str]:
    """Split on commas that are not nested inside (), [], {} or quotes."""
    parts: List[str] = []
    depth = 0
    quote: Optional[str] = None
    buf: List[str] = []
    for ch in text:
        if quote:
            buf.append(ch)
            if ch == quote:
                quote = None
            continue
        if ch in "\"'":
            quote = ch
            buf.append(ch)
            continue
        if ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1
        if ch == "," and depth == 0:
            parts.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    if buf:
        parts.append("".join(buf))
    return parts


def _parse_assignments(text: str) -> Dict[str, Any]:
    """Parse ``name = value, name2 = value2`` into an ordered dict of values."""
    result: Dict[str, Any] = {}
    for part in _split_top_level_commas(text):
        if "=" not in part:
            continue
        name, _, value = part.partition("=")
        name = name.strip()
        if not re.match(r"^[A-Za-z_]\w*$", name):
            continue
        ok, val = _literal(value)
        result[name] = val if ok else value.strip()
    return result


def _extract_examples_block(md: str) -> Optional[str]:
    """Return the text of the ``## Examples`` section (up to the next ``## ``)."""
    m = re.search(r"^##\s+Examples\s*$", md, re.MULTILINE)
    if not m:
        return None
    start = m.end()
    nxt = re.search(r"^##\s+", md[start:], re.MULTILINE)
    return md[start : start + nxt.start()] if nxt else md[start:]


def _fenced_blocks(text: str) -> List[str]:
    """Return the contents of ``` fenced code blocks within ``text``."""
    return re.findall(r"```[^\n]*\n(.*?)```", text, re.DOTALL)


def parse(md: str) -> ProblemDoc:
    doc = ProblemDoc()
    tm = _TITLE_RE.search(md)
    if tm:
        doc.title = tm.group(1).strip()
    dm = _DIFFICULTY_RE.search(md)
    if dm:
        doc.difficulty_raw = dm.group(1).strip()
    sm = _SOURCE_RE.search(md)
    if sm:
        doc.source_raw = sm.group(1).strip()

    block = _extract_examples_block(md)
    if block is None:
        return doc
    doc.has_examples_section = True

    for fenced in _fenced_blocks(block):
        _parse_example_fence(fenced, doc)
    return doc


def _parse_example_fence(fenced: str, doc: ProblemDoc) -> None:
    lines = fenced.strip("\n").splitlines()
    joined = "\n".join(lines)

    # Class-op-style: an Input: whose following non-empty lines start with '[' and
    # contain a list of operation-name strings.
    input_idx = _find_label(lines, "Input")
    output_idx = _find_label(lines, "Output")
    if input_idx is None or output_idx is None:
        return

    input_body = _label_body(lines, input_idx, output_idx)
    output_body = _label_body(lines, output_idx, _find_label(lines, "Explanation"))

    if _looks_like_opseq(input_body):
        ex = _parse_opseq(input_body, output_body)
        if ex is not None:
            doc.opseq_examples.append(ex)
        return

    # Function-style.
    inputs = _parse_assignments(" ".join(input_body).strip())
    ok, out = _literal(" ".join(output_body).strip())
    doc.function_examples.append(
        FunctionExample(
            inputs=inputs,
            output=out if ok else None,
            output_parsed=ok,
            raw_input=" ".join(input_body).strip(),
            raw_output=" ".join(output_body).strip(),
        )
    )


def _find_label(lines: List[str], label: str) -> Optional[int]:
    for i, ln in enumerate(lines):
        if re.match(rf"^\s*{label}\s*:", ln):
            return i
    return None


def _label_body(lines: List[str], idx: Optional[int], end: Optional[int]) -> List[str]:
    """Text belonging to a ``Label:`` — the inline remainder plus following lines."""
    if idx is None:
        return []
    stop = end if end is not None else len(lines)
    first = re.sub(r"^\s*\w+\s*:", "", lines[idx]).strip()
    body = [first] if first else []
    for ln in lines[idx + 1 : stop]:
        if ln.strip():
            body.append(ln.strip())
    return body


def _looks_like_opseq(body: List[str]) -> bool:
    if not body:
        return False
    joined = " ".join(body)
    ok, val = _literal(joined.split("]")[0] + "]") if "]" in joined else (False, None)
    # Heuristic: first parsed list is a list of strings (operation names).
    return bool(ok and isinstance(val, list) and val and all(isinstance(x, str) for x in val))


def _parse_opseq(input_body: List[str], output_body: List[str]) -> Optional[OpSequenceExample]:
    joined_in = " ".join(input_body)
    # Split into the two top-level lists: ops array and args array.
    lists = _extract_bracket_lists(joined_in)
    if len(lists) < 2:
        return None
    ok_ops, ops = _literal(lists[0])
    ok_args, args = _literal(lists[1])
    ok_out, outputs = _literal(" ".join(output_body))
    if not (ok_ops and ok_args):
        return None
    return OpSequenceExample(
        ops=ops,
        args=args,
        outputs=outputs if ok_out else [],
        outputs_parsed=ok_out,
    )


def _extract_bracket_lists(text: str) -> List[str]:
    """Return top-level ``[...]`` substrings in order."""
    out: List[str] = []
    depth = 0
    start = -1
    for i, ch in enumerate(text):
        if ch == "[":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "]":
            depth -= 1
            if depth == 0 and start >= 0:
                out.append(text[start : i + 1])
                start = -1
    return out


def parse_file(path: Union[str, Path]) -> ProblemDoc:
    return parse(Path(path).read_text(encoding="utf-8"))
