# Sliding Window Maximum

**Difficulty:** Hard

**Source:** LeetCode 239 — Sliding Window Maximum

## Description

Given an array `nums` and a window size `k`, return the list of maximums of every contiguous window of length `k` as the window slides from left to right.

## Examples

### Example 1

```
Input:  nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
```

## Hint

Maintain a deque of indices with decreasing values; the front is the window max; pop out-of-window indices.
