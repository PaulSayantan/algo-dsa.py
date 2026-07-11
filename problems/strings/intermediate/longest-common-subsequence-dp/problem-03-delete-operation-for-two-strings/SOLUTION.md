# Solution — Delete Operation for Two Strings

## Brute Force

Try every subsequence of `word1`, check if it is also a subsequence of `word2`,
and among all common ones pick the longest; deletions equal the characters left
over in both strings. Enumerating subsequences is `O(2^n * m)` — exponential.

## Optimal Approach — Longest Common Subsequence (DP)

**Key reduction.** After all deletions the two strings become identical; call
that common result `s`. Since we only ever *delete* (never insert or replace),
`s` must be a subsequence of `word1` **and** a subsequence of `word2` — i.e. a
common subsequence. To minimize deletions we maximize the length of `s`, so `s`
is the LCS. The characters we delete are exactly those not in the LCS:

```
deletions = (len(word1) - LCS) + (len(word2) - LCS)
          = len(word1) + len(word2) - 2 * LCS
```

So compute the LCS length with the standard 2D DP, then apply the formula.

**Recurrence** (same as canonical LCS): `dp[i][j]` = LCS of `word1[:i]` and
`word2[:j]`:

- `word1[i-1] == word2[j-1]` -> `dp[i][j] = dp[i-1][j-1] + 1`.
- else -> `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

**Why it is correct.** Any sequence of deletions that equalizes the strings
leaves a common subsequence; conversely any common subsequence is reachable by
deleting everything else. Thus minimum deletions correspond one-to-one with the
maximum common subsequence, which the DP computes optimally.

**Worked example** for `word1 = "sea"`, `word2 = "eat"`:

```
        ""  e  a  t
   ""    0  0  0  0
   s     0  0  0  0
   e     0  1  1  1
   a     0  1  2  2
```

LCS `= dp[3][3] = 2` (the subsequence `"ea"`). Deletions
`= 3 + 3 - 2*2 = 2`.

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        lcs = dp[n][m]
        return n + m - 2 * lcs
```

- **Time:** `O(n * m)`.
- **Space:** `O(n * m)`, reducible to `O(min(n, m))`.

**Direct DP variant.** You can also define `dp[i][j]` as the deletions to equate
the prefixes directly: `dp[i][0] = i`, `dp[0][j] = j`, and
`dp[i][j] = dp[i-1][j-1]` on a match else `1 + min(dp[i-1][j], dp[i][j-1])`.
This is the same computation reorganized.

## Key Insights & Edge Cases

- **The `n + m - 2*LCS` trick** appears repeatedly whenever "keep the common
  part, delete the rest" describes the operation — memorize it.
- **Already equal strings** give `LCS = n = m`, so deletions `= 0`.
- **No common characters** gives `LCS = 0`, so you delete both strings entirely:
  `deletions = n + m`.
- This is *not* full edit distance — there are no substitutions or insertions,
  only deletions, which is exactly why LCS (not Levenshtein) is the right tool.
