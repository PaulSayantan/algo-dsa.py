# Find All Numbers Disappeared in an Array

**Difficulty:** Easy

**Source:** LeetCode 448 — Find All Numbers Disappeared in an Array

## Description

Given an array `nums` of `n` integers where each value is in `[1, n]`, return a list of all the integers in `[1, n]` that do **not** appear in `nums`, in ascending order.

## Examples

### Example 1

```
Input:  nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
```

## Hint

Put the values in a set, then scan 1..n and collect every value the set is missing.
