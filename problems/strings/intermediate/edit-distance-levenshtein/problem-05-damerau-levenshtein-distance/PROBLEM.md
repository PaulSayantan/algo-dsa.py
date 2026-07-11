# Damerau-Levenshtein Distance

**Difficulty:** Hard

**Source:** Classic string-metric problem (Damerau 1964; common in spell-check
and fuzzy-matching systems). This is the "Optimal String Alignment" variant.

## Description

Given two strings `a` and `b`, return the minimum number of operations to
transform `a` into `b`, where the allowed operations are the three Levenshtein
edits **plus** a fourth:

- **Insert** a character
- **Delete** a character
- **Replace** a character
- **Transpose** two *adjacent* characters (swap `xy` into `yx`), counting as one
  operation

Transpositions model a very common human/typing error (typing `teh` for `the`),
which plain Levenshtein charges as 2 replaces. Damerau-Levenshtein charges it as
1.

Implement the **Optimal String Alignment (OSA)** version: no substring is edited
more than once (each pair of positions may participate in at most one
transposition). This is the form used in most interviews and spell-checkers.

## Constraints

- `0 <= a.length, b.length <= 1000`
- `a` and `b` consist of printable ASCII characters.

## Examples

### Example 1

```
Input:  a = "ca", b = "ac"
Output: 1
Explanation: A single adjacent transposition swaps 'c' and 'a' to turn "ca" into
"ac". Plain Levenshtein would report 2 (two replacements).
```

### Example 2

```
Input:  a = "teh", b = "the"
Output: 1
Explanation: Transpose the adjacent 'e' and 'h' to fix the typo "teh" -> "the".
```

### Example 3

```
Input:  a = "sitting", b = "kitten"
Output: 3
Explanation: No adjacent transposition helps here, so the answer matches the
plain Levenshtein distance. Aligning "sitting" with "kitten": replace 's'->'k',
keep "itt", replace 'i'->'e', keep 'n', and delete the final 'g' — 3 operations.
```

### Example 4

```
Input:  a = "abc", b = "abc"
Output: 0
Explanation: The strings are identical; no operations are needed.
```

## Hint

Start from the **Edit Distance (Levenshtein)** DP and add one more transition:
when the last two characters of the current prefixes are a swapped pair
(`a[i-1] == b[j-2]` and `a[i-2] == b[j-1]`), allow `dp[i-2][j-2] + 1`. Everything
else is the familiar insert/delete/replace recurrence.
