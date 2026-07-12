# Shortest Subarray with Sum at Least K

**Difficulty:** Hard

**Source:** LeetCode 862 — Shortest Subarray with Sum at Least K

## Description

Given an integer array `nums` (which may contain negatives) and an integer `k`, return the length of the shortest non-empty subarray with sum at least `k`, or `-1` if none exists.

## Examples

### Example 1

```
Input:  nums = [2,-1,2], k = 3
Output: 3
```

## Hint

Over prefix sums P, keep an increasing deque; while P[i]-P[front] >= k record and popleft; pop back to stay increasing.
