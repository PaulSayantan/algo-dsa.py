# Palindrome Partitioning II

**Difficulty:** Hard

**Source:** LeetCode 132 — Palindrome Partitioning II

## Description

Given a string `s`, partition `s` such that **every substring of the partition is
a palindrome**.

Return the **minimum number of cuts** needed for such a palindrome
partitioning of `s`. A "cut" is placed between two adjacent characters; a string
split into `p` palindromic pieces uses `p - 1` cuts.

## Constraints

- `1 <= s.length <= 2000`
- `s` consists of lowercase English letters only.

## Examples

### Example 1
```
Input:  s = "aab"
Output: 1
Explanation: The string can be split as ["aa", "b"], both palindromes, using
1 cut. No zero-cut partition works because "aab" is not itself a palindrome.
```

### Example 2
```
Input:  s = "a"
Output: 0
Explanation: "a" is already a palindrome, so no cuts are needed.
```

### Example 3
```
Input:  s = "aabaa"
Output: 0
Explanation: "aabaa" reads the same forwards and backwards, so it is already a
single palindromic piece and needs 0 cuts.
```

### Example 4
```
Input:  s = "abccbc"
Output: 2
Explanation: One optimal split is ["a", "bccb", "c"] -> palindromes "a",
"bccb", "c" using 2 cuts. No partition into fewer than 3 palindromic pieces
exists, so the minimum number of cuts is 2.
```

## Hint

Think **Range / Interval DP**: precompute a boolean table `isPal[i][j]` (whether
`s[i..j]` is a palindrome) with an interval recurrence, then run a linear
min-cut DP on top of it.
