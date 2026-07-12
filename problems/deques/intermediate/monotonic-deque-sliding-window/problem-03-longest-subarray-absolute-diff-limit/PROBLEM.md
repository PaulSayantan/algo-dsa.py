# Longest Continuous Subarray With Absolute Diff <= Limit

**Difficulty:** Medium

**Source:** LeetCode 1438 — Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

## Description

Given an integer array `nums` and an integer `limit`, return the length of the **longest** contiguous subarray such that the absolute difference between **any two** elements of that subarray is `<= limit`. Equivalently, within the chosen window `max(window) - min(window) <= limit`.

Constraints: `1 <= len(nums)`, `0 <= limit`.

## Examples

### Example 1

```
Input:  nums = [8,2,4,7], limit = 4
Output: 2
```

**Explanation:** `[8,2]` has diff 6, `[2,4]` has diff 2, `[4,7]` has diff 3; the longest valid subarray is length 2 (e.g. `[2,4]`).

### Example 2

```
Input:  nums = [10,1,2,4,7,2], limit = 5
Output: 4
```

**Explanation:** `[2,4,7,2]` has `max - min = 7 - 2 = 5 <= 5`.

## Hint

Slide a window and maintain TWO monotonic deques of indices — a decreasing one for the window max and an increasing one for the window min; shrink from the left while `max - min > limit`.
