# Longest Common Subsequence

**Difficulty:** Medium

**Source:** LeetCode 1143 (Longest Common Subsequence); classic CLRS problem

## Description

Given two strings `text1` and `text2`, return the length of their **longest common
subsequence**. If there is no common subsequence, return `0`.

A **subsequence** of a string is a new string generated from the original string with
some characters (can be none) deleted **without changing the relative order** of the
remaining characters.

- For example, `"ace"` is a subsequence of `"abcde"`.

A **common subsequence** of two strings is a subsequence that is common to both strings.

## Constraints

- `1 <= text1.length, text2.length <= 1000`
- `text1` and `text2` consist of lowercase English characters.

## Examples

### Example 1

```
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
```

### Example 2

```
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
```

### Example 3

```
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no common subsequence, so the answer is 0.
```

## Hint

Use **Dynamic Programming (memoization / tabulation)**: compare prefixes of the two
strings. If the current characters match, extend the LCS of the shorter prefixes by 1;
otherwise take the better of dropping one character from either string. Cache each
`(i, j)` prefix pair.
