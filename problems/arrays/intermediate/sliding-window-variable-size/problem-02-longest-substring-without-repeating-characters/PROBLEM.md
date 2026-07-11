# Longest Substring Without Repeating Characters

**Difficulty:** Medium

**Source:** LeetCode 3 — Longest Substring Without Repeating Characters

## Description

Given a string `s`, find the length of the **longest substring** that contains
**no repeating characters**. A substring is a contiguous run of characters within
the string.

For example, in `"abcabcbb"` the substrings `"abc"`, `"bca"`, and `"cab"` all have
length 3 with all-distinct characters, and no longer all-distinct substring
exists, so the answer is 3.

## Constraints

- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols, and spaces.

## Examples

### Example 1

```
Input:  s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with length 3. Extending to "abca" repeats 'a'.
```

### Example 2

```
Input:  s = "bbbbb"
Output: 1
Explanation: The best substring with all-unique characters is "b", length 1.
```

### Example 3

```
Input:  s = "pwwkew"
Output: 3
Explanation: The answer is "wke", length 3. Note "pwke" is a subsequence, not a
             substring, so it does not count.
```

## Hint

Use a **Sliding Window (variable size)**. Keep a window with all-distinct
characters; when a duplicate enters on the right, shrink from the left until the
duplicate is gone, tracking the largest valid window seen.
