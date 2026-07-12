# Sliding Window Median

**Difficulty:** Hard

**Source:** LeetCode 480 — Sliding Window Median

## Description

Given an array `nums` and window size `k`, return the median of each contiguous window as a list of floats (for even `k`, the median is the average of the two middle values).

## Examples

### Example 1

```
Input:  nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1,-1,-1,3,5,6]
```

## Hint

Maintain the window as a sorted list via binary search (bisect); median is the middle element(s).
