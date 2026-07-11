# Longest Common Substring of Two Strings

**Difficulty:** Hard

Source: Classic (SPOJ LCS / competitive programming; GeeksforGeeks "Longest Common Substring")

## Description

Given two strings `a` and `b`, find the **longest contiguous substring that
appears in both** of them. Return the substring itself (any one of them if there
are ties). If they share no common substring, return the empty string `""`.

Note: this is the *substring* problem (contiguous), not the *subsequence*
problem.

## Constraints

- `1 <= len(a), len(b) <= 10^5`
- `a` and `b` consist of lowercase English letters.
- You may assume you can pick two separator characters that do not appear in
  either string (for example, `'#'` and `'$'`), or handle separators by index
  bookkeeping.

## Examples

### Example 1
```
Input:  a = "abcde", b = "cdefg"
Output: "cde"
Explanation: "cde" is contained in both "ab[cde]" and "[cde]fg". No length-4
  substring is common, so "cde" (length 3) is the answer.
```

### Example 2
```
Input:  a = "GeeksforGeeks", b = "GeeksQuiz"
Output: "Geeks"
Explanation: "Geeks" appears in both strings. It occurs twice in the first
  string, but as a common substring it is counted once and is the longest such
  match (length 5).
```

### Example 3
```
Input:  a = "abc", b = "xyz"
Output: ""
Explanation: The two strings share no character, so the longest common
  substring has length 0.
```

## Hint

Concatenate the two strings with a unique separator in between (e.g.
`a + '#' + b + '$'`), build the **Suffix Array** and **LCP array (Kasai's
algorithm)**. The answer comes from adjacent sorted suffixes whose starting
positions lie in *different* original strings — take the maximum LCP among those
pairs.
