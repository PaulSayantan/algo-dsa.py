# Longest Palindromic Substring

**Difficulty:** Medium

**Source:** LeetCode 5 — Longest Palindromic Substring

## Description

Given a string `s`, return the **longest** substring of `s` that is a
palindrome. A substring is a contiguous run of characters. If several
palindromic substrings share the maximum length, returning any one of them is
acceptable.

## Constraints

- `1 <= len(s) <= 1000`
- `s` consists of digits and English letters.

## Examples

### Example 1
```
Input:  s = "babad"
Output: "bab"
Explanation: "bab" is a palindrome of length 3. "aba" is also a valid
             answer of the same length; either is accepted.
```

### Example 2
```
Input:  s = "cbbd"
Output: "bb"
Explanation: The longest palindromic substring is "bb" (length 2). No
             length-3 substring of "cbbd" is a palindrome.
```

### Example 3
```
Input:  s = "a"
Output: "a"
Explanation: A single character is always a palindrome, and it is the only
             substring, so it is the longest.
```

## Hint

Use the **Palindrome Check (two pointers)** technique in its *expand around
center* form: for each possible center (each character for odd-length
palindromes, and each gap between characters for even-length ones), push two
pointers outward while the characters match, and track the longest span found.
