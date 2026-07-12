# Continuous Subarray Sum

**Difficulty:** Medium

**Source:** LeetCode 523 — Continuous Subarray Sum

## Description

Given an integer array `nums` and an integer `k`, return `True` if `nums` has a contiguous subarray of length **at least 2** whose sum is a multiple of `k`.

## Examples

### Example 1

```
Input:  nums = [23,2,4,6,7], k = 6
Output: true
```

## Hint

Earliest index of each prefix remainder; a repeat at distance >= 2 proves it.
