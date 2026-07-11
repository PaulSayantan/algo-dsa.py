# Longest Palindromic Substring

**Difficulty:** Medium

Source: LeetCode 5 — "Longest Palindromic Substring".

## Description

Given a string `s`, return the **longest substring of `s` that is a palindrome**.
A palindrome reads the same forwards and backwards. If several palindromic
substrings share the maximum length, returning any one of them is acceptable.

While LeetCode 5 is classically solved with expand-around-center or Manacher's
algorithm, it is also a clean application of the **Palindromic Tree (Eertree)**:
every palindromic substring corresponds to exactly one node, and the answer is
simply the node with the greatest length. Building the eertree also sets you up
to answer many follow-up questions about palindromes on the same string.

## Constraints

- `1 <= len(s) <= 1000` (original LeetCode). The eertree approach scales to
  `len(s) <= 10^5` comfortably.
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
Explanation: The longest palindromic substring is "bb" (length 2). Single
             characters like "c" are shorter.
```

### Example 3

```
Input:  s = "forgeeksskeegfor"
Output: "geeksskeeg"
Explanation: "geeksskeeg" (length 10) is the longest palindromic substring;
             no longer palindrome exists in the string.
```

## Hint

Build a **Palindromic Tree (Eertree)** over `s`. Each node is a distinct
palindrome storing its length; the answer is the node with the maximum length.
Track, per node, one ending position (or the index where the node was created)
so you can recover the actual substring.
