# Maximum Size Subarray Sum Equals k

**Difficulty:** Medium

**Source:** LeetCode 325 — Maximum Size Subarray Sum Equals k

## Description

Given an integer array `nums` and an integer `k`, return the maximum length of a contiguous subarray that sums to exactly `k`. If none exists, return 0. The array may contain negatives.

## Examples

### Example 1

```
Input:  nums = [1,-1,5,-2,3], k = 3
Output: 4
```

## Hint

Store earliest index of each prefix sum; best = i - first[cur - k].
