# Longest Substring Without Repeating Characters

**Difficulty:** Medium

**Source:** LeetCode 3 — Longest Substring Without Repeating Characters

## Description

Given a string `s`, find the length of the longest substring that contains no repeating characters.

## Examples

### Example 1

```
Input:  s = "abcabcbb"
Output: 3
```

**Explanation:** The answer is "abc".

### Example 2

```
Input:  s = "pwwkew"
Output: 3
```

**Explanation:** The answer is "wke".

## Hint

Store each char's last-seen index; when it lies inside the window, move start to last-seen + 1.
