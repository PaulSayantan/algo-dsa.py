# Minimum Number of Removals to Make Mountain Array

**Difficulty:** Hard

**Source:** LeetCode 1671 — Minimum Number of Removals to Make Mountain Array

## Description

You are given an integer array `nums`. An array `arr` is a **mountain array**
if and only if:

- `arr.length >= 3`, and
- there exists some index `i` with `0 < i < arr.length - 1` such that
  - `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]` (strictly increasing up to
    the peak), and
  - `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]` (strictly decreasing
    after the peak).

Return the **minimum number of elements to remove** from `nums` so that the
remaining array is a mountain array. It is guaranteed that a valid answer
always exists (i.e., you can always reach a mountain array).

## Constraints

- `3 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^9`

## Examples

### Example 1

```
Input:  nums = [1, 3, 1]
Output: 0
Explanation: The array is already a mountain (peak at index 1: 1 < 3 > 1),
             so nothing needs to be removed.
```

### Example 2

```
Input:  nums = [2, 1, 1, 5, 6, 2, 3, 1]
Output: 3
Explanation: Remove the elements at indices 0, 1, and 5 (values 2, 1, 2),
             leaving [1, 5, 6, 3, 1], which is a mountain with peak 6.
             You cannot make a mountain by removing fewer than 3 elements.
```

### Example 3

```
Input:  nums = [1, 2, 1, 2, 1]
Output: 2
Explanation: One option is to remove indices 2 and 3 (or 1 and 3),
             leaving a length-3 mountain such as [1, 2, 1].
```

## Hint

For each index, compute the longest strictly increasing subsequence ending
there and the longest strictly decreasing subsequence starting there — both
via the Longest Increasing Subsequence (patience / binary search) technique.
The best peak keeps `LIS_left + LDS_right - 1` elements; remove the rest.
