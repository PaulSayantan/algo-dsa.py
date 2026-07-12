"""Extract runnable test cases from a solution.py ``__main__`` block.

The workspace convention (verified across all 884 files) is::

    if __name__ == "__main__":
        sol = Solution()                       # setup
        print(sol.search([1, 2, 3], 2))        # a case  # expected: 1
        na = NumArray([1, 2])                  # more setup (interleaved)
        print(na.sumRange(0, 1))               # another case  # expected: 3

Each ``print(<call>)`` becomes a :class:`~dsa.model.Case`. Non-print statements
before it accumulate into that case's ``setup`` list, so replaying setup then
evaluating the call reproduces the exact observed state — this handles the
three signature families (``class Solution`` methods, free functions, and
stateful design classes) uniformly.

The expected value lives in a trailing comment. ``ast`` discards comments, so we
recover them with ``tokenize`` keyed by line, and (crucially) we attach a
comment to a statement by the statement's ``end_lineno`` — 101 files have
multi-line ``print(...)`` calls where ``lineno != end_lineno``.
"""

from __future__ import annotations

import ast
import io
import re
import tokenize
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union

from ..model import Case
from .literals import try_parse_literal

# Matches "# expected: X", "# Expected: X", "# Expected output: X", and qualified
# forms like "# expected (any order): X" (case-insensitive). The parenthetical
# qualifier is captured separately so callers can loosen comparison (e.g. order-
# insensitive) for that case.
# The trailing ``\s*`` before the parenthetical was folded *into* the optional
# group so only one ``\s*`` sits adjacent to the required ``:``. The previous form
# had two ambiguous whitespace runs (``\s*(?:\(...\))?\s*``) around the colon, which
# let the engine backtrack quadratically (O(n^2)) on a ``# expected`` comment with a
# long whitespace run and no colon — freezing the CLI. Callers additionally
# short-circuit via a cheap ``":" in`` check (see :func:`_collect_expected_comments`).
_EXPECTED_RE = re.compile(
    r"#\s*expected(?:\s+output)?\s*(?:\(([^)]*)\)\s*)?:\s*(.*)$",
    re.IGNORECASE,
)

# Internal sentinel prefixing a payload whose comment said "(any order)".
_UNORDERED_PREFIX = "\x00unordered\x00"


class MainBlockNotFound(Exception):
    """Raised when a solution.py has no ``if __name__ == "__main__"`` block."""


def _collect_expected_comments(source: str) -> Dict[int, str]:
    """Map line number -> expected-payload text for every expected-comment.

    Only lines whose comment matches the ``expected:`` marker are included (the
    payload after the marker; may be empty prose like "# e.g. ..." which the
    marker regex won't match — those are simply absent, and the corresponding
    print becomes non-deterministic).
    """
    payloads: Dict[int, str] = {}
    try:
        tokens = tokenize.generate_tokens(io.StringIO(source).readline)
        for tok in tokens:
            if tok.type == tokenize.COMMENT:
                # An expected-marker always contains a colon; skipping colon-free
                # comments avoids running the regex on the exact input that could
                # trigger catastrophic backtracking (see _EXPECTED_RE).
                if ":" not in tok.string:
                    continue
                m = _EXPECTED_RE.search(tok.string)
                if m:
                    qualifier = (m.group(1) or "").strip()
                    payload = m.group(2).strip()
                    # Encode an "any order" qualifier as a prefix marker consumed
                    # by the case builder; keeps the return type a simple str map.
                    if qualifier and ("order" in qualifier.lower() or "any" in qualifier.lower()):
                        payload = _UNORDERED_PREFIX + payload
                    payloads[tok.start[0]] = payload
    except tokenize.TokenError:
        pass
    return payloads


def _comment_lines(source: str) -> set:
    """Line numbers that carry *any* comment (expected or not)."""
    lines: set = set()
    try:
        for tok in tokenize.generate_tokens(io.StringIO(source).readline):
            if tok.type == tokenize.COMMENT:
                lines.add(tok.start[0])
    except tokenize.TokenError:
        pass
    return lines


def _detect_block_convention(prints: List[ast.stmt], comments: Dict[int, str]) -> str:
    """Return 'inline', 'above', or 'below' — where block comments sit vs a print.

    Determined from the first print that has an adjacent expected-comment, so a
    file that writes ``# Expected: X`` *above* each print (convex-hull style) is
    not confused with one that writes it *below* (transpose style).
    """
    for stmt in prints:
        end = stmt.end_lineno or stmt.lineno
        start = stmt.lineno
        if end in comments:
            return "inline"
        if (start - 1) in comments:
            return "above"
        if (end + 1) in comments:
            return "below"
    return "inline"


def _find_main_body(tree: ast.Module) -> Optional[List[ast.stmt]]:
    """Return the statement list inside ``if __name__ == "__main__":``."""
    for node in tree.body:
        if not isinstance(node, ast.If):
            continue
        test = node.test
        if isinstance(test, ast.Compare) and len(test.comparators) == 1:
            left, right = test.left, test.comparators[0]
            names = {_dunder_name(left), _dunder_name(right)}
            if "__name__" in names and "__main__" in names:
                return node.body
    return None


def _dunder_name(node: ast.expr) -> Optional[str]:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None


def _print_arg(stmt: ast.stmt) -> Optional[ast.expr]:
    """If ``stmt`` is ``print(<expr>)`` at statement level, return ``<expr>``.

    Unwraps ``print(repr(x))`` to ``x``: those files write the expected literal
    as the *value* (``'l'``) which ``repr`` renders with quotes when printed, so
    comparing against the underlying value is correct.
    """
    if not isinstance(stmt, ast.Expr):
        return None
    call = stmt.value
    if (
        isinstance(call, ast.Call)
        and isinstance(call.func, ast.Name)
        and call.func.id == "print"
        and len(call.args) == 1
        and not call.keywords
    ):
        arg = call.args[0]
        if (
            isinstance(arg, ast.Call)
            and isinstance(arg.func, ast.Name)
            and arg.func.id == "repr"
            and len(arg.args) == 1
        ):
            return arg.args[0]
        return arg
    return None


def _expected_for(
    stmt: ast.stmt,
    comments: Dict[int, str],
    convention: str,
    all_comment_lines: set,
) -> Tuple[bool, Optional[str]]:
    """Find the expected-comment payload attached to a print statement.

    Inline always wins (``print(...)  # expected: 4``). Otherwise use the file's
    detected block convention — ``above`` (comment precedes the print) or
    ``below`` (comment follows it) — so multi-example blocks don't shift by one.

    Crucially, if the print carries its *own* inline comment that is NOT an
    ``expected:`` marker (e.g. ``# 2`` or ``# some note``), the print is treated
    as having no expected value — we do NOT borrow a neighbor's expected, which
    would misalign every subsequent case. Returns ``(has_comment, payload)``.
    """
    end = stmt.end_lineno or stmt.lineno
    start = stmt.lineno
    # 1. Inline on the print's final line always wins.
    if end in comments:
        return True, comments[end]
    # 2. Inline comment present but not an `expected:` marker -> non-deterministic
    #    (do NOT borrow a neighbor's expected; that would misalign later cases).
    if end in all_comment_lines:
        return False, None
    # 3. No inline comment: consult the block neighbor. Prefer the file's detected
    #    convention, but a print's own immediately-below expected comment is
    #    unambiguously its own even in a file whose other cases are inline.
    if convention == "above" and (start - 1) in comments:
        return True, comments[start - 1]
    if (end + 1) in comments:
        return True, comments[end + 1]
    if (start - 1) in comments:
        return True, comments[start - 1]
    return False, None


def extract_cases(source: str) -> List[Case]:
    """Parse ``source`` and return the ordered list of cases from ``__main__``."""
    tree = ast.parse(source)
    body = _find_main_body(tree)
    if body is None:
        raise MainBlockNotFound("no `if __name__ == \"__main__\"` block")

    comments = _collect_expected_comments(source)
    all_comment_lines = _comment_lines(source)
    print_stmts = [s for s in body if _print_arg(s) is not None]
    convention = _detect_block_convention(print_stmts, comments)

    cases: List[Case] = []
    setup: List[str] = []
    idx = 0
    for stmt in body:
        arg = _print_arg(stmt)
        if arg is None:
            # Setup statement (assignment, mutation, bare call, etc.).
            setup.append(ast.unparse(stmt))
            continue

        call_src = ast.unparse(arg)
        has_comment, payload = _expected_for(stmt, comments, convention, all_comment_lines)
        unordered = False
        if payload and payload.startswith(_UNORDERED_PREFIX):
            unordered = True
            payload = payload[len(_UNORDERED_PREFIX) :]
        case = Case(
            index=idx,
            call_src=call_src,
            setup=list(setup),
            lineno=stmt.lineno,
            raw_expected=payload,
            unordered=unordered,
        )
        # A prior print's call may mutate shared object state that this case
        # depends on (design-class op-sequences like KthLargest.add). Since we
        # rebuild state per case in a fresh namespace, replay earlier calls as
        # side-effecting setup for the *next* case.
        setup.append(call_src)
        if payload:
            ok, value = try_parse_literal(payload)
            if ok:
                case.expected = value
                case.kind = "value"
            else:
                case.kind = "nondeterministic"
        else:
            # No expected: marker (prose "# e.g." / "# some permutation" / none).
            case.kind = "nondeterministic"
        cases.append(case)
        idx += 1

    return cases


def extract_cases_from_file(path: Union[str, Path]) -> List[Case]:
    return extract_cases(Path(path).read_text(encoding="utf-8"))


def _body_is_empty(fn: ast.AST) -> bool:
    """A function body counts as "empty" (unimplemented) if, after dropping the
    docstring, it is only ``pass``, ``...``, or ``raise NotImplementedError``."""
    stmts = list(fn.body)  # type: ignore[attr-defined]
    if (
        stmts
        and isinstance(stmts[0], ast.Expr)
        and isinstance(getattr(stmts[0], "value", None), ast.Constant)
        and isinstance(stmts[0].value.value, str)
    ):
        stmts = stmts[1:]
    if not stmts:
        return True
    for s in stmts:
        if isinstance(s, ast.Pass):
            continue
        if isinstance(s, ast.Expr) and isinstance(s.value, ast.Constant) and s.value.value is ...:
            continue
        # Only ``raise NotImplementedError`` counts as "unimplemented" (per the
        # docstring). A body whose sole statement is any *other* raise (e.g.
        # ``raise ValueError(...)``) is a real implementation — treating it as a stub
        # would silently skip its cases instead of grading them.
        if isinstance(s, ast.Raise) and _raises_not_implemented(s):
            continue
        return False
    return True


def _raises_not_implemented(node: ast.Raise) -> bool:
    """True if ``node`` raises ``NotImplementedError`` (bare name or call)."""
    exc = node.exc
    if isinstance(exc, ast.Name):
        return exc.id == "NotImplementedError"
    if isinstance(exc, ast.Call) and isinstance(exc.func, ast.Name):
        return exc.func.id == "NotImplementedError"
    return False


def is_stub(source: str) -> bool:
    """Is this solution an unimplemented learner template?

    The corpus's templates commonly ship a filled-in ``ListNode``/``TreeNode``
    data class and ``build``/``to_list`` harness helpers alongside an *empty*
    entrypoint. So we look specifically at the methods/functions the ``__main__``
    cases actually invoke: if any invoked entrypoint has an empty body, the
    solution is still a stub (skip its cases rather than fail them).
    """
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return False

    # Names the cases call (both attribute methods like ``.add`` and bare funcs).
    try:
        cases = extract_cases(source)
    except Exception:  # noqa: BLE001
        cases = []
    called: set = set()
    for c in cases:
        for src in [*c.setup, c.call_src]:
            try:
                node = ast.parse(src, mode="eval") if src == c.call_src else ast.parse(src)
            except SyntaxError:
                continue
            for sub in ast.walk(node):
                if isinstance(sub, ast.Call):
                    f = sub.func
                    if isinstance(f, ast.Attribute):
                        called.add(f.attr)
                    elif isinstance(f, ast.Name):
                        called.add(f.id)

    # Only consider top-level functions and class methods as candidate
    # entrypoints — never helpers defined *inside* the ``__main__`` block.
    top_funcs = _top_level_functions(tree)

    entry_funcs = [fn for fn in top_funcs if fn.name in called]
    if entry_funcs:
        # Stub if ANY invoked entrypoint is unimplemented.
        return any(_body_is_empty(fn) for fn in entry_funcs)

    # No identifiable entrypoint among top-level defs: fall back to "every
    # top-level function/method is empty" (ignores __main__ test helpers).
    return bool(top_funcs) and all(_body_is_empty(fn) for fn in top_funcs)


def _top_level_functions(tree: ast.Module) -> List[ast.AST]:
    """Module-level functions and methods of module-level classes (not nested)."""
    out: List[ast.AST] = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            out.append(node)
        elif isinstance(node, ast.ClassDef):
            for m in node.body:
                if isinstance(m, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    out.append(m)
    return out
