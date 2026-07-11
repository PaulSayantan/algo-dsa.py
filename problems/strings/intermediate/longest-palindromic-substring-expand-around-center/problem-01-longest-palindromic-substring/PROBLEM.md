# Longest Palindromic Substring

**Difficulty:** Medium

**Source:** LeetCode 5 — Longest Palindromic Substring

## Description

Given a string `s`, return *the longest palindromic substring* in `s`.

A **substring** is a contiguous, non-empty sequence of characters within a
string. A string is a **palindrome** when it reads the same forwards and
backwards (for example, `"racecar"` and `"noon"`).

If several palindromic substrings share the maximum length, you may return any
one of them.

## Constraints

- `1 <= s.length <= 1000`
- `s` consists of only digits and English letters.

## Examples

**Example 1**

```
Input:  s = "babad"
Output: "bab"
Explanation: "bab" is a palindrome of length 3. "aba" is also a valid answer
             of the same length — either is accepted.
```

**Example 2**

```
Input:  s = "cbbd"
Output: "bb"
Explanation: The longest palindromic substring is "bb" (length 2). Single
             characters are palindromes too, but "bb" is longer.
```

**Example 3**

```
Input:  s = "a"
Output: "a"
Explanation: A single character is always a palindrome, so it is the answer.
```

## Hint

Every palindrome grows symmetrically from a center. Use the **Longest
Palindromic Substring (expand around center)** technique: try each of the
`2n - 1` possible centers (both single-character and between-character centers)
and expand outward while the mirrored characters match, tracking the longest
palindrome you find.
