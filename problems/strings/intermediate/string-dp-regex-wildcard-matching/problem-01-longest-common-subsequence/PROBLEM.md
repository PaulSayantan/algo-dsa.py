# Longest Common Subsequence

**Difficulty:** Medium

**Source:** LeetCode 1143 — Longest Common Subsequence

## Description

Given two strings `text1` and `text2`, return the length of their **longest
common subsequence**. If there is no common subsequence, return `0`.

A **subsequence** of a string is a new string generated from the original
string with some characters (possibly none) deleted **without changing the
relative order** of the remaining characters.

- For example, `"ace"` is a subsequence of `"abcde"`.

A **common subsequence** of two strings is a subsequence that is common to both
strings.

This is the foundational 2D string-DP problem: the table cell `dp[i][j]` stores
the LCS length of the first `i` characters of `text1` and the first `j`
characters of `text2`, and every longer string DP (edit distance, pattern
matching) is a variation on the transitions used here.

## Constraints

- `1 <= text1.length, text2.length <= 1000`
- `text1` and `text2` consist of only lowercase English characters.

## Examples

### Example 1

```
Input:  text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
```

### Example 2

```
Input:  text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
```

### Example 3

```
Input:  text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no common subsequence, so the result is 0.
```

## Hint

Build a 2D table where `dp[i][j]` is the LCS length of the two prefixes. This is
the entry point to **String DP (regex/wildcard matching)**: when the current
characters match, extend the diagonal; otherwise take the best of dropping a
character from either string.
