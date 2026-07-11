# Palindrome Partitioning IV

**Difficulty:** Hard

**Source:** LeetCode 1745 — Palindrome Partitioning IV

## Description

Given a string `s`, return `true` if it is possible to split the string into
**three non-empty palindromic substrings**. Otherwise, return `false`.

Concretely, you must decide whether there exist indices `i` and `j` with
`0 < i <= j < n - 1` such that `s[0:i]`, `s[i:j+1]`, and `s[j+1:n]` are all
palindromes.

The naive approach tests each split with O(n) palindrome checks, costing O(n^3).
Manacher's Algorithm preprocesses the string in O(n) so that any "is `s[l..r]` a
palindrome?" query is answered in O(1); the split search then costs O(n^2).

## Constraints

- `3 <= s.length <= 2000`
- `s` consists only of lowercase English letters.

## Examples

### Example 1
```
Input:  s = "abcbdd"
Output: true
Explanation: "abcbdd" = "a" + "bcb" + "dd". All three parts are palindromes, so
the answer is true.
```

### Example 2
```
Input:  s = "bcbddxy"
Output: false
Explanation: No way to split "bcbddxy" into three palindromic substrings exists.
```

### Example 3
```
Input:  s = "aaa"
Output: true
Explanation: Split into "a" + "a" + "a"; each single character is a palindrome.
```

## Hint

Precompute palindrome radii once with **Manacher's Algorithm** so each
`is s[l..r] a palindrome?` check is O(1), then scan the two cut positions.
