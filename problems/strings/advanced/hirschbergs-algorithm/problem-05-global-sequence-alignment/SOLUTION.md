# Solution — Global Sequence Alignment in Linear Space

## Brute Force

Enumerate every way to interleave gaps into `a` and `b` and score each. The number of
alignments grows exponentially (`~ C(n+m, n)`), so this is only usable for toy inputs.

The standard polynomial method is the Needleman–Wunsch DP: fill an `(n+1) × (m+1)` score
table, then **backtrack** from `dp[n][m]` to read the alignment.

```
dp[i][j] = max( dp[i-1][j-1] + s(a[i-1], b[j-1]),   # align the two characters
                dp[i-1][j]   + gap,                  # a[i-1] aligned to a gap
                dp[i][j-1]   + gap )                 # b[j-1] aligned to a gap
```
with borders `dp[i][0] = i·gap`, `dp[0][j] = j·gap`, and `s(x, y) = match if x == y else
mismatch`.

- **Time:** `O(n·m)`
- **Space:** `O(n·m)` — the table is needed for the backtrack. This is exactly the memory
  wall Hirschberg removes.

## Optimal Approach — Hirschberg's Algorithm

The optimal alignment path through the grid is monotone, so it crosses the middle row
`mid = n // 2` at exactly one column `k`, splitting the problem into aligning
`(a[:mid], b[:k])` and `(a[mid:], b[k:])`. To find `k` in linear space, take a forward
score sweep of the top half and a backward score sweep of the bottom half; the column
maximising their sum is an optimal crossing point.

```python
from typing import List, Tuple


def nw_score_row(a: str, b: str, match: int, mismatch: int, gap: int) -> List[int]:
    prev = [gap * j for j in range(len(b) + 1)]         # aligning "" to b[:j]
    for i in range(1, len(a) + 1):
        curr = [gap * i] + [0] * len(b)                 # aligning a[:i] to ""
        ai = a[i - 1]
        for j in range(1, len(b) + 1):
            diag = prev[j - 1] + (match if ai == b[j - 1] else mismatch)
            up = prev[j] + gap
            left = curr[j - 1] + gap
            curr[j] = max(diag, up, left)
        prev = curr
    return prev


def _base_align(a, b, match, mismatch, gap):
    """Full NW with traceback; called only on a 1-row (or empty) base case."""
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = gap * i
    for j in range(m + 1):
        dp[0][j] = gap * j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            diag = dp[i - 1][j - 1] + (match if a[i - 1] == b[j - 1] else mismatch)
            dp[i][j] = max(diag, dp[i - 1][j] + gap, dp[i][j - 1] + gap)
    ra, rb = [], []
    i, j = n, m
    while i > 0 and j > 0:
        cur = dp[i][j]
        if cur == dp[i - 1][j - 1] + (match if a[i - 1] == b[j - 1] else mismatch):
            ra.append(a[i - 1]); rb.append(b[j - 1]); i -= 1; j -= 1
        elif cur == dp[i - 1][j] + gap:
            ra.append(a[i - 1]); rb.append('-'); i -= 1
        else:
            ra.append('-'); rb.append(b[j - 1]); j -= 1
    while i > 0:
        ra.append(a[i - 1]); rb.append('-'); i -= 1
    while j > 0:
        ra.append('-'); rb.append(b[j - 1]); j -= 1
    return "".join(reversed(ra)), "".join(reversed(rb))


def align(a: str, b: str, match: int = 1, mismatch: int = -1,
          gap: int = -2) -> Tuple[str, str]:
    n, m = len(a), len(b)
    if n == 0:
        return "-" * m, b
    if m == 0:
        return a, "-" * n
    if n == 1:
        return _base_align(a, b, match, mismatch, gap)

    mid = n // 2
    L = nw_score_row(a[:mid], b, match, mismatch, gap)              # forward
    R = nw_score_row(a[mid:][::-1], b[::-1], match, mismatch, gap)  # backward

    best_k, best = 0, None
    for k in range(m + 1):
        s = L[k] + R[m - k]
        if best is None or s > best:
            best, best_k = s, k

    a1, b1 = align(a[:mid], b[:best_k], match, mismatch, gap)
    a2, b2 = align(a[mid:], b[best_k:], match, mismatch, gap)
    return a1 + a2, b1 + b2
```

### Why it is correct

- **Score sweeps are exact.** `L[k]` is the optimal alignment score of `a[:mid]` vs
  `b[:k]`; `R[m-k]` is the optimal score of `a[mid:]` vs `b[k:]` (the backward sweep runs
  on reversed strings, and alignment score is invariant under reversing both). Their sum,
  maximised over `k`, equals `dp[n][m]` and pinpoints a valid crossing column.
- **Recomposition preserves order and completeness.** The two recursive alignments cover
  disjoint prefixes/suffixes, so concatenating them yields equal-length strings whose
  gap-stripped versions are exactly `a` and `b`. Validated against a brute-force optimum
  over thousands of random pairs and several scoring schemes.

### Complexity

- **Time:** `O(n·m)` — the halving of grid area per recursion level gives the geometric
  sum `≤ 2·n·m`.
- **Space:** `O(min(n, m))` for the two rolling score rows (index by the shorter string),
  `O(log n)` recursion stack, plus the `O(n + m)` output. The `_base_align` helper only
  ever runs on a `1 × m` (or empty) strip, so it uses `O(m)` — still linear.

## Key Insights & Edge Cases

- **Border initialisation matters.** Unlike LCS (borders all 0), alignment borders are
  `i·gap` / `j·gap` because reaching a prefix by pure gaps has a real (negative) cost.
  Getting this wrong silently produces suboptimal scores.
- **Single-row base case:** handled by a tiny full DP with traceback (`_base_align`) rather
  than an ad-hoc rule, because with general scores the best placement of one character
  against `b` can be a match, a mismatch, or a gap depending on the numbers. This keeps the
  recovered alignment provably optimal.
- **Empty inputs:** align the non-empty string entirely against gaps.
- **Gap-only vs mismatch trade-off:** with `match=1, mismatch=-1, gap=-2`, inserting a gap
  (`-2`) is worse than a single mismatch (`-1`) but the surrounding matches can still make a
  gap-bearing alignment win overall (Examples 1 and 2 both prefer one gap to a forced
  mismatch cascade).
- **This is the historical motivation for Hirschberg's algorithm** — aligning long
  biological sequences where the quadratic-space table is the binding constraint, not time.
- **Extending to affine gaps** (opening + extension penalties, Gotoh's algorithm) needs
  three rolling rows instead of one but keeps the same linear-space divide-and-conquer
  structure.
