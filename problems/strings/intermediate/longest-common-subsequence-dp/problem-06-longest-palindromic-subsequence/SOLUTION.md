# Solution — Longest Palindromic Subsequence

## Brute Force

Generate every subsequence of `s` (there are `2^n`), test each for being a
palindrome, and keep the longest. That is `O(2^n * n)` — exponential and
infeasible for `n` up to 1000.

## Optimal Approach — Longest Common Subsequence (DP)

**Key reduction.** A string is a palindrome iff it equals its own reverse. So a
palindromic subsequence of `s` is a subsequence that appears in both `s` and
`reverse(s)` at corresponding positions — i.e. a **common subsequence of `s`
and its reverse**. Therefore:

```
LongestPalindromicSubseq(s) = LCS(s, reverse(s))
```

Let `t = reverse(s)` and run the standard LCS DP on `s` and `t`.

**Recurrence.** `dp[i][j]` = LCS of `s[:i]` and `t[:j]`:

- `s[i-1] == t[j-1]` -> `dp[i][j] = dp[i-1][j-1] + 1`.
- else -> `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

Answer is `dp[n][n]`.

**Why it is correct.** Any palindromic subsequence `p` of `s` reads identically
forwards and backwards; reading it backwards is a subsequence of `t = reverse(s)`
and reading it forwards is a subsequence of `s`, so `p` is a common subsequence,
giving `LPS <= LCS(s, t)`. Conversely one can show the LCS of `s` and its
reverse is always itself a palindrome, so `LCS(s, t) <= LPS`. The two bounds
meet, proving equality.

**Worked example** for `s = "bbbab"`, `t = "babbb"`:

The LCS of `"bbbab"` and `"babbb"` is `"bbbb"` of length 4, which is exactly the
longest palindromic subsequence.

```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        t = s[::-1]
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n][n]
```

- **Time:** `O(n^2)` (this is `O(n * m)` with `m = n`).
- **Space:** `O(n^2)`, reducible to `O(n)` with a rolling row.

**Direct interval DP (equivalent).** You can also solve it without reversing, by
defining `dp[i][j]` = LPS of the substring `s[i..j]`: if `s[i] == s[j]` then
`dp[i][j] = dp[i+1][j-1] + 2`, else `dp[i][j] = max(dp[i+1][j], dp[i][j-1])`,
with `dp[i][i] = 1`. Same `O(n^2)` complexity; the reverse-LCS framing is
included here to reinforce the LCS pattern.

## Key Insights & Edge Cases

- **"Palindrome subsequence" = LCS with the reverse** is a classic reduction
  worth memorizing; it turns a self-referential condition into a two-string LCS.
- **Single character** always yields `1`.
- **All identical characters** yields `n` (the whole string is a palindrome).
- **No repeated characters** (e.g. `"abcd"`) yields `1`, since any single
  character is a length-1 palindrome.
- The interval-DP variant is preferred in practice for palindrome problems
  because it avoids allocating the reversed string, but both are `O(n^2)`.
