# Edit Distance

**Difficulty:** Hard

**Source:** LeetCode 72 (Edit Distance); Levenshtein distance (classic)

## Description

Given two strings `word1` and `word2`, return the **minimum number of operations**
required to convert `word1` to `word2`.

You have the following three operations permitted on a word:

- **Insert** a character
- **Delete** a character
- **Replace** a character

Each operation counts as one step. This minimum is known as the *Levenshtein distance*
between the two strings.

## Constraints

- `0 <= word1.length, word2.length <= 500`
- `word1` and `word2` consist of lowercase English letters.

## Examples

### Example 1

```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
  horse -> rorse   (replace 'h' with 'r')
  rorse -> rose    (delete 'r')
  rose  -> ros     (delete 'e')
Three operations, and no shorter sequence exists.
```

### Example 2

```
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
  intention -> inention  (delete 't')
  inention  -> enention  (replace 'i' with 'e')
  enention  -> exention  (replace 'n' with 'x')
  exention  -> exection  (replace 'n' with 'c')
  exection  -> execution (insert 'u')
Five operations in total.
```

### Example 3

```
Input: word1 = "", word2 = "abc"
Output: 3
Explanation: Insert 'a', 'b', and 'c' — three insertions turn "" into "abc".
```

## Hint

Use **Dynamic Programming (memoization / tabulation)**: compare prefixes. If the current
characters match, no operation is needed; otherwise take 1 + the best of insert, delete,
or replace on the shorter prefixes. Cache each `(i, j)` prefix pair.
