# Subarrays with K Different Integers

**Difficulty:** Hard

**Source:** LeetCode 992 — Subarrays with K Different Integers

## Description

Given an integer array `nums` and an integer `k`, return the number of **good** subarrays — contiguous subarrays that contain exactly `k` distinct integers. Use `exactly(k) = atMost(k) - atMost(k-1)`.

## Examples

### Example 1

```
Input:  nums = [1,2,1,2,3], k = 2
Output: 7
```

**Explanation:** Subarrays with exactly 2 distinct integers: [1,2],[2,1],[1,2],[2,1],[1,2,1],[2,1,2],[1,2,1,2].

### Example 2

```
Input:  nums = [1,2,1,3,4], k = 3
Output: 3
```

## Hint

Two at-most sliding-window counts; subtract to get exactly-k.
