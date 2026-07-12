# Sliding Window Maximum

**Difficulty:** Hard

**Source:** LeetCode 239 — Sliding Window Maximum

## Description

Given an integer array `nums` and a window size `k`, the window slides from the left to the right of the array one position at a time. Return a list of the **maximum** value in each window of size `k`, in order (there are `len(nums) - k + 1` windows).

## Examples

### Example 1

```
Input:  nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
```

### Example 2

```
Input:  nums = [9,11], k = 2
Output: [11]
```

## Hint

Decreasing monotonic deque of indices: pop smaller-or-equal tails, evict a stale front, read nums[dq[0]].
