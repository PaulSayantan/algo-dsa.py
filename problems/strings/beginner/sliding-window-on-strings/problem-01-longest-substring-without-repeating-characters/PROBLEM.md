# Longest Substring Without Repeating Characters

**Difficulty:** Medium

**Source:** LeetCode 3 — Longest Substring Without Repeating Characters

## Description

Given a string `s`, find the length of the **longest substring** that contains
no repeating characters.

A **substring** is a contiguous, non-empty run of characters within the string.
"No repeating characters" means every character in the chosen substring is
distinct. Return only the *length* of the best such substring, not the
substring itself.

## Constraints

- `0 <= len(s) <= 5 * 10^4`
- `s` consists of English letters, digits, symbols, and spaces.

## Examples

### Example 1
```
Input:  s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with length 3. The next character 'a'
             would repeat the earlier 'a', so the window cannot grow past
             length 3 without a duplicate.
```

### Example 2
```
Input:  s = "bbbbb"
Output: 1
Explanation: Every character is 'b'. The longest substring without a repeat
             is just "b", of length 1.
```

### Example 3
```
Input:  s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with length 3. Note that "pwke" is a
             subsequence, not a substring, so it does not count; the answer
             must be contiguous.
```

## Hint

Use the **Sliding Window on Strings** technique: expand a window to the right,
and whenever the entering character is already inside the window, shrink from
the left until the duplicate is gone. Track the largest window size seen.
