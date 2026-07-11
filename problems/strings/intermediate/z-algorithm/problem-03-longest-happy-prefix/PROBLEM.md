# Longest Happy Prefix

**Difficulty:** Medium

**Source:** LeetCode 1392 — "Longest Happy Prefix".

## Description

A string is called a **happy prefix** if it is a **non-empty prefix** which is
also a **suffix** — but excluding the whole string itself (a *proper* prefix and
suffix).

Given a string `s`, return the **longest happy prefix** of `s`. If no such
non-empty prefix exists, return the empty string `""`.

With the Z-Algorithm the answer falls out of a single observation: the suffix of
`s` that starts at index `i` is identical to a prefix of `s` **exactly when**
`z[i] == n - i` (the match reaches all the way to the end of the string). Among
all indices `i >= 1` satisfying that, the **smallest** `i` gives the **longest**
border, of length `n - i`.

## Constraints

- `1 <= s.length <= 10^5`
- `s` contains only lowercase English letters.

## Examples

### Example 1

```
Input:  s = "level"
Output: "l"
Explanation: The prefixes of "level" (excluding the whole word) are
"l", "le", "lev", "leve"; the suffixes are "l", "el", "vel", "evel". The largest
string that is both a prefix and a suffix is "l".
```

### Example 2

```
Input:  s = "ababab"
Output: "abab"
Explanation: "abab" is the largest prefix which is also a suffix. The suffix
starting at index 2 ("abab") equals the prefix "abab", and its length is
6 - 2 = 4.
```

### Example 3

```
Input:  s = "abcdef"
Output: ""
Explanation: No proper prefix equals a suffix, so the answer is the empty string.
```

## Hint

Compute the **Z-array** of `s`. A suffix starting at `i` equals a prefix iff
`z[i] == n - i`; scan `i` upward and take the first hit for the longest border.
