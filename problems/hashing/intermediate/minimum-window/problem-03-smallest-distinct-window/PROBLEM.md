# Smallest Subarray Covering All Distinct Elements

**Difficulty:** Medium

**Source:** Classic — smallest window containing all distinct elements

## Description

Given an integer array `arr`, return the length of the smallest contiguous subarray that contains **all** of the array's distinct values at least once. If the array is empty, return `0`.

## Examples

### Example 1

```
Input:  arr = [1,2,2,3,1]
Output: 3
```

**Explanation:** The distinct values are {1,2,3}; [2,3,1] covers them in length 3.

## Hint

Let total = len(set(arr)); expand until you have all distinct, then shrink and record the min length.
