# Distinct Subsequences

**Difficulty:** Hard

**Source:** LeetCode 115 — Distinct Subsequences

## Description

Given two strings `s` and `t`, return the **number of distinct subsequences of
`s` which equal `t`**.

A subsequence of a string is obtained by deleting some (possibly zero)
characters without changing the relative order of the remaining characters.
(For example, `"ACE"` is a subsequence of `"ABCDE"` while `"AEC"` is not.)

The answer is guaranteed to fit in a 32-bit signed integer.

This is the **counting** flavor of 2D string DP: instead of a max or a boolean,
each cell accumulates the *number of ways* the prefix `t[:j]` can be formed as a
subsequence of `s[:i]`. It is the natural bridge from LCS/Edit-Distance toward
the pattern-matching problems, because the `'*'`-style "take it or leave it"
branching shows up here as a sum rather than an OR.

## Constraints

- `1 <= s.length, t.length <= 1000`
- `s` and `t` consist of English letters.

## Examples

### Example 1

```
Input:  s = "rabbbit", t = "rabbit"
Output: 3
Explanation: There are 3 ways to form "rabbit" from "rabbbit" by deleting one
             of the three 'b's:
  rabb b it   (delete the 3rd b)
  rab b bit   (delete the 2nd b)
  ra b bbit   (delete the 1st b)
```

### Example 2

```
Input:  s = "babgbag", t = "bag"
Output: 5
Explanation: There are 5 ways to form "bag" as a subsequence:
  ba___g, ba____g, b____ag, ____bag, and __b__ag (choosing different b/a/g
  positions). The count is 5.
```

### Example 3

```
Input:  s = "abc", t = "abcd"
Output: 0
Explanation: t is longer than s, so it cannot be a subsequence — 0 ways.
```

## Hint

Use **String DP (regex/wildcard matching)** in its counting form: let
`dp[i][j]` be the number of ways `t[:j]` appears as a subsequence of `s[:i]`.
You may always skip `s[i-1]` (`dp[i-1][j]`); if `s[i-1] == t[j-1]` you may
*additionally* use it (`+ dp[i-1][j-1]`). Add the two options together.
