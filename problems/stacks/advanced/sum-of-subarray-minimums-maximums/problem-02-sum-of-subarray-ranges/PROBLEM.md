# Sum of Subarray Ranges

**Difficulty:** Medium

**Source:** LeetCode 2104 — Sum of Subarray Ranges

## Description

Given an integer array `nums`, the *range* of a subarray is the difference between its largest and smallest element. Return the sum of all subarray ranges of `nums`.

## Examples

### Example 1

```
Input:  nums = [1,2,3]
Output: 4
```

## Hint

Sum of maxes minus sum of mins, each via monotonic-stack contribution counting.
