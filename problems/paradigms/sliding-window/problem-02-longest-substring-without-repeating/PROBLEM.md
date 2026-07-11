# Longest Substring Without Repeating Characters

**Difficulty:** Medium

**Source:** LeetCode 3 — Longest Substring Without Repeating Characters

## Description

Given a string `s`, find the length of the **longest substring** that contains no
repeating characters.

A substring is a **contiguous** sequence of characters within the string. You return
only the length, not the substring itself.

## Constraints

- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols, and spaces.

## Examples

### Example 1

```
Input:  s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with length 3. Once a second 'a' appears the window
             must shrink, so no valid window is longer than 3.
```

### Example 2

```
Input:  s = "bbbbb"
Output: 1
Explanation: The best substring is "b", with length 1 — every extension repeats 'b'.
```

### Example 3

```
Input:  s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with length 3. Note that "pwke" is a subsequence,
             not a substring, so it does not count.
```

### Example 4

```
Input:  s = ""
Output: 0
Explanation: The empty string has no characters, so the longest valid length is 0.
```

## Hint

Use the **Sliding Window** technique: expand the window to the right and, whenever a
character repeats inside the window, move the left edge just past its previous
occurrence so the window always holds distinct characters.
