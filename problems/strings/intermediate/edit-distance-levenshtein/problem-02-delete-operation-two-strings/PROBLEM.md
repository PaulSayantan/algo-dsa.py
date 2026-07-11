# Delete Operation for Two Strings

**Difficulty:** Medium

**Source:** LeetCode 583 — Delete Operation for Two Strings

## Description

Given two strings `word1` and `word2`, return the **minimum number of steps**
required to make `word1` and `word2` the same.

In one step you may delete **exactly one character** in either string. This is a
restricted form of edit distance in which *insert* and *replace* are not
allowed — only deletions.

## Constraints

- `1 <= word1.length, word2.length <= 500`
- `word1` and `word2` consist of only lowercase English letters.

## Examples

### Example 1

```
Input:  word1 = "sea", word2 = "eat"
Output: 2
Explanation: Delete 's' from "sea" to get "ea", and delete 't' from "eat" to
get "ea". After 2 deletions both strings equal "ea".
```

### Example 2

```
Input:  word1 = "leetcode", word2 = "etco"
Output: 4
Explanation: The longest common subsequence is "etco" (length 4). We delete the
4 extra characters of "leetcode" ('l', 'e', 'd', 'e') and 0 from "etco",
for a total of 8 - 4 = 4 deletions.
```

### Example 3

```
Input:  word1 = "abc", word2 = "abc"
Output: 0
Explanation: The strings are already equal, so no deletions are needed.
```

## Hint

This is **Edit Distance (Levenshtein)** with only the delete operation allowed.
Equivalently, characters that survive form the **longest common subsequence**;
everything outside the LCS must be deleted from one string or the other.
