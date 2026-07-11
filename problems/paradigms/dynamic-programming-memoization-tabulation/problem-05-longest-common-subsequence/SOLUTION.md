# Solution — Longest Common Subsequence

## Brute Force

Recurse on the two prefix lengths; at each step compare the last characters:

```python
def lcs(i, j):
    if i == 0 or j == 0:
        return 0
    if text1[i - 1] == text2[j - 1]:
        return 1 + lcs(i - 1, j - 1)
    return max(lcs(i - 1, j), lcs(i, j - 1))
```

Alternatively, enumerate all `2^m` subsequences of `text1` and check each against
`text2`. Either way the work is exponential.

- **Time:** `O(2^(m+n))` for the naive branching recursion.
- **Space:** `O(m + n)` recursion depth.

The `(i, j)` prefix pair recurs from many call paths — overlapping subproblems.

## Optimal Approach (Dynamic Programming)

**State:** `dp[i][j]` = LCS length of the first `i` characters of `text1` and the first
`j` characters of `text2`.

**Recurrence:**

```
if text1[i - 1] == text2[j - 1]:
    dp[i][j] = dp[i - 1][j - 1] + 1        # matched char extends the LCS
else:
    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # drop one char from either string
```

**Base cases:** `dp[0][j] = dp[i][0] = 0` (an empty prefix shares nothing).

### Bottom-up (tabulation)

```python
class Solution:
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

**Why it is correct:** Consider the last characters of both prefixes. If they are equal,
that character can end a common subsequence, so the answer is one more than the LCS of
the two shorter prefixes. If they differ, at least one of them is not in the optimal LCS,
so we drop it and take the better branch. These cases are exhaustive, giving optimal
substructure.

### Trace on `text1 = "abcde", text2 = "ace"` (rows = text1 prefixes, cols = text2 prefixes)

```
        ""  a  c  e
    ""   0  0  0  0
    a    0  1  1  1
    b    0  1  1  1
    c    0  1  2  2
    d    0  1  2  2
    e    0  1  2  3
```

Bottom-right cell `dp[5][3] = 3`, matching subsequence `"ace"`. ✔

### Space optimization

Each cell depends only on the current and previous row, so two rows (or one row plus a
diagonal temp) reduce space to `O(min(m, n))`.

- **Time:** `O(m * n)` — one constant-work cell per `(i, j)` pair.
- **Space:** `O(m * n)` for the full table, or `O(min(m, n))` when rolling rows.

## Key Insights & Edge Cases

- This is the prototypical **2D grid DP over two sequences**; edit distance, shortest
  common supersequence, and diff tools all share this skeleton.
- **1-based indexing** on the table (with a padding row/column of zeros) keeps the base
  cases clean and avoids off-by-one errors when reading `text1[i - 1]`.
- **No common characters** → the whole table stays 0, correctly returning 0.
- **Subsequence vs. substring:** subsequences allow gaps, which is exactly why the
  "drop one character" transition is valid; a *substring* problem would need a different,
  contiguity-preserving recurrence.
- To recover the actual subsequence (not just its length), backtrack from `dp[m][n]`
  following the choices that produced each cell.
