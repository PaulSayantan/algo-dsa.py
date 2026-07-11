# Exponential Search in a Sorted Array

**Difficulty:** Easy

**Source:** Classic algorithm (GeeksforGeeks "Exponential Search"; the search
routine behind `std::equal_range`-style lookups and Timsort's merge)

## Description

You are given an array `nums` sorted in **ascending order** and a value
`target`. Return the index of `target` in `nums`, or `-1` if it is not present.
If `target` occurs more than once, returning the index of any occurrence is
acceptable.

Although the array size is known here, you must implement the search using the
**exponential (galloping) search** strategy rather than a single full-range
binary search:

1. Probe indices `1, 2, 4, 8, ...`, doubling each time, until the probed value
   is greater than or equal to `target` (or the probe passes the end of the
   array).
2. Binary-search the range bounded by the last two probes.

This is the canonical warm-up for the technique: get the doubling loop and the
handoff to binary search exactly right on a bounded array before moving on to
the unbounded variants.

## Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i], target <= 10^9`
- `nums` is sorted in non-decreasing order.

## Examples

**Example 1**

```
Input:  nums = [2, 3, 4, 10, 40], target = 10
Output: 3
Explanation: Probe index 1 (value 3 < 10), then 2 (value 4 < 10), then 4
(value 40 >= 10) — target must lie in [2, 4]. Binary search that window and find
10 at index 3.
```

**Example 2**

```
Input:  nums = [2, 3, 4, 10, 40], target = 5
Output: -1
Explanation: Doubling stops at index 4 (value 40 >= 5). Binary search over
[2, 4] never finds 5, so the answer is -1.
```

**Example 3**

```
Input:  nums = [1], target = 1
Output: 0
Explanation: nums[0] == target, so the answer is index 0 before the doubling
loop even begins.
```

## Hint

Use Exponential (Galloping) Search: double a `bound` index until
`nums[bound] >= target` or `bound` exceeds the array, then run a plain binary
search on `[bound // 2, min(bound, n - 1)]`.
