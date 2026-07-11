# Edit Distance

**Difficulty:** Medium (frequently ranked Hard)

**Source:** LeetCode 72 — Edit Distance (classic Levenshtein distance / CLRS)

## Description

Given two strings `word1` and `word2`, return the **minimum number of operations** required
to convert `word1` into `word2`.

You may perform the following three operations on `word1`, each counting as one step:

- **Insert** a character.
- **Delete** a character.
- **Replace** a character.

The result is the classic **Levenshtein edit distance** between the two strings.

## Constraints

- `0 <= word1.length, word2.length <= 500`
- `word1` and `word2` consist of lowercase English letters.

## Examples

**Example 1**

```
Input:  word1 = "horse", word2 = "ros"
Output: 3
Explanation: horse -> rorse (replace 'h' with 'r')
             rorse -> rose  (delete 'r')
             rose  -> ros   (delete 'e')
             Three operations, and no shorter sequence exists.
```

**Example 2**

```
Input:  word1 = "intention", word2 = "execution"
Output: 5
Explanation: intention -> inention (delete 't')
             inention  -> enention (replace 'i' with 'e')
             enention  -> exention (replace 'n' with 'x')
             exention  -> exection (replace 'n' with 'c')
             exection  -> execution (insert 'u')
             Five operations, which is optimal.
```

**Example 3**

```
Input:  word1 = "", word2 = "abc"
Output: 3
Explanation: Insert 'a', 'b', and 'c'. Turning an empty string into a length-3 string needs
             at least 3 insertions.
```

## Hint

This is the textbook problem the **Wagner–Fischer (Edit Distance DP)** algorithm was
designed for. Build the `(n+1) x (m+1)` table where a match copies the diagonal and a
mismatch takes `1 + min` of the delete, insert, and replace neighbours.
