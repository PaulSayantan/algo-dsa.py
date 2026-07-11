# Shortest Common Supersequence

**Difficulty:** Hard

**Source:** LeetCode 1092 — Shortest Common Supersequence

## Description

Given two strings `str1` and `str2`, return **the shortest string** that has **both**
`str1` and `str2` as **subsequences**. If more than one shortest answer exists, you may
return **any** of them.

A string `t` is a subsequence of a string `s` if `t` can be formed from `s` by deleting
zero or more characters without changing the order of the remaining characters.

This is the string-building counterpart of edit distance: instead of counting edits, you
merge the two strings along an optimal alignment so that shared characters are written once
and the non-shared characters of each string are woven in.

## Constraints

- `1 <= str1.length, str2.length <= 1000`
- `str1` and `str2` consist of lowercase English letters.

## Examples

**Example 1**

```
Input:  str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: "cabac" contains "abac" as a subsequence (take positions 1,2,3,4) and "cab" as
             a subsequence (take positions 0,1,2). Its length is 5. Since the longest common
             subsequence of the inputs is "ab" (length 2), the shortest supersequence has
             length 4 + 3 - 2 = 5, so no shorter answer exists. Any valid length-5
             supersequence is accepted.
```

**Example 2**

```
Input:  str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"
Explanation: The two strings are identical, so their shortest common supersequence is the
             string itself — length 8, nothing extra to add.
```

## Hint

Run the **Wagner–Fischer (Edit Distance DP)** style table (here the Longest Common
Subsequence table, its close relative), then **walk the table backward** from the
bottom-right corner to reconstruct the merged string. Length of the answer =
`len(str1) + len(str2) − LCS(str1, str2)`.
