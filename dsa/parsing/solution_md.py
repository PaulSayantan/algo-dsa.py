"""Extract the reference implementation from SOLUTION.md.

SOLUTION.md holds correct code in ```python fences. Files often contain two
fences (a brute-force snippet and the optimal one); we select the fence under a
heading that starts with "Optimal", falling back to the last python fence. Some
fences drop type hints and re-import their own dependencies, so callers prepend
a permissive preamble before executing.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Union


@dataclass
class ReferenceCode:
    code: Optional[str]  # selected reference block, or None if no python fence
    heading: str = ""  # heading the block was found under
    num_blocks: int = 0


# Matches a heading line and captures its text; and python fences with position.
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$", re.MULTILINE)
_PY_FENCE_RE = re.compile(r"```(?:python|py)\s*\n(.*?)```", re.DOTALL | re.IGNORECASE)


def _heading_at(md: str, pos: int) -> str:
    """The nearest heading text at or before ``pos``."""
    best = ""
    for m in _HEADING_RE.finditer(md):
        if m.start() <= pos:
            best = m.group(2)
        else:
            break
    return best


def extract_reference(md: str) -> ReferenceCode:
    blocks: List[tuple] = []  # (heading, code)
    for m in _PY_FENCE_RE.finditer(md):
        heading = _heading_at(md, m.start())
        blocks.append((heading, m.group(1)))

    if not blocks:
        return ReferenceCode(code=None, num_blocks=0)

    # Prefer a block under an "Optimal..." heading (last such if several).
    optimal = [b for b in blocks if b[0].lower().lstrip("# ").startswith("optimal")]
    chosen = optimal[-1] if optimal else blocks[-1]
    return ReferenceCode(code=chosen[1], heading=chosen[0], num_blocks=len(blocks))


def extract_reference_file(path: Union[str, Path]) -> ReferenceCode:
    return extract_reference(Path(path).read_text(encoding="utf-8"))


PREAMBLE = (
    "from typing import *\n"
    "import heapq, math, bisect, collections, itertools, functools, re, random, sys\n"
    "from collections import defaultdict, Counter, deque, OrderedDict\n"
    "from functools import lru_cache, reduce\n"
    "from itertools import accumulate\n"
)
