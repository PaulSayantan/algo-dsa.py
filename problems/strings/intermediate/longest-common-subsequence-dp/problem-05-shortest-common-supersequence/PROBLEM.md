# Shortest Common Supersequence

**Difficulty:** Hard

**Source:** LeetCode 1092 — Shortest Common Supersequence

## Description

Given two strings `str1` and `str2`, return the **shortest string** that has
both `str1` and `str2` as **subsequences**. If there are multiple valid answers,
return any of them.

A string `s` is a subsequence of string `t` if deleting some number of
characters from `t` (possibly zero) results in `s`.

## Constraints

- `1 <= str1.length, str2.length <= 1000`
- `str1` and `str2` consist of lowercase English letters.

## Examples

### Example 1

```
Input:  str1 = "abac", str2 = "cab"
Output: "cabac"
```

Explanation: `str1 = "abac"` is a subsequence of `"cabac"` (delete the leading
`c`: c**abac** -> `abac`). `str2 = "cab"` is a subsequence of `"cabac"`
(**cab**ac -> `cab`). The result has length 5, and no shorter common
supersequence exists. `"acbac"` and `"cabac"` are both valid length-5 answers.

### Example 2

```
Input:  str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"
```

Explanation: The two strings are identical, so the shortest common
supersequence is the string itself, length 8.

## Hint

Merge the two strings but write the **shared** characters (the Longest Common
Subsequence) only once. First compute the LCS table with **Longest Common
Subsequence (DP)**, then walk the table backwards to interleave the unique
characters of each string around the common ones.
