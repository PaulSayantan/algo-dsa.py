# Count All Palindromic Substrings

**Difficulty:** Medium

Source: LeetCode 647 — "Palindromic Substrings".

## Description

Given a string `s`, return the **number of palindromic substrings** in it,
counting **every occurrence separately**. Substrings that are equal but start at
different positions are counted multiple times. A substring is a contiguous
block of characters, and it counts if it reads the same forwards and backwards.

For example, `"aaa"` contains the palindromic substrings `"a"`, `"a"`, `"a"`,
`"aa"`, `"aa"`, and `"aaa"` — six in total, even though there are only three
*distinct* palindromes.

Return the total number of palindromic substring occurrences.

## Constraints

- `1 <= len(s) <= 1000` (original LeetCode). The eertree scales to `10^5`+.
- `s` consists of lowercase English letters.

## Examples

### Example 1

```
Input:  s = "abc"
Output: 3
Explanation: The three palindromic substrings are "a", "b", and "c".
```

### Example 2

```
Input:  s = "aaa"
Output: 6
Explanation: The palindromic substrings are "a", "a", "a", "aa", "aa", "aaa".
             Occurrences are counted separately, giving 6.
```

### Example 3

```
Input:  s = "aba"
Output: 4
Explanation: The palindromic substrings are "a", "b", "a" (three single-letter
             occurrences) and "aba", for a total of 4.
```

## Hint

Build a **Palindromic Tree (Eertree)**. Each node holds a running count of how
often it was the longest palindromic suffix; propagating those counts **up the
suffix links** (from longer to shorter palindromes) yields each palindrome's
total number of occurrences. Summing over all nodes gives the answer.
