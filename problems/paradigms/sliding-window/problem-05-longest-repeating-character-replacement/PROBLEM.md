# Longest Repeating Character Replacement

**Difficulty:** Medium

**Source:** LeetCode 424 — Longest Repeating Character Replacement

## Description

You are given a string `s` and an integer `k`. You may choose **any** character of the
string and change it to any other uppercase English character. You can perform this
operation **at most `k` times**.

Return the length of the **longest substring** containing the same letter you can
obtain after performing the above operations.

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of only uppercase English letters.
- `0 <= k <= s.length`

## Examples

### Example 1

```
Input:  s = "ABAB", k = 2
Output: 4
Explanation: Change the two 'A's to 'B' (or vice versa) to get "BBBB". The whole
             string of length 4 becomes uniform.
```

### Example 2

```
Input:  s = "AABABBA", k = 1
Output: 4
Explanation: Change the single 'A' at index 3 to 'B' to form "AABBBBA" — the window
             "BBBB" (indices 2..5) has length 4. No length-5 window is fixable with
             just 1 replacement.
```

### Example 3

```
Input:  s = "AAAA", k = 0
Output: 4
Explanation: The string is already all the same letter, so with zero replacements the
             whole length-4 string qualifies.
```

## Hint

Use the **Sliding Window** technique: a window is valid when
`(window length) - (count of its most frequent character) <= k`, i.e. the number of
characters you would need to replace does not exceed `k`. Grow the window and slide it
forward when this condition breaks.
