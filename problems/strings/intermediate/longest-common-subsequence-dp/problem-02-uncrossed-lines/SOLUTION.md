# Solution — Uncrossed Lines

## Brute Force

Try every subset of matching index pairs `(i, j)` with `nums1[i] == nums2[j]`,
keep only the subsets where the pairs are strictly increasing in both `i` and
`j` (so no two lines cross), and return the size of the largest such subset.
The number of subsets is exponential, so this is `O(2^(n*m))`-ish and hopeless
beyond tiny inputs.

## Optimal Approach — Longest Common Subsequence (DP)

**Key reduction.** Two lines `(i1, j1)` and `(i2, j2)` cross exactly when one
line's top endpoint is to the left but its bottom endpoint is to the right of
the other. Requiring *no* crossings means the chosen pairs must satisfy: if
`i1 < i2` then `j1 < j2`. In other words, the connected values, read left to
right, form the **same ordered sequence in both arrays** — a common
subsequence. Maximizing the number of lines = maximizing the length of a common
subsequence = **LCS**.

So the problem is identical to LeetCode 1143, but comparing integers instead of
characters.

**Recurrence.** Let `dp[i][j]` = max lines using the first `i` of `nums1` and
first `j` of `nums2`:

- If `nums1[i-1] == nums2[j-1]`: `dp[i][j] = dp[i-1][j-1] + 1`.
- Else: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

Base case `dp[0][*] = dp[*][0] = 0`.

**Why it is correct.** Same inductive argument as standard LCS: the optimal set
of lines either pairs the two current trailing elements (when equal) or omits
at least one of them; the recurrence takes the maximum over these exhaustive
choices.

**Worked example** for `nums1 = [1,4,2]`, `nums2 = [1,2,4]`:

```
        ""  1  2  4
   ""    0  0  0  0
   1     0  1  1  1
   4     0  1  1  2
   2     0  1  2  2
```

Answer `dp[3][3] = 2`.

```python
class Solution:
    def maxUncrossedLines(self, nums1, nums2):
        n, m = len(nums1), len(nums2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n][m]
```

- **Time:** `O(n * m)`.
- **Space:** `O(n * m)`, reducible to `O(min(n, m))` with a rolling row.

## Key Insights & Edge Cases

- **Recognize the disguise:** "keep relative order, no crossing" is a giant flag
  for LCS. Many LCS problems are worded to hide the reduction.
- **Duplicates matter:** the same value can appear multiple times; the DP handles
  this automatically because it works on positions, not on value sets.
- **Arrays of length 1:** the answer is `1` if the single elements match, else
  `0` — covered by the base row/column.
- Only the *count* of lines is asked, so no reconstruction is needed, but the
  same back-tracking trick from problem 1 would recover which pairs to connect.
