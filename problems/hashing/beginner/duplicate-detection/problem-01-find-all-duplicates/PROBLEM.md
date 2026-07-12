# Find All Duplicates in an Array

**Difficulty:** Medium

**Source:** LeetCode 442 — Find All Duplicates in an Array

## Description

Given an integer array `nums` of length `n` where each value is in `[1, n]` and each appears **once or twice**, return an array of all the values that appear exactly twice. The returned list is sorted in ascending order.

## Examples

### Example 1

```
Input:  nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
```

**Explanation:** 2 and 3 each appear twice.

## Hint

Count occurrences; collect the values whose count is 2 and return them sorted.
