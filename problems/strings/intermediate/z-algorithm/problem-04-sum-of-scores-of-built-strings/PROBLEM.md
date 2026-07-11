# Sum of Scores of Built Strings

**Difficulty:** Hard

**Source:** LeetCode 2223 — "Sum of Scores of Built Strings".

## Description

You are building a string `s` of length `n` **one character at a time, always
prepending the new character to the front**. Formally, if the final string is
`s` (with `1`-indexed convention `s_1 s_2 ... s_n`), then after the `i`-th
operation you hold the string `s_i` consisting of the **last `i` characters** of
`s` — that is, the suffix `s[n - i:]`. The last built string `s_n` equals the
whole string `s`.

The **score** of a built string `s_i` is the length of the **longest common
prefix** between `s_i` and the final string `s_n` (which is `s`).

Return the **sum of the scores** of every built string `s_1, s_2, ..., s_n`.

This is a direct application of the Z-Algorithm: `z[j]` is by definition the
length of the longest common prefix of `s` and its suffix `s[j:]`. The suffix
`s[n - i:]` corresponds to index `j = n - i`, so the score of `s_i` is exactly
`z[n - i]`. Summing over all `i` sums the entire Z-array (with `z[0] = n`, since
`s_n = s` matches `s` completely).

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.

## Examples

### Example 1

```
Input:  s = "babab"
Output: 9
Explanation: The built strings and their scores (LCP with "babab"):
  s_1 = "b"     -> LCP with "babab" = "b"      -> score 1
  s_2 = "ab"    -> LCP with "babab" = ""       -> score 0
  s_3 = "bab"   -> LCP with "babab" = "bab"    -> score 3
  s_4 = "abab"  -> LCP with "babab" = ""       -> score 0
  s_5 = "babab" -> LCP with "babab" = "babab"  -> score 5
Sum = 1 + 0 + 3 + 0 + 5 = 9.
```

### Example 2

```
Input:  s = "azbazbzaz"
Output: 14
Explanation: Only three built strings share a prefix with s = "azbazbzaz":
  s_2 = "az"      -> LCP with s = "az"   -> score 2
  s_6 = "azbzaz"  -> LCP with s = "azb"  -> score 3
  s_9 = "azbazbzaz" (the full string) -> LCP = "azbazbzaz" -> score 9
Every other built string has score 0. Sum = 2 + 3 + 9 = 14.
```

## Hint

The score of the built string with `i` characters is the length of the longest
common prefix of `s` and its suffix of length `i`. That is precisely a
**Z-array** value, so the answer is the **sum of the Z-array** of `s` (taking
`z[0] = n`).
