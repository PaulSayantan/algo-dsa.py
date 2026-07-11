# Longest Common Substring of Two Strings

**Difficulty:** Hard

Source: Classic (CLRS / competitive programming; GeeksforGeeks "Longest Common Substring using Generalized Suffix Tree")

## Description

Given two strings `s1` and `s2`, find the **longest string that occurs as a
contiguous substring of both**. This is the *substring* problem, not the
*subsequence* problem — the characters must be consecutive in each string.

Return the longest common substring itself. If the two strings share no
character, return the empty string `""`. If several common substrings share the
maximum length, returning any one of them is acceptable.

## Constraints

- `1 <= len(s1), len(s2) <= 5 * 10^4`
- `s1` and `s2` consist of English letters (the examples use both cases; any
  fixed alphabet works as long as it excludes the two terminal sentinels).
- A substring is a contiguous, non-empty slice.

## Examples

### Example 1
```
Input:  s1 = "xabxa", s2 = "babxba"
Output: "abx"
Explanation: "abx" occurs in "xabxa" (indices 1..3) and in "babxba"
  (indices 1..3). No length-4 string is common to both, so "abx" is a
  longest common substring.
```

### Example 2
```
Input:  s1 = "GeeksforGeeks", s2 = "GeeksQuiz"
Output: "Geeks"
Explanation: "Geeks" is common to both strings and has length 5; no longer
  common substring exists.
```

### Example 3
```
Input:  s1 = "abcde", s2 = "fghij"
Output: ""
Explanation: The two strings share no character, so the longest common
  substring is empty.
```

## Hint

Build a **generalized suffix tree** with **Ukkonen's algorithm** over the
concatenation `s1 + '#' + s2 + '$'`, where `#` and `$` are two distinct
terminals used nowhere else. Mark each leaf by which original string its suffix
came from. The answer is the deepest **internal node whose subtree contains
leaves from both strings** — its path label (trimmed at any separator) is the
longest common substring.
