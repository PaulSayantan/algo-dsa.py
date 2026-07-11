# Longest Happy Prefix

**Difficulty:** Hard

**Source:** LeetCode 1392 — "Longest Happy Prefix"

## Description

A string is called a **happy prefix** if it is a **non-empty prefix** which is
also a **suffix** — but excluding the whole string itself (a *proper* prefix).

Given a string `s`, return the longest happy prefix of `s`. If no such prefix
exists, return the empty string `""`.

This is precisely the "longest proper prefix that is also a suffix" — the value
the KMP failure function is built to produce.

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.

## Examples

### Example 1

```
Input:  s = "level"
Output: "l"
Explanation: The proper prefixes are "l", "le", "lev", "leve".
             The only one that is also a suffix is "l"
             (the string ends in "l"). So the answer is "l".
```

### Example 2

```
Input:  s = "ababab"
Output: "abab"
Explanation: "abab" is a prefix and also a suffix of "ababab"
             (positions 2..5 are "abab"). It is the longest such proper prefix.
```

### Example 3

```
Input:  s = "leetcodeleet"
Output: "leet"
Explanation: "leet" is both the leading 4 characters and the trailing 4
             characters. No longer proper prefix is also a suffix.
```

## Hint

The answer's length is exactly `lps[n-1]`, the last entry of the **LPS array**.
Build it with **KMP (Knuth–Morris–Pratt)** and slice off that many leading
characters.
