# Palindrome Partitioning IV

**Difficulty:** Hard

**Source:** LeetCode 1745 — Palindrome Partitioning IV

## Description

Given a string `s`, return `true` if it is possible to split the string `s` into
**three non-empty palindromic substrings**. Otherwise, return `false`.

Formally, you must decide whether there exist indices `i` and `j` with
`0 < i <= j < len(s) - 1` such that all three pieces

- `s[0 .. i-1]`,
- `s[i .. j]`, and
- `s[j+1 .. len(s)-1]`

are palindromes and each is non-empty.

## Constraints

- `3 <= s.length <= 2000`
- `s` consists only of lowercase English letters.

## Examples

**Example 1**

```
Input:  s = "abcbdd"
Output: true
Explanation: Split into "a", "bcb", "dd" — all three are palindromes.
```

**Example 2**

```
Input:  s = "bcbddxy"
Output: false
Explanation: No way to cut the string into three palindromic pieces, because
             the trailing "xy" can never be part of a palindromic partition here.
```

**Example 3**

```
Input:  s = "aabbaa"
Output: true
Explanation: Split into "aa", "bb", "aa" — three palindromes. (Other valid
             splits such as "a", "abba", "a" also exist.)
```

## Hint

Precompute which substrings `s[i..j]` are palindromes so each membership test is
`O(1)`. Build that table with the **Longest Palindromic Substring (expand around
center)** technique — expand from every center and mark each palindrome window as
you find it — then try every pair of cut points using the table.
