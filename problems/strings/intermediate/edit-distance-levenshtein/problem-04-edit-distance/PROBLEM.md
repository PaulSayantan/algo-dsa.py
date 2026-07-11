# Edit Distance

**Difficulty:** Medium

**Source:** LeetCode 72 — Edit Distance (classic Levenshtein distance)

## Description

Given two strings `word1` and `word2`, return the **minimum number of
operations** required to convert `word1` into `word2`.

You have the following three operations, each counting as one step and each
usable any number of times:

- **Insert** a character
- **Delete** a character
- **Replace** a character

This is the textbook **Levenshtein distance** between two strings.

## Constraints

- `0 <= word1.length, word2.length <= 500`
- `word1` and `word2` consist of lowercase English letters.

## Examples

### Example 1

```
Input:  word1 = "horse", word2 = "ros"
Output: 3
Explanation: One optimal sequence:
  horse -> rorse   (replace 'h' with 'r')
  rorse -> rose    (delete 'r')
  rose  -> ros     (delete 'e')
Three operations, and no shorter sequence exists.
```

### Example 2

```
Input:  word1 = "intention", word2 = "execution"
Output: 5
Explanation: One optimal sequence:
  intention -> inention  (delete 't')
  inention  -> enention  (replace 'i' with 'e')
  enention  -> exention  (replace 'n' with 'x')
  exention  -> exection  (replace 'n' with 'c')
  exection  -> execution (insert 'u')
Five operations.
```

### Example 3

```
Input:  word1 = "", word2 = "abc"
Output: 3
Explanation: word1 is empty, so we insert all 3 characters of word2.
```

## Hint

This is the canonical **Edit Distance (Levenshtein)** problem. Build a 2-D DP
table where `dp[i][j]` is the edit distance between the first `i` characters of
`word1` and the first `j` characters of `word2`, and relate each cell to its
three neighbors for insert, delete, and replace.
