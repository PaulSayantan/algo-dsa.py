# Longest Palindromic Subsequence — Solution

## Brute Force

Enumerate every subsequence of `s`, test each for being a palindrome, and keep
the longest. There are `2^n` subsequences.

- **Time:** `O(2^n * n)` — exponentially many subsequences, `O(n)` palindrome test each.
- **Space:** `O(n)` recursion depth.

Hopeless for `n = 1000`.

## Optimal Approach (Range / Interval DP)

Define the state over a **contiguous interval** of the string:

> `dp[i][j]` = length of the longest palindromic subsequence within `s[i..j]`
> (inclusive).

**Recurrence** — compare the two endpoints of the interval:

- If `s[i] == s[j]`: the two matching characters can wrap the best palindrome of
  the inner interval:
  `dp[i][j] = dp[i+1][j-1] + 2`.
- Otherwise, at least one endpoint is unused:
  `dp[i][j] = max(dp[i+1][j], dp[i][j-1])`.

**Base case:** every single character is a palindrome of length 1, so
`dp[i][i] = 1`. (When `i > j` the interval is empty and contributes 0, which the
`dp[i+1][j-1]` term handles automatically for the `j == i+1` case since a
2-length equal pair gives `0 + 2 = 2`.)

**Why it is correct.** A longest palindromic subsequence of `s[i..j]` either uses
both endpoints (only possible/optimal to pair them when they are equal — pairing
equal endpoints never hurts), or it skips at least one endpoint. Those cases are
exactly the branches above, and each references a strictly smaller interval, so
the recursion is well-founded and covers all optimal structures.

**Iteration order.** `dp[i][j]` needs `dp[i+1][...]` (a larger `i`) and
`dp[...][j-1]` (a smaller `j`). Iterate `i` from `n-1` down to `0`, and `j` from
`i+1` up to `n-1`.

```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]
```

- **Time:** `O(n^2)` — one `O(1)` transition per interval.
- **Space:** `O(n^2)`; reducible to `O(n)` with two rolling rows.

### Trace for `s = "bbbab"`

The interval `dp[0][4]` covers the whole string. Endpoints `s[0]='b'`,
`s[4]='b'` match, so `dp[0][4] = dp[1][3] + 2`. Inside, `s[1..3] = "bba"`
yields `dp[1][3] = 3` ("bbb" via the equal 'b's), giving `dp[0][4] = 4`.

## Key Insights & Edge Cases

- This is the **easiest interval-DP shape**: the transition compares only the two
  endpoints, so it is `O(1)` (no inner split loop). It is the ideal warm-up
  before matrix-chain-style `O(n^3)` problems.
- **Subsequence vs. substring:** because we allow deletions, the recurrence can
  independently drop either endpoint. (Contrast with longest palindromic
  *substring*, where a break at either end kills the whole candidate.)
- Longest palindromic subsequence of `s` equals the **LCS of `s` and `reverse(s)`** —
  a neat sanity check, though the interval-DP form is more direct.
- **Single character** (`n == 1`) returns 1. A string with all distinct
  characters returns 1. A string that is already a palindrome returns `n`.
