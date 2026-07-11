# Edit Distance

**Difficulty:** Medium

**Source:** LeetCode 72 — Edit Distance (a.k.a. Levenshtein distance, CLRS 15)

## Description

Given two strings `word1` and `word2`, return the **minimum number of
operations** required to convert `word1` into `word2`.

You have the following three operations permitted on a word:

- **Insert** a character
- **Delete** a character
- **Replace** a character

This is the classic Levenshtein-distance problem. Like Longest Common
Subsequence it is solved with a 2D table over prefixes, but the transition set
is richer: each cell chooses the cheapest of insert, delete, or replace, which
introduces the "combine three neighbors" pattern that regex/wildcard matching
later specializes.

## Constraints

- `0 <= word1.length, word2.length <= 500`
- `word1` and `word2` consist of lowercase English letters.

## Examples

### Example 1

```
Input:  word1 = "horse", word2 = "ros"
Output: 3
Explanation:
  horse -> rorse   (replace 'h' with 'r')
  rorse -> rose    (delete 'r')
  rose  -> ros     (delete 'e')
```

### Example 2

```
Input:  word1 = "intention", word2 = "execution"
Output: 5
Explanation:
  intention -> inention  (delete 't')
  inention  -> enention  (replace 'i' with 'e')
  enention  -> exention  (replace 'n' with 'x')
  exention  -> exection  (replace 'n' with 'c')
  exection  -> execution (insert 'u')
```

### Example 3

```
Input:  word1 = "", word2 = "abc"
Output: 3
Explanation: Insert 'a', 'b', and 'c' — three insertions.
```

## Hint

Use **String DP (regex/wildcard matching)**: let `dp[i][j]` be the edit distance
between the first `i` characters of `word1` and the first `j` of `word2`. When
the current characters match, the cost is inherited from the diagonal;
otherwise it is `1 +` the minimum of the three neighboring subproblems.
