# Palindromic Substrings

**Difficulty:** Medium

**Source:** LeetCode 647 — Palindromic Substrings

## Description

Given a string `s`, return the **number** of palindromic substrings in it.

A substring is a contiguous sequence of characters within the string. Two
substrings are counted as different if they start or end at different indices,
even when the substrings themselves are identical in content.

## Constraints

- `1 <= len(s) <= 1000`
- `s` consists of lowercase English letters.

## Examples

### Example 1
```
Input:  s = "abc"
Output: 3
Explanation: The palindromic substrings are "a", "b", and "c" — three
             single characters. No longer substring is a palindrome.
```

### Example 2
```
Input:  s = "aaa"
Output: 6
Explanation: The palindromic substrings are "a", "a", "a" (three singles),
             "aa", "aa" (two adjacent pairs), and "aaa" — 3 + 2 + 1 = 6.
             Note the two "aa" occurrences count separately by position.
```

### Example 3
```
Input:  s = "aba"
Output: 4
Explanation: "a", "b", "a" (three singles) plus "aba" itself = 4. The
             substring "ab" and "ba" are not palindromes.
```

## Hint

Use the **Palindrome Check (two pointers)** technique in its *expand around
center* form: from each of the `2n - 1` centers, push two pointers outward,
and every time the characters still match you have discovered one more
palindromic substring — add one to the count for each successful expansion.
