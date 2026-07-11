# Minimum Window Substring

**Difficulty:** Hard

**Source:** LeetCode 76 — Minimum Window Substring

## Description

Given two strings `s` and `t`, return the **minimum window substring** of `s` such
that every character in `t` (including duplicates) is included in the window. If there
is no such substring, return the empty string `""`.

The characters of `t` may appear in any order within the window, and the window must
contain each character of `t` **at least as many times** as it occurs in `t`. It is
guaranteed that the answer is unique.

## Constraints

- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 10^5`
- `s` and `t` consist of uppercase and lowercase English letters.

## Examples

### Example 1

```
Input:  s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The substring "BANC" (indices 9..12) contains 'A', 'B', and 'C'. It is
             the shortest window of s that covers all of t.
```

### Example 2

```
Input:  s = "a", t = "a"
Output: "a"
Explanation: The entire string is the only and smallest window covering t.
```

### Example 3

```
Input:  s = "a", t = "aa"
Output: ""
Explanation: t needs two 'a's but s has only one, so no valid window exists and the
             answer is the empty string.
```

## Hint

Use the **Sliding Window** technique: expand the right edge until the window covers
all required characters of `t`, then contract the left edge as far as possible while
the window still covers `t`, tracking the smallest valid window seen. Frequency counts
plus a "how many requirements are satisfied" counter let you test coverage in O(1).
