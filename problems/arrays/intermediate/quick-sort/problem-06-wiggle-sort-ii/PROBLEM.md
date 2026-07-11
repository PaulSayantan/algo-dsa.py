# Wiggle Sort II

**Difficulty:** Hard

**Source:** LeetCode 324 — Wiggle Sort II

## Description

Given an integer array `nums`, reorder it **in place** so that

```
nums[0] < nums[1] > nums[2] < nums[3] > nums[4] < ...
```

That is, every element at an odd index is strictly greater than its neighbors, and
every element at an even index is strictly less than its neighbors.

You may assume the input array always has a valid answer. Note the inequalities are
**strict**, which makes duplicates the crux of the problem: the naive "sort, then
alternate" fails when equal values land next to each other.

The intended approach finds the **median** with **Quickselect** (average O(n)), then
uses a **3-way partition** to split values into those less than, equal to, and greater
than the median, and finally interleaves the two halves so equal values are pushed as
far apart as possible. Both building blocks come straight from Quick Sort.

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `0 <= nums[i] <= 5000`
- It is guaranteed that there will be an answer for the given input `nums`.

## Examples

### Example 1

```
Input:  nums = [1, 5, 1, 1, 6, 4]
Output: [1, 6, 1, 5, 1, 4]
Explanation: Check the pattern: 1 < 6 > 1 < 5 > 1 < 4. Every odd-index element exceeds
both neighbors. (Other valid arrangements exist; any that satisfies the wiggle pattern
is accepted.)
```

### Example 2

```
Input:  nums = [1, 3, 2, 2, 3, 1]
Output: [2, 3, 1, 3, 1, 2]
Explanation: Check the pattern: 2 < 3 > 1 < 3 > 1 < 2. The two 3s (the larger values)
occupy odd positions and are separated by smaller values.
```

### Example 3

```
Input:  nums = [1, 2]
Output: [1, 2]
Explanation: 1 < 2 already satisfies nums[0] < nums[1].
```

## Hint

Find the **median** with **Quickselect**, then apply a **3-way partition** so equal-to-
median values are grouped. Map sorted positions to interleaved index slots (odd indices
first, then even indices) so that duplicate medians are placed far apart and the strict
inequalities hold.
