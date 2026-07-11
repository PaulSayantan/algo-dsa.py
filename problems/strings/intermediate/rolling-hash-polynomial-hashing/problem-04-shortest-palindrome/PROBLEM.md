# Shortest Palindrome

**Difficulty:** Hard

**Source:** LeetCode 214 — "Shortest Palindrome". Solvable with KMP, but has an
elegant **forward-vs-reverse rolling hash** solution.

## Description

You are given a string `s`. You may convert `s` into a palindrome by adding
characters **in front of it**. Return the **shortest** palindrome you can obtain
this way.

The key observation is that the answer is determined by the **longest prefix of
`s` that is itself a palindrome**. If `s[0..k-1]` is the longest palindromic
prefix, then the leftover suffix `s[k..n-1]` must be mirrored: prepend
`reverse(s[k..n-1])` to the front of `s`. Adding fewer characters than that could
not make the whole string a palindrome.

To find the longest palindromic prefix quickly, maintain a **forward** rolling
hash of `s[0..i]` and a **reverse** rolling hash of the same characters read
right-to-left. A prefix is a palindrome exactly when these two hashes match, so
you can find the longest palindromic prefix in a single `O(n)` scan.

## Constraints

- `0 <= len(s) <= 5 * 10^4`
- `s` consists of lowercase English letters.

## Examples

### Example 1

```
Input:  s = "aacecaaa"
Output: "aaacecaaa"
Explanation: The longest palindromic prefix is "aacecaa" (length 7). The leftover
             suffix is "a"; prepend its reverse ("a") to get "aaacecaaa", which
             is a palindrome and is the shortest achievable.
```

### Example 2

```
Input:  s = "abcd"
Output: "dcbabcd"
Explanation: The longest palindromic prefix is "a" (length 1). The leftover
             suffix is "bcd"; prepend its reverse ("dcb") to get "dcbabcd".
```

### Example 3

```
Input:  s = "aba"
Output: "aba"
Explanation: "aba" is already a palindrome, so nothing is added.
```

## Hint

Scan `s` left to right while maintaining a **forward** polynomial hash of the
prefix and a **reverse** polynomial hash of the same characters. The prefix
`s[0..i]` is a palindrome exactly when the two hashes are equal; take the longest
such prefix. This is **Rolling Hash / Polynomial Hashing**.
