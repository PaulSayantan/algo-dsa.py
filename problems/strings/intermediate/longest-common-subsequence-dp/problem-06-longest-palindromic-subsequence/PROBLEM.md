# Longest Palindromic Subsequence

**Difficulty:** Medium

**Source:** LeetCode 516 — Longest Palindromic Subsequence

## Description

Given a string `s`, return the length of the **longest palindromic
subsequence** of `s`.

A **subsequence** is a sequence that can be derived from another sequence by
deleting some or no elements without changing the order of the remaining
elements. A palindrome reads the same forwards and backwards.

## Constraints

- `1 <= s.length <= 1000`
- `s` consists only of lowercase English letters.

## Examples

### Example 1

```
Input:  s = "bbbab"
Output: 4
```

Explanation: One longest palindromic subsequence is `"bbbb"` (drop the `a`),
which has length 4.

### Example 2

```
Input:  s = "cbbd"
Output: 2
```

Explanation: One longest palindromic subsequence is `"bb"`, which has length 2.

### Example 3

```
Input:  s = "agbdba"
Output: 5
```

Explanation: The subsequence `"abdba"` (or `"abgba"`) is a palindrome of
length 5; you cannot keep all 6 characters and stay a palindrome.

## Hint

A subsequence that reads the same forwards and backwards is a subsequence common
to `s` and its reverse. Reverse the string and run **Longest Common Subsequence
(DP)** between `s` and `reversed(s)`.
