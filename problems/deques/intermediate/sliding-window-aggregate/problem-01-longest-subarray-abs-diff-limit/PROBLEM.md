# Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

**Difficulty:** Medium

**Source:** LeetCode 1438 — Longest Continuous Subarray With Absolute Diff <= Limit

## Description

Given an integer array `nums` and an integer `limit`, return the size of the **longest** non-empty contiguous subarray such that the absolute difference between any two elements of it is `<= limit` (equivalently, `max - min <= limit`).

## Examples

### Example 1

```
Input:  nums = [8,2,4,7], limit = 4
Output: 2
```

**Explanation:** [2,4] has max-min = 2 <= 4.

### Example 2

```
Input:  nums = [10,1,2,4,7,2], limit = 5
Output: 4
```

**Explanation:** [2,4,7,2] has max-min = 5.

## Hint

Two deques (window max & min). Grow right; while max - min > limit, advance left and evict stale fronts.
