# Unique Number of Occurrences

**Difficulty:** Easy

**Source:** LeetCode 1207 — Unique Number of Occurrences

## Description

Given an integer array `arr`, return `true` if the number of occurrences of each value in the array is **unique** — that is, no two distinct values occur the same number of times — otherwise return `false`.

## Examples

### Example 1

```
Input:  arr = [1,2,2,1,1,3]
Output: true
```

**Explanation:** Counts are 3, 2, 1 — all distinct.

### Example 2

```
Input:  arr = [1,2]
Output: false
```

**Explanation:** Both values occur once.

## Hint

Count each value, then check whether the multiset of counts has any duplicates (len == len of set).
