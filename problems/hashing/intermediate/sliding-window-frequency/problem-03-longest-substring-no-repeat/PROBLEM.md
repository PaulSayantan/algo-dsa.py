# Longest Substring Without Repeating Characters

**Difficulty:** Medium

**Source:** LeetCode 3 — Longest Substring Without Repeating Characters

## Description

Given a string `s`, return the length of the longest substring that contains no repeated character. Use a map from character to its most recent index so the left edge can jump directly past any repeat.

## Examples

### Example 1

```
Input:  s = "abcabcbb"
Output: 3
```

**Explanation:** The answer is "abc", of length 3.

### Example 2

```
Input:  s = "pwwkew"
Output: 3
```

**Explanation:** The answer is "wke", of length 3.

## Hint

Track last-seen index per char; when a repeat is inside the window, move left to last+1.
