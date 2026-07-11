# Longest Palindromic Substring

**Difficulty:** Medium

**Source:** LeetCode 5 — Longest Palindromic Substring

## Description

Given a string `s`, return the **longest palindromic substring** in `s`.

A substring is a contiguous sequence of characters. A palindrome reads the same
forwards and backwards. If several substrings share the maximum length, returning
any one of them is acceptable.

The classic dynamic-programming and "expand around center" solutions both run in
O(n^2) time. For large inputs we want a linear solution: with Manacher's
Algorithm we can compute, in O(n), the radius of the longest palindrome centered
at every position and read the global maximum directly.

## Constraints

- `1 <= s.length <= 1000` (aim for a solution that also scales to `10^5+`)
- `s` consists of digits and English letters.

## Examples

### Example 1
```
Input:  s = "babad"
Output: "bab"
Explanation: "bab" is a palindrome of length 3. "aba" is also a valid answer of
the same length; either is accepted.
```

### Example 2
```
Input:  s = "cbbd"
Output: "bb"
Explanation: The only palindrome longer than a single character is the even-length
"bb", so it is the longest.
```

### Example 3
```
Input:  s = "a"
Output: "a"
Explanation: A single character is itself a palindrome of length 1.
```

## Hint

Insert separators between characters so even and odd palindromes are handled the
same way, then use **Manacher's Algorithm** to find the longest palindrome radius
in one linear pass.
