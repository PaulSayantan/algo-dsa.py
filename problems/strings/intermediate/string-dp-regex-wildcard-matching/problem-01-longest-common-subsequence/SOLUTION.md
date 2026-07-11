# Longest Common Subsequence — Solution

## Brute Force

Enumerate every subsequence of `text1` (there are `2^m` of them) and, for each,
check whether it is also a subsequence of `text2`, keeping the longest match.

- **Time:** `O(2^m * n)` — exponential in the length of the first string.
- **Space:** `O(m)` for the recursion stack.

Equivalently, a plain recursion compares the last characters and branches:

```
lcs(i, j):
    if i == 0 or j == 0: return 0
    if text1[i-1] == text2[j-1]: return 1 + lcs(i-1, j-1)
    return max(lcs(i-1, j), lcs(i, j-1))
```

This recomputes the same `(i, j)` states many times, which is exactly what DP
removes.

## Optimal Approach (String DP)

Let `dp[i][j]` be the length of the LCS of `text1[:i]` and `text2[:j]`.

**Transitions**

- If `text1[i-1] == text2[j-1]`, the two characters can be paired up and appended
  to the LCS of the shorter prefixes:
  `dp[i][j] = dp[i-1][j-1] + 1`.
- Otherwise, at least one of the two current characters cannot be in the common
  subsequence, so we drop one and take the better option:
  `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

**Base case:** `dp[0][j] = dp[i][0] = 0` — an empty prefix shares nothing.

**Why it is correct:** every common subsequence either uses the matched pair
`(text1[i-1], text2[j-1])` or it does not. The two transitions cover exactly
those two cases, and because sub-answers are optimal for smaller prefixes
(optimal substructure), the maximum over them is optimal for `(i, j)`.

**Step by step** for `text1 = "abcde"`, `text2 = "ace"`:

```
        ""  a  c  e
    ""   0  0  0  0
     a   0  1  1  1
     b   0  1  1  1
     c   0  1  2  2
     d   0  1  2  2
     e   0  1  2  3   <- answer dp[5][3] = 3  ("ace")
```

**Reference implementation**

```python
def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
```

- **Time:** `O(m * n)` — one constant-time transition per cell.
- **Space:** `O(m * n)`, reducible to `O(min(m, n))` with two rolling rows since
  each cell reads only the current and previous row.

## Key Insights & Edge Cases

- **This is the template.** Edit distance, distinct subsequences, and pattern
  matching all reuse the "diagonal on match, otherwise combine neighbors"
  skeleton. Learn this table shape first.
- **Subsequence vs. substring:** characters need not be contiguous, so a
  non-match still lets us keep progress by dropping just one character.
- **Empty strings:** the `dp[0][*]` and `dp[*][0]` row/column of zeros handles
  them automatically; no special-casing needed.
- **Rolling array:** if you only need the length (not the actual subsequence),
  keep two 1D rows. To reconstruct the subsequence itself, keep the full table
  and walk back from `dp[m][n]`.
- **All-distinct inputs** (Example 3) naturally yield `0` because no diagonal
  step is ever taken.
