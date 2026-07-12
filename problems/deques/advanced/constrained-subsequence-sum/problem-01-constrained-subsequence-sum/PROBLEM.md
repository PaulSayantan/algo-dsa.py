# Constrained Subsequence Sum

**Difficulty:** Hard

**Source:** LeetCode 1425 — Constrained Subsequence Sum

## Description

Given an integer array `nums` and integer `k`, return the maximum sum of a non-empty subsequence such that for every two consecutive chosen elements at indices `i < j`, `j - i <= k` holds.

## Examples

### Example 1

```
Input:  nums = [10,2,-10,5,20], k = 2
Output: 37
```

## Hint

dp[i] = nums[i] + max(0, window-max of dp over [i-k, i-1]); keep the window max with a monotonic deque.
