# N-Repeated Element in Size 2N Array

**Difficulty:** Easy

**Source:** LeetCode 961 — N-Repeated Element in Size 2N Array

## Description

You are given an integer array `nums` of length `2n` containing `n + 1` distinct values, exactly one of which is repeated `n` times. Return the element that is repeated `n` times.

## Examples

### Example 1

```
Input:  nums = [2,1,2,5,3,2]
Output: 2
```

## Hint

Scan while adding to a set; the first value you see a second time is the repeated element.
