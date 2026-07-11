# Count Distinct Necklaces

**Difficulty:** Medium

**Source:** Classic combinatorics-on-strings problem (necklace canonicalization; appears
in many competitive-programming judges as "count distinct necklaces / circular strings").

## Description

A **necklace** is a string considered up to **rotation**: two strings represent the same
necklace if one is a rotation of the other. For example `"abc"`, `"bca"`, and `"cab"` are
all the *same* necklace, because you can rotate one into another.

You are given a list of strings `words`. Count how many **distinct necklaces** it
contains — that is, group the strings so that any two strings that are rotations of each
other fall in the same group, and return the number of groups.

Two strings of **different lengths** can never be rotations of each other, so they are
always distinct necklaces.

## Constraints

- `1 <= len(words) <= 10^5`
- `1 <= len(words[i]) <= 10^5`
- The total number of characters across all words is at most `10^6`.
- Characters come from a fixed, totally ordered alphabet (e.g. lowercase letters).

## Examples

### Example 1

```
Input:  words = ["abc", "bca", "cab", "xyz"]
Output: 2
Explanation: "abc", "bca", "cab" are all rotations of each other -> 1 necklace.
             "xyz" -> another necklace. Total = 2.
```

### Example 2

```
Input:  words = ["abab", "baba", "ab", "ba", "abc"]
Output: 3
Explanation: {"abab","baba"} share canonical rotation "abab";
             {"ab","ba"} share canonical rotation "ab";
             {"abc"} is on its own.
             Distinct necklaces = 3.
```

### Example 3

```
Input:  words = ["aa", "aaa", "aaaa"]
Output: 3
Explanation: All three are made only of 'a', but they have different lengths, so no two
             can be rotations of each other. Distinct necklaces = 3.
```

## Hint

Map each string to a **canonical representative**: its lexicographically smallest
rotation. Two strings are the same necklace iff their canonical forms are identical.
Compute each canonical form with **Booth's Algorithm** in `O(len)` and count the number
of distinct canonical strings (e.g. with a hash set).
