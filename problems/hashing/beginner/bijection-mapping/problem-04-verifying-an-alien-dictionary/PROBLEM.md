# Verifying an Alien Dictionary

**Difficulty:** Easy

**Source:** LeetCode 953 — Verifying an Alien Dictionary

## Description

In an alien language the lowercase letters are ordered by the string `order` (a permutation of the 26 letters). Given a list of `words`, return whether the words are sorted **lexicographically** according to this alien order.

## Examples

### Example 1

```
Input:  words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
```

### Example 2

```
Input:  words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
```

## Hint

Map each letter to its rank in `order`, then verify every adjacent pair is non-decreasing under those ranks.
