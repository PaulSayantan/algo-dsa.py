# Delete Operation for Two Strings

**Difficulty:** Medium

**Source:** LeetCode 583 — Delete Operation for Two Strings

## Description

Given two strings `word1` and `word2`, return the **minimum number of steps**
required to make `word1` and `word2` the same.

In one step, you can delete exactly one character in either string.

## Constraints

- `1 <= word1.length, word2.length <= 500`
- `word1` and `word2` consist of only lowercase English letters.

## Examples

### Example 1

```
Input:  word1 = "sea", word2 = "eat"
Output: 2
```

Explanation: Delete `"s"` from `"sea"` to get `"ea"`, and delete `"t"` from
`"eat"` to get `"ea"`. Both strings become `"ea"` after 2 deletions.

### Example 2

```
Input:  word1 = "leetcode", word2 = "etco"
Output: 4
```

Explanation: The longest common subsequence is `"etco"` (length 4). We delete
the 4 non-matching characters of `"leetcode"` (`l`, `e`, `d`, `e`) and 0 from
`"etco"`, for 4 deletions total.

### Example 3

```
Input:  word1 = "abc", word2 = "abc"
Output: 0
```

Explanation: The strings are already equal, so no deletions are needed.

## Hint

The characters you keep must be a subsequence common to both words. Everything
else is deleted, so deletions = `len(word1) + len(word2) - 2 * LCS`. Compute the
LCS with **Longest Common Subsequence (DP)**.
