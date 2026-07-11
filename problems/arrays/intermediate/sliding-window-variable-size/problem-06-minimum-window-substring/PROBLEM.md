# Minimum Window Substring

**Difficulty:** Hard

**Source:** LeetCode 76 — Minimum Window Substring

## Description

Given two strings `s` and `t`, return the **shortest substring** of `s` that
contains **every character of `t`, including duplicates** (i.e. `t` as a
multiset). If no such window exists, return the empty string `""`.

For example, if `t = "AABC"`, a valid window must contain at least two `A`s, one
`B`, and one `C`. The window may contain any extra characters — it just has to
*cover* the multiset of `t`.

The answer is guaranteed to be **unique** if it exists.

## Constraints

- `m == s.length`, `n == t.length`
- `1 <= m, n <= 10^5`
- `s` and `t` consist of uppercase and lowercase English letters.

## Examples

### Example 1

```
Input:  s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The window "BANC" (indices 9..12) contains A, B, and C. It is the
             shortest such window; e.g. "ADOBEC" also covers ABC but is longer.
```

### Example 2

```
Input:  s = "a", t = "a"
Output: "a"
Explanation: The whole string "a" is the smallest window covering t = "a".
```

### Example 3

```
Input:  s = "a", t = "aa"
Output: ""
Explanation: t needs two 'a's, but s has only one, so no window can cover t.
```

## Hint

Use a **Sliding Window (variable size)**. Expand `right` until the window covers
all required character counts, then shrink `left` as far as possible while it
still covers `t`, recording the smallest covering window seen.
