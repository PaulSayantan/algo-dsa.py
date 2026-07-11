# Minimum Number of Steps to Make Two Strings Anagram

**Difficulty:** Medium

Source: LeetCode 1347 — Minimum Number of Steps to Make Two Strings Anagram

## Description

You are given two strings `s` and `t` of the **same length**. In one step you may
replace any single character of `t` with any other lowercase English letter.

Return the **minimum** number of steps needed to make `t` an anagram of `s`.

An anagram of a string is a string that contains the same characters with the same
frequencies. Because `s` and `t` already have equal length, you only ever need to
change characters of `t` (never insert or delete).

## Constraints

- `1 <= s.length <= 5 * 10^4`
- `s.length == t.length`
- `s` and `t` consist of lowercase English letters.

## Examples

### Example 1

```
Input:  s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with 'b' -> t = "bba", which is an anagram of
s = "bab". One replacement suffices.
```

### Example 2

```
Input:  s = "leetcode", t = "practice"
Output: 5
Explanation: Replacing 5 characters of t (the extra p, r, a, i, and one c) with
l, e, e, d, o turns "practice" into an anagram of "leetcode".
```

### Example 3

```
Input:  s = "anagram", t = "mangaar"
Output: 0
Explanation: t is already an anagram of s (both have a×3, n, g, r, m), so no steps
are needed.
```

## Hint

Use an **Anagram Check (sort or count)** idea: build frequency tables and measure how
much `t` is *deficient* relative to `s`. The number of characters `t` lacks equals the
number of replacements required.
