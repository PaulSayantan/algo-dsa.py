# Continuous Subarrays

**Difficulty:** Medium

**Source:** LeetCode 2762 — Continuous Subarrays

## Description

Given a 0-indexed integer array `nums`, call a contiguous subarray **continuous** if for every pair of indices `i, j` within it, `abs(nums[i] - nums[j]) <= 2`. Equivalently, within the subarray `max - min <= 2`. Return the **total number** of continuous subarrays.

Constraints: `1 <= len(nums)`.

## Examples

### Example 1

```
Input:  nums = [5,4,2,4]
Output: 8
```

**Explanation:** Size-1 subarrays: 4 of them. Size-2: `[5,4]`, `[4,2]`, `[2,4]` — 3. Size-3: `[4,2,4]` — 1. Total `4 + 3 + 1 = 8`.

### Example 2

```
Input:  nums = [1,2,3]
Output: 6
```

**Explanation:** Every subarray is continuous (`max - min <= 2`), so all `3 + 2 + 1 = 6` of them count.

## Hint

Slide a window with two monotonic deques (window max and window min); shrink from the left while `max - min > 2`, and add `right - left + 1` valid subarrays ending at each `right`.
