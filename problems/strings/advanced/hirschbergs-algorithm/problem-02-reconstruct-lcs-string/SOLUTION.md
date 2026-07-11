# Solution — Reconstruct the LCS in Linear Space

## Brute Force

Compute the full `O(n·m)` DP table of LCS lengths, then **backtrack** from `dp[n][m]`:
at each cell move diagonally (emitting a character) when `a[i-1] == b[j-1]`, otherwise
step toward the larger of `dp[i-1][j]` / `dp[i][j-1]`.

- **Time:** `O(n·m)`
- **Space:** `O(n·m)` — the whole table must be retained for the backtrack. This is what
  we are trying to avoid for large inputs.

## Optimal Approach — Hirschberg's Algorithm

### The key lemma

Let `n = len(a)`, and split `a` at the middle row `mid = n // 2` into `a[:mid]` and
`a[mid:]`. There is always an optimal LCS "path" through the DP grid that crosses row
`mid` at *some* column `k`. If we knew `k`, the problem would decompose into two
independent subproblems: LCS of `(a[:mid], b[:k])` plus LCS of `(a[mid:], b[k:])`.

To find `k` without the full table, compute two length-only score rows:

- `L[j]` = LCS length of `a[:mid]` and `b[:j]`  (forward pass).
- `R[j]` = LCS length of `reverse(a[mid:])` and `reverse(b[j:])`, i.e. the LCS of the
  *suffix* `a[mid:]` and the suffix `b[j:]`  (backward pass).

Then the best crossing column maximises `L[k] + R[k]` over all `k` in `0..m`, and that
maximum equals the total LCS length. Each score row costs `O(min · other)` time and only
`O(m)` (or `O(min(n,m))`) space.

### Step by step

```python
from typing import List


def lcs_score_row(a: str, b: str) -> List[int]:
    prev = [0] * (len(b) + 1)
    for i in range(1, len(a) + 1):
        curr = [0] * (len(b) + 1)
        ai = a[i - 1]
        for j in range(1, len(b) + 1):
            if ai == b[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = prev[j] if prev[j] >= curr[j - 1] else curr[j - 1]
        prev = curr
    return prev


def longest_common_subsequence(a: str, b: str) -> str:
    n, m = len(a), len(b)

    # Base cases.
    if n == 0 or m == 0:
        return ""
    if n == 1:
        return a if a in b else ""   # single row: match the lone char if present

    mid = n // 2
    L = lcs_score_row(a[:mid], b)                       # forward scores
    R = lcs_score_row(a[mid:][::-1], b[::-1])           # backward scores (reversed)

    # Find the column k that maximises L[k] + R[m - k].
    best_k, best_val = 0, -1
    for k in range(m + 1):
        total = L[k] + R[m - k]
        if total > best_val:
            best_val, best_k = total, k

    # Divide and conquer around (mid, best_k).
    return (longest_common_subsequence(a[:mid], b[:best_k])
            + longest_common_subsequence(a[mid:], b[best_k:]))
```

Note the reversed backward row: `R = lcs_score_row(reverse(a[mid:]), reverse(b))`, and
`R[m - k]` is the LCS length of `a[mid:]` with the suffix `b[k:]`. Adding `L[k]` gives the
best total achievable when the split happens after column `k`.

### Why it is correct

- **Optimal substructure:** any common subsequence of `a` and `b` splits at row `mid`
  into a common subsequence of `(a[:mid], b[:k])` and one of `(a[mid:], b[k:])` for the
  column `k` where it crosses. Maximising over `k` recovers a global optimum.
- **The score rows are exact:** `L[k]` and `R[m-k]` are true LCS lengths of the
  corresponding prefix/suffix pairs (Problem 1's routine), so `max_k L[k] + R[m-k]` is the
  true LCS length, and its argmax is a valid crossing column.
- Recursing on the two halves and concatenating yields characters in correct left-to-right
  order because `a[:mid]/b[:k]` lies entirely above-left of `a[mid:]/b[k:]`.

### Complexity

- **Time:** `O(n·m)`. The two score passes at the top level cost `≈ n·m`; the recursion
  works on two subgrids whose combined area is at most half the parent's, giving
  `nm + nm/2 + nm/4 + … ≤ 2·nm = O(n·m)`.
- **Space:** `O(min(n, m))` for the score rows (index the row by the shorter dimension),
  plus `O(log n)` recursion-stack depth, plus the `O(LCS length)` output.

## Key Insights & Edge Cases

- **The `n == 1` base case is essential.** With a single row the "crossing column" idea
  degenerates; you simply check whether that one character occurs in `b`. Forgetting it
  causes infinite recursion (`mid` becomes `0`, and `a[:0]` never shrinks the problem).
- **Reverse carefully.** The backward pass runs on `reverse(a[mid:])` vs `reverse(b)`, and
  you must index it as `R[m - k]`, not `R[k]`.
- **Empty inputs** return `""` immediately.
- **Any valid LCS is accepted.** The tie-break in the `max` (and in the crossing-column
  search) chooses one specific optimal subsequence; a different consistent tie-break may
  return a different but equally long string.
- **Linear space is real, not asymptotic hand-waving:** at no point is an `O(n·m)`
  structure allocated — only rolling rows of width `O(min(n, m))`.
