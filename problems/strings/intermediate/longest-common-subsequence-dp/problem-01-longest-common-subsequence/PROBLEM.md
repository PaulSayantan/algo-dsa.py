# Longest Common Subsequence

**Difficulty:** Medium

**Source:** LeetCode 1143 — Longest Common Subsequence

## Description

Given two strings `text1` and `text2`, return the length of their **longest
common subsequence**. If there is no common subsequence, return `0`.

A **subsequence** of a string is a new string generated from the original string
with some characters (possibly none) deleted, without changing the relative
order of the remaining characters.

- For example, `"ace"` is a subsequence of `"abcde"`.

A **common subsequence** of two strings is a subsequence that is common to both
strings.

## Constraints

- `1 <= text1.length, text2.length <= 1000`
- `text1` and `text2` consist of only lowercase English characters.

## Examples

### Example 1

```
Input:  text1 = "abcde", text2 = "ace"
Output: 3
```

Explanation: The longest common subsequence is `"ace"`, whose length is 3.

### Example 2

```
Input:  text1 = "abc", text2 = "abc"
Output: 3
```

Explanation: The longest common subsequence is `"abc"`, whose length is 3.

### Example 3

```
Input:  text1 = "abc", text2 = "def"
Output: 0
```

Explanation: There is no common subsequence, so the result is 0.

## Hint

Compare the two strings character by character and build a table of answers for
every pair of prefixes. This is the canonical **Longest Common Subsequence (DP)**
problem: `dp[i][j]` = LCS length of the first `i` characters of `text1` and the
first `j` characters of `text2`.
