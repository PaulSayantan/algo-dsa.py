# Wiggle Sort II

**Difficulty:** Hard

**Source:** LeetCode 324 — Wiggle Sort II

## Description

Given an integer array `nums`, reorder it **in place** so that it satisfies the "wiggle"
property:

```
nums[0] < nums[1] > nums[2] < nums[3] > nums[4] < ...
```

That is, every even-indexed element is **strictly less** than its neighbors, and every
odd-indexed element is **strictly greater** than its neighbors. You may assume the input
always has at least one valid answer.

Note the **strict** inequalities: unlike the simpler "Wiggle Sort I," equal adjacent
values are **not** allowed. This is what makes the problem hard when the array contains
many duplicates clustered around the median.

**Follow-up:** Can you do it in `O(n)` time and/or in place with `O(1)` extra space?

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `0 <= nums[i] <= 5000`
- It is guaranteed that there will be an answer for the given input array.

## Examples

### Example 1

```
Input:  nums = [1, 5, 1, 1, 6, 4]
Output: [1, 6, 1, 5, 1, 4]
```

**Explanation:** Check the wiggle pattern on the output: `1 < 6 > 1 < 5 > 1 < 4`. All
inequalities hold strictly. (Other valid answers exist, e.g. `[2, 3, 1, 3, 1, 2]` for a
different input — any arrangement satisfying the strict pattern is accepted.)

### Example 2

```
Input:  nums = [1, 3, 2, 2, 3, 1]
Output: [2, 3, 1, 3, 1, 2]
```

**Explanation:** Verify: `2 < 3 > 1 < 3 > 1 < 2`. All strict inequalities hold. Note the
two `2`s and two `3`s (values near the median) are separated so that no equal values land
next to each other.

## Hint

Find the **median** with **Quickselect** in expected `O(n)`. Then place numbers greater
than the median on the odd indices and numbers less than the median on the even indices,
so that the two copies of the median (and other duplicates) are pushed as far apart as
possible. An index-rewiring / three-way partition around the median avoids adjacent equal
values.
