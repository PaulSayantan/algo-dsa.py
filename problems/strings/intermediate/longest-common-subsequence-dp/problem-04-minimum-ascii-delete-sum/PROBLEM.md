# Minimum ASCII Delete Sum for Two Strings

**Difficulty:** Medium

**Source:** LeetCode 712 — Minimum ASCII Delete Sum for Two Strings

## Description

Given two strings `s1` and `s2`, return the **lowest ASCII sum of deleted
characters** required to make the two strings equal.

In one deletion you remove a single character from either string; the "cost" of
that deletion is the ASCII value of the removed character. You want to make
`s1` and `s2` identical while minimizing the total ASCII cost of everything you
delete.

## Constraints

- `1 <= s1.length, s2.length <= 1000`
- `s1` and `s2` consist of lowercase English letters.

## Examples

### Example 1

```
Input:  s1 = "sea", s2 = "eat"
Output: 231
```

Explanation: Deleting `"s"` from `"sea"` adds the ASCII value of `"s"` (115) to
the sum. Deleting `"t"` from `"eat"` adds 116. Both strings become `"ea"`, for a
total cost of `115 + 116 = 231`, which is the minimum possible.

### Example 2

```
Input:  s1 = "delete", s2 = "leet"
Output: 403
```

Explanation: The best strings to keep is `"let"` (ASCII sum 325). From
`"delete"` we delete `d(100), e(101), e(101)` and from `"leet"` we delete
`e(101)`, giving `100 + 101 + 101 + 101 = 403`. Any other choice costs more.

## Constraints reminder

- ASCII value of `'a'` is 97, `'z'` is 122.

## Hint

This is a *weighted* cousin of Longest Common Subsequence: instead of maximizing
the count of kept characters, maximize the **ASCII sum** of the kept common
subsequence, then delete the rest. Use **Longest Common Subsequence (DP)** with
character weights.
