# Shortest Palindrome

**Difficulty:** Hard

**Source:** LeetCode 214 — Shortest Palindrome

## Description

You are given a string `s`. You may convert it into a palindrome by adding
characters **in front of it**. Return the **shortest** palindrome you can form by
performing this transformation.

The crux of the problem is finding the **longest palindromic prefix** of `s`. Once
you know it, the characters *after* that prefix must be reversed and prepended.
Manacher's Algorithm finds, in O(n), the longest palindrome centered at every
position; among those, the longest one that starts at index 0 is exactly the
longest palindromic prefix.

## Constraints

- `0 <= s.length <= 5 * 10^4`
- `s` consists of lowercase English letters only.

## Examples

### Example 1
```
Input:  s = "aacecaaa"
Output: "aaacecaaa"
Explanation: The longest palindromic prefix is "aacecaa" (length 7). Only the last
character "a" lies outside it, so we prepend "a": "a" + "aacecaaa" = "aaacecaaa".
```

### Example 2
```
Input:  s = "abcd"
Output: "dcbabcd"
Explanation: The longest palindromic prefix is "a" (length 1). We reverse the
remaining "bcd" -> "dcb" and prepend it: "dcb" + "abcd" = "dcbabcd".
```

### Example 3
```
Input:  s = "aba"
Output: "aba"
Explanation: The entire string is already a palindrome, so nothing is added.
```

## Hint

Prepending is fixed by the **longest palindromic prefix**. Use **Manacher's
Algorithm** to find, in linear time, the longest palindrome that begins at index 0,
then reverse and prepend the leftover suffix.
