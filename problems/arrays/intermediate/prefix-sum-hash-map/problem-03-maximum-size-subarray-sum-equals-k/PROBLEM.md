# Maximum Size Subarray Sum Equals k

**Difficulty:** Medium

**Source:** LeetCode 325 — Maximum Size Subarray Sum Equals k

## Description

Given an integer array `nums` and an integer `k`, return the **maximum length**
of a contiguous subarray whose elements sum to exactly `k`. If there is no such
subarray, return `0`.

Unlike LeetCode 560 (which *counts* subarrays), here you must find the
**longest** one. The array may contain negative numbers and zeros, so you
cannot rely on a monotonic sliding window.

## Constraints

- `1 <= nums.length <= 2 * 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `-10^9 <= k <= 10^9`

## Examples

### Example 1

```
Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] (indices 0..3) sums to 3 and has
length 4. It is the longest such subarray; [3] (index 4) also sums to 3 but
is shorter.
```

### Example 2

```
Input: nums = [-2, -1, 2, 1], k = 1
Output: 2
Explanation: The subarray [-1, 2] (indices 1..2) sums to 1 with length 2.
No longer subarray sums to 1.
```

### Example 3

```
Input: nums = [1, 0, -1], k = 0
Output: 3
Explanation: The whole array [1, 0, -1] sums to 0, giving length 3.
```

## Hint

Use a running **prefix sum**. Store the *earliest* index at which each
prefix-sum value occurred in a **hash map**; when you later reach a prefix sum
of `current - k`, the span between the two indices is a candidate longest
subarray.
