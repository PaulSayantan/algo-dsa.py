# Longest Repeating Character Replacement

**Difficulty:** Medium

**Source:** LeetCode 424 — Longest Repeating Character Replacement

## Description

Given a string `s` of uppercase letters and an integer `k`, you may change at most `k` characters to any other uppercase letter. Return the length of the longest substring that can be made to consist of a single repeated letter after those changes. A window is valid when its length minus the count of its most frequent letter is at most `k`.

## Examples

### Example 1

```
Input:  s = "ABAB", k = 2
Output: 4
```

**Explanation:** Replace the two A's with B's (or vice versa) to get 4 in a row.

### Example 2

```
Input:  s = "AABABBA", k = 1
Output: 4
```

**Explanation:** Replace one char to make "AABA"->"AAAA" or "BABB"->"BBBB", length 4.

## Hint

Track max_freq inside the window; while (window_len - max_freq) > k, shrink from the left.
