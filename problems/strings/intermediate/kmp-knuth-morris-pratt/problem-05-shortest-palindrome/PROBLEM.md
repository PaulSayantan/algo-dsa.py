# Shortest Palindrome

**Difficulty:** Hard

**Source:** LeetCode 214 — "Shortest Palindrome"

## Description

You are given a string `s`. You may convert it to a palindrome by adding
characters **in front of it** (only at the beginning). Return the **shortest**
palindrome you can form this way.

The trick is to find the **longest prefix of `s` that is already a palindrome**.
Whatever comes after that prefix must be mirrored and prepended. Minimizing the
number of prepended characters is equivalent to maximizing that palindromic
prefix.

## Constraints

- `0 <= s.length <= 5 * 10^4`
- `s` consists of lowercase English letters.

## Examples

### Example 1

```
Input:  s = "aacecaaa"
Output: "aaacecaaa"
Explanation: The longest palindromic prefix is "aacecaa". The remaining
             suffix is "a"; mirror it and prepend to get "aaacecaaa".
```

### Example 2

```
Input:  s = "abcd"
Output: "dcbabcd"
Explanation: The longest palindromic prefix is just "a". Mirror the remaining
             "bcd" -> "dcb" and prepend it, giving "dcbabcd".
```

### Example 3

```
Input:  s = "aba"
Output: "aba"
Explanation: "aba" is already a palindrome, so nothing needs to be prepended.
```

## Hint

Form the combined string `s + '#' + reverse(s)` and compute its **LPS array**.
The last LPS value is the length of the longest palindromic prefix of `s`. This
is the classic **KMP (Knuth–Morris–Pratt)** application to palindromes; the `#`
separator prevents the overlap from exceeding `len(s)`.
