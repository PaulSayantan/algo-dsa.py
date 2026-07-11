# Kth Largest Element in an Array

**Difficulty:** Medium

**Source:** LeetCode 215 — Kth Largest Element in an Array

## Description

Given an integer array `nums` and an integer `k`, return the `k`-th largest element in
the array.

Note that it is the `k`-th largest element in **sorted order**, not the `k`-th distinct
element. Duplicates are counted individually.

Can you solve it **without fully sorting** the array?

## Constraints

- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Examples

### Example 1

```
Input:  nums = [3, 2, 1, 5, 6, 4], k = 2
Output: 5
```

**Explanation:** Sorted in descending order the array is `[6, 5, 4, 3, 2, 1]`. The 2nd
largest element is 5.

### Example 2

```
Input:  nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
Output: 4
```

**Explanation:** Sorted descending: `[6, 5, 5, 4, 3, 3, 2, 2, 1]`. The 4th element
(counting duplicates) is 4.

### Example 3

```
Input:  nums = [1], k = 1
Output: 1
```

**Explanation:** Only one element, which is trivially the 1st largest.

## Hint

You do not need the whole array sorted — only the `k` largest values. Use **Top-K via
Heap** (a size-`k` min-heap) for an `O(n log k)` solution, or Quickselect for `O(n)`
average time.
