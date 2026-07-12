# Longest Consecutive Sequence

**Difficulty:** Medium

**Source:** LeetCode 128 — Longest Consecutive Sequence

## Description

Given an unsorted integer array `nums`, return the length of the longest run of consecutive integers present in the array (order in the array does not matter, duplicates count once). The algorithm must run in O(n).

## Examples

### Example 1

```
Input:  nums = [100,4,200,1,3,2]
Output: 4
```

**Explanation:** The longest run is [1,2,3,4].

### Example 2

```
Input:  nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

**Explanation:** The run [0..8] has length 9.

## Hint

Set membership; start a walk only when x-1 is not in the set, so each value is walked once.
