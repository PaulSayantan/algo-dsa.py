# Solution — Longest Common Subsequence

## Brute Force

Enumerate every subsequence of `text1` (there are `2^n` of them) and, for each,
check whether it is also a subsequence of `text2`; keep the longest match.

- **Time:** `O(2^n * m)` — exponential in the length of `text1`.
- **Space:** `O(n)` for the recursion / candidate string.

An equivalent recursive framing (without memoization) compares the last
characters:

```
def lcs(i, j):
    if i == 0 or j == 0:
        return 0
    if text1[i-1] == text2[j-1]:
        return 1 + lcs(i-1, j-1)
    return max(lcs(i-1, j), lcs(i, j-1))
```

This recursion re-solves the same `(i, j)` subproblems over and over, giving
exponential time. Memoizing it is exactly the DP below.

## Optimal Approach — Longest Common Subsequence (DP)

Define `dp[i][j]` = length of the LCS of the prefix `text1[:i]` and the prefix
`text2[:j]`. There are only `(n+1) * (m+1)` distinct subproblems.

**Recurrence.** Look at the last characters of each prefix:

- If `text1[i-1] == text2[j-1]`, that shared character can end the LCS, so
  `dp[i][j] = dp[i-1][j-1] + 1`.
- Otherwise at least one of the two characters is not in the LCS, so
  `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

**Base case.** `dp[0][j] = dp[i][0] = 0` — an empty prefix shares nothing.

**Why it is correct.** Every common subsequence either uses the pair of equal
trailing characters (reducing to the smaller `dp[i-1][j-1]` problem plus one) or
it drops one of the two trailing characters (reducing to `dp[i-1][j]` or
`dp[i][j-1]`). The recurrence takes the best of these mutually exhaustive cases,
so by induction on `i + j` each cell holds the true optimum.

**Step by step** for `text1 = "abcde"`, `text2 = "ace"`:

```
       ""  a  c  e
   ""   0  0  0  0
   a    0  1  1  1
   b    0  1  1  1
   c    0  1  2  2
   d    0  1  2  2
   e    0  1  2  3
```

The bottom-right cell is `3`.

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n][m]
```

- **Time:** `O(n * m)` — fill every cell once.
- **Space:** `O(n * m)`, reducible to `O(min(n, m))` by keeping only the
  previous row (see below).

**Space-optimized rolling row:**

```python
def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    if len(text1) < len(text2):
        text1, text2 = text2, text1
    prev = [0] * (len(text2) + 1)
    for c1 in text1:
        curr = [0] * (len(text2) + 1)
        for j, c2 in enumerate(text2, 1):
            curr[j] = prev[j - 1] + 1 if c1 == c2 else max(prev[j], curr[j - 1])
        prev = curr
    return prev[-1]
```

## Key Insights & Edge Cases

- **Subsequence, not substring:** characters need not be contiguous, only in
  order. That distinction is exactly why the "skip a character" branches exist.
- **1-based DP indexing** with an extra zero row/column removes special-casing
  for empty prefixes.
- **No common characters** yields `0` (handled naturally by the zero base row).
- **Identical strings** give `dp[n][m] = n` — the whole string is the LCS.
- To **reconstruct** the actual subsequence, walk back from `dp[n][m]`: on a
  match step diagonally and emit the character; otherwise move toward the larger
  of `dp[i-1][j]` / `dp[i][j-1]`.
