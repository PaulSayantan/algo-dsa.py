# Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

**Difficulty:** Medium

**Source:** LeetCode 1438 — Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

## Description

Given an array of integers `nums` and an integer `limit`, return the size of the
**longest non-empty contiguous subarray** such that the absolute difference
between the **maximum** and **minimum** element of that subarray is less than or
equal to `limit`.

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `0 <= limit <= 10^9`

## Examples

### Example 1

```
Input:  nums = [8, 2, 4, 7], limit = 4
Output: 2
```

**Explanation:** All subarrays and their max-min differences:
`[8] -> 0`, `[8,2] -> 6`, `[8,2,4] -> 6`, `[8,2,4,7] -> 6`, `[2] -> 0`,
`[2,4] -> 2`, `[2,4,7] -> 5`, `[4] -> 0`, `[4,7] -> 3`, `[7] -> 0`. The longest
one whose difference is `<= 4` is `[2, 4]` with length `2`.

### Example 2

```
Input:  nums = [10, 1, 2, 4, 7, 2], limit = 5
Output: 4
```

**Explanation:** The subarray `[2, 4, 7, 2]` has max `7` and min `2`, a
difference of `5 <= 5`, and length `4`. No valid subarray is longer.

### Example 3

```
Input:  nums = [4, 2, 2, 2, 4, 4, 2, 2], limit = 0
Output: 3
```

**Explanation:** With `limit = 0` every element in the window must be equal. The
longest run of equal values is `[2, 2, 2]`, length `3`.

## Hint

Slide a variable-size window with two **Monotonic Deques**: one decreasing to
track the window **maximum** and one increasing to track the window **minimum**.
Whenever `max - min > limit`, advance the left edge and expire deque fronts.
