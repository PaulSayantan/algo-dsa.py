# Solution — Shortest Common Supersequence

## Brute Force

Generate candidate supersequences by interleaving `str1` and `str2` in every
possible way and keep the shortest one that contains both as subsequences. The
number of interleavings is `C(n+m, n)` — exponential. Even just enumerating all
strings up to length `n + m` and testing is hopeless.

## Optimal Approach — Longest Common Subsequence (DP)

**Length insight.** The shortest common supersequence writes every character of
both strings, but the characters that the two strings *share in order* (their
LCS) only need to be written **once**. So:

```
len(SCS) = len(str1) + len(str2) - len(LCS)
```

To actually build the string we need the LCS *path*, not just its length, so we
reconstruct.

**Step 1 — build the LCS table.** Standard DP: `dp[i][j]` = LCS length of
`str1[:i]` and `str2[:j]`.

- `str1[i-1] == str2[j-1]` -> `dp[i][j] = dp[i-1][j-1] + 1`.
- else -> `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

**Step 2 — walk backward from `dp[n][m]` to build the SCS.** Maintain pointers
`i = n`, `j = m` and append characters, then reverse at the end:

- If `str1[i-1] == str2[j-1]`: this character is part of the LCS — write it once,
  step `i -= 1, j -= 1`.
- Else if `dp[i-1][j] >= dp[i][j-1]`: the LCS path came from above — write
  `str1[i-1]` (a unique char of `str1`), step `i -= 1`.
- Else: write `str2[j-1]`, step `j -= 1`.
- When one string is exhausted, append the remaining prefix of the other.

**Why it is correct.** Any common supersequence must contain both strings as
subsequences; the minimum overlap you can achieve between them is exactly their
LCS, and the reconstruction realizes that overlap by emitting shared characters
a single time while preserving each string's internal order. Hence the built
string is a valid supersequence of both and has the minimum possible length.

**Worked example** for `str1 = "abac"`, `str2 = "cab"`. LCS is `"ab"` (length
2), so `len(SCS) = 4 + 3 - 2 = 5`. Backward walk yields `"cabac"` (one of the
valid answers).

```python
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        i, j, out = n, m, []
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                out.append(str1[i - 1]); i -= 1; j -= 1
            elif dp[i - 1][j] >= dp[i][j - 1]:
                out.append(str1[i - 1]); i -= 1
            else:
                out.append(str2[j - 1]); j -= 1
        while i > 0:
            out.append(str1[i - 1]); i -= 1
        while j > 0:
            out.append(str2[j - 1]); j -= 1
        return "".join(reversed(out))
```

- **Time:** `O(n * m)` to fill the table plus `O(n + m)` to reconstruct.
- **Space:** `O(n * m)` — the full table is required for the backward walk, so
  the rolling-row trick is *not* applicable when you must reconstruct the string.

## Key Insights & Edge Cases

- **Reconstruction needs the whole table.** Problems that ask only for a length
  can drop to `O(min(n,m))` space; problems that ask for the actual string
  cannot, because backtracking reads earlier rows.
- **Tie-breaking is free:** when `dp[i-1][j] == dp[i][j-1]` either direction
  gives a valid shortest answer, which is why multiple outputs are accepted.
- **Identical strings** produce the string itself (LCS = whole string).
- **No common characters** produces a simple concatenation of the two strings,
  length `n + m` (LCS = 0).
- Don't forget the two trailing `while` loops that flush the remainder of
  whichever string is not yet exhausted.
