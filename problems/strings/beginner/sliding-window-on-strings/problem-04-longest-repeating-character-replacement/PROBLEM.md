# Longest Repeating Character Replacement

**Difficulty:** Medium

**Source:** LeetCode 424 — Longest Repeating Character Replacement

## Description

You are given a string `s` and an integer `k`. You may choose **at most `k`**
characters in `s` and replace each with any uppercase English letter.

Return the length of the **longest substring** that can be made to consist of a
single repeated character after performing at most `k` such replacements.

The key observation: within any window, the cheapest way to make it uniform is
to keep the most frequent character and replace the rest. A window of length
`L` can be made uniform with at most `k` replacements exactly when
`L - (count of the most frequent character in the window) <= k`.

## Constraints

- `1 <= len(s) <= 10^5`
- `s` consists of uppercase English letters.
- `0 <= k <= len(s)`

## Examples

### Example 1
```
Input:  s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with 'B' (or the two 'B's with 'A') to get
             "BBBB". The whole string of length 4 becomes uniform using 2
             replacements.
```

### Example 2
```
Input:  s = "AABABBA", k = 1
Output: 4
Explanation: The window "BABB" (indices 2..5) has three 'B's and one 'A';
             replacing that single 'A' yields "BBBB", length 4. No length-5
             window can be made uniform with a single replacement, because
             every 5-character window has at least two characters that differ
             from its most frequent letter.
```

### Example 3
```
Input:  s = "AAAA", k = 0
Output: 4
Explanation: The string is already a single repeated character, so with 0
             replacements the entire length-4 string qualifies.
```

## Hint

Use the **Sliding Window on Strings** technique. Track the frequency of the
most common character in the current window; the window is valid while
`window_length - max_frequency <= k`. Grow on the right, and when the window
becomes invalid, slide the left edge forward.
