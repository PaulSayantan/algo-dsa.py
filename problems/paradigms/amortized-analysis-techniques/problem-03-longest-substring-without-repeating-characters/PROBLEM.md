# Longest Substring Without Repeating Characters

**Difficulty:** Medium

**Source:** LeetCode 3 — Longest Substring Without Repeating Characters

## Description

Given a string `s`, find the length of the **longest substring** that contains no
repeating characters.

A **substring** is a contiguous, non-empty sequence of characters within the string.

## Constraints

- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols, and spaces.

## Examples

### Example 1

```
Input:  s = "abcabcbb"
Output: 3
```

Explanation: The answer is `"abc"`, with length 3. (After index 2 the window must shrink
because `a`, then `b`, then `c` repeat.)

### Example 2

```
Input:  s = "bbbbb"
Output: 1
```

Explanation: The longest substring without repeating characters is `"b"`, with length 1.

### Example 3

```
Input:  s = "pwwkew"
Output: 3
```

Explanation: The answer is `"wke"`, with length 3. Note that `"pwke"` is a *subsequence*
but not a *substring*, so it does not count.

### Example 4

```
Input:  s = ""
Output: 0
```

Explanation: The empty string has no characters, so the longest valid substring has
length 0.

## Hint

Use **Amortized Analysis Techniques** via a **sliding window**. Keep a window
`[left, right]` with all-distinct characters and a map of last-seen positions. As `right`
advances, only move `left` forward (never backward) when a duplicate appears. Because
`left` and `right` each traverse the string once and never retreat, the total work is
O(n) even though a single step of `right` might advance `left` several positions.
