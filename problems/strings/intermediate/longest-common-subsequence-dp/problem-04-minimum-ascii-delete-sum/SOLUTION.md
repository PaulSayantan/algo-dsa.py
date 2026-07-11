# Solution — Minimum ASCII Delete Sum for Two Strings

## Brute Force

Enumerate every common subsequence of `s1` and `s2`; for each, the delete cost
is `total_ascii(s1) + total_ascii(s2) - 2 * ascii_sum(common)`. Keep the minimum
cost, i.e. maximize `ascii_sum(common)`. Enumerating subsequences is
exponential, `O(2^n * m)`.

## Optimal Approach — Longest Common Subsequence (DP)

This is a **weighted LCS**. In plain LCS every kept character is worth `1`; here
each kept character is worth its ASCII value, and we maximize the total value of
the common subsequence we keep. Everything not kept is deleted, so the answer is:

```
total_ascii(s1) + total_ascii(s2) - 2 * maxKeptAsciiSum
```

There are two equivalent formulations. The cleanest defines the DP directly on
delete cost.

**DP definition.** `dp[i][j]` = minimum ASCII delete sum to make `s1[:i]` and
`s2[:j]` equal.

**Base cases.** To equalize with an empty prefix you must delete the whole other
prefix:

- `dp[i][0] = ascii(s1[0]) + ... + ascii(s1[i-1])`
- `dp[0][j] = ascii(s2[0]) + ... + ascii(s2[j-1])`

**Recurrence.**

- If `s1[i-1] == s2[j-1]`: keep both (free) -> `dp[i][j] = dp[i-1][j-1]`.
- Else delete the cheaper side to make progress:
  `dp[i][j] = min(dp[i-1][j] + ascii(s1[i-1]), dp[i][j-1] + ascii(s2[j-1]))`.

**Why it is correct.** When the trailing characters match, deleting either is
never beneficial, so we align them at zero cost and recurse on the smaller
problem. When they differ, at least one trailing character can never be part of
the final equal string, so we pay to delete one of them and recurse. The `min`
over these exhaustive options yields the optimum by induction on `i + j`.

**Worked example** for `s1 = "sea"`, `s2 = "eat"` (`s`=115, `e`=101, `a`=97,
`t`=116):

```
         ""    e     a     t
   ""     0   101   198   314
   s    115   216   313   429
   e    216   115   212   328
   a    313   212   115   231
```

Answer `dp[3][3] = 231` — matching deletions of `s`(115) and `t`(116).

```python
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]),
                                   dp[i][j - 1] + ord(s2[j - 1]))
        return dp[n][m]
```

- **Time:** `O(n * m)`.
- **Space:** `O(n * m)`, reducible to `O(min(n, m))` with a rolling row.

**Alternative:** compute the max-ASCII common subsequence with a weighted LCS
(`dp[i][j] = dp[i-1][j-1] + ord(c)` on match, else `max(...)`) and subtract from
the total ASCII of both strings — same answer.

## Key Insights & Edge Cases

- **Weighted LCS lens:** whenever "make equal by deleting" pairs with per-item
  costs, generalize LCS from "count kept" to "sum kept value" (or, equivalently,
  "minimize deleted cost").
- **Greedy fails:** always deleting the smaller trailing ASCII is wrong; equal
  characters must be kept even when they are large, which is exactly what the
  match branch enforces.
- **No common characters:** the answer is the ASCII sum of both entire strings.
- **Identical strings:** the answer is `0`.
