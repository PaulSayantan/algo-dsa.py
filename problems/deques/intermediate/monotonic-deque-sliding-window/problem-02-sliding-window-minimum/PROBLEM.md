# Sliding Window Minimum

**Difficulty:** Medium

**Source:** CSES — Sliding Window Minimum (companion to LC 239)

## Description

Given an integer array `nums` and a window size `k`, return a list of the **minimum** value in each contiguous window of size `k`, in left-to-right order. This is the mirror image of Sliding Window Maximum: keep an increasing monotonic deque so the front is always the window minimum.

## Examples

### Example 1

```
Input:  nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [-1,-3,-3,-3,3,3]
```

## Hint

Increasing monotonic deque of indices: pop greater-or-equal tails, evict a stale front, read nums[dq[0]].
