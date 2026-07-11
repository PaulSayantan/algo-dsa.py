# Palindrome Partitioning

**Difficulty:** Medium

**Source:** LeetCode 131 — "Palindrome Partitioning"

## Description

Given a string `s`, partition `s` such that **every substring of the partition
is a palindrome**. Return *all possible palindrome partitionings of `s`*. You
may return the answer in any order.

A *partition* is a way of cutting the string into contiguous, non-empty pieces
whose concatenation is the original string. A string is a *palindrome* if it
reads the same forwards and backwards.

## Constraints

- `1 <= s.length <= 16`
- `s` contains only lowercase English letters.

## Examples

### Example 1

```
Input:  s = "aab"
Output: [["a","a","b"], ["aa","b"]]
Explanation: Two ways to cut "aab" into all-palindrome pieces:
  - "a" | "a" | "b"  (each single char is a palindrome)
  - "aa" | "b"       ("aa" is a palindrome, "b" is a palindrome)
The cut "aab" as one piece is invalid because "aab" is not a palindrome.
```

### Example 2

```
Input:  s = "aba"
Output: [["a","b","a"], ["aba"]]
Explanation: "a" | "b" | "a" uses three single-char palindromes, and "aba" is
itself a palindrome, so the whole string uncut is also a valid partition.
The cut "ab" | "a" is invalid because "ab" is not a palindrome.
```

## Hint

Use **Backtracking**: scan a cut point forward from the current start; for each
prefix that is a palindrome, add it to the current partition and recurse on the
remaining suffix, then remove it (undo) to try a longer prefix.
