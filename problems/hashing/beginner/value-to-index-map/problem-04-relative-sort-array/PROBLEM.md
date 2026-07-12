# Relative Sort Array

**Difficulty:** Easy

**Source:** LeetCode 1122 — Relative Sort Array

## Description

Given two arrays `arr1` and `arr2` where the elements of `arr2` are distinct and all appear in `arr1`, sort `arr1` so that its items follow the order in `arr2`. Elements of `arr1` that do not appear in `arr2` are placed at the end in ascending order.

## Examples

### Example 1

```
Input:  arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
```

## Hint

Build a value -> rank (index in arr2) map; sort arr1 by (rank, value), with a large rank for unranked values.
