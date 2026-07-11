# Longest Common Subsequence — Length in Linear Space

**Difficulty:** Easy

**Source:** Classic (LeetCode 1143 "Longest Common Subsequence", solved under a space constraint)

## Description

Given two strings `text1` and `text2`, return the length of their **longest common
subsequence** (LCS). A subsequence is a sequence derived from another string by deleting
zero or more characters without changing the relative order of the remaining characters.
A common subsequence of two strings is a subsequence common to both. If there is no
common subsequence, return `0`.

The twist that makes this the natural warm-up for Hirschberg's algorithm: you must use
only **`O(min(len(text1), len(text2)))` extra space**, not the usual `O(n·m)` DP table.

This is exactly the *score pass* that Hirschberg's divide-and-conquer is built on top of:
if you can compute the LCS length with a single rolling row, you have the primitive the
full algorithm calls repeatedly.

## Constraints

- `1 <= text1.length, text2.length <= 1000`
- `text1` and `text2` consist of lowercase English characters.
- Extra space (beyond the inputs) must be `O(min(len(text1), len(text2)))`.

## Examples

### Example 1
```
Input:  text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace", which has length 3.
```

### Example 2
```
Input:  text1 = "abc", text2 = "abc"
Output: 3
Explanation: The whole string "abc" is common to both, so the LCS length is 3.
```

### Example 3
```
Input:  text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no common character, so the LCS is empty with length 0.
```

## Hint

You never need the full 2-D table just to get the *length*. Keep only two rows (or one
rolling row) of the DP, iterating so the shorter string indexes the row — this is the
linear-space score routine at the heart of **Hirschberg's Algorithm**.
