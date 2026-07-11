# Longest Palindromic Subsequence

**Difficulty:** Medium

**Source:** LeetCode 516 — Longest Palindromic Subsequence

## Description

Given a string `s`, find the length of the **longest palindromic subsequence**
in `s`.

A **subsequence** is a sequence that can be derived from another sequence by
deleting some or no elements without changing the order of the remaining
elements. A string is a **palindrome** if it reads the same forwards and
backwards.

Return the length (an integer) of the longest subsequence of `s` that is a
palindrome.

## Constraints

- `1 <= s.length <= 1000`
- `s` consists only of lowercase English letters.

## Examples

### Example 1
```
Input:  s = "bbbab"
Output: 4
Explanation: One longest palindromic subsequence is "bbbb" (delete the 'a').
```

### Example 2
```
Input:  s = "cbbd"
Output: 2
Explanation: One longest palindromic subsequence is "bb".
```

### Example 3
```
Input:  s = "agbdba"
Output: 5
Explanation: The subsequence "abdba" (keep indices 0,2,3,4,5) is a palindrome
of length 5. No longer palindromic subsequence exists.
```

## Hint

Think **Range / Interval DP**: let `dp[i][j]` be the answer for the substring
`s[i..j]`, and relate it to the shorter intervals obtained by comparing the two
endpoints `s[i]` and `s[j]`.
