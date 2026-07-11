# Squares of a Sorted Array

**Difficulty:** Easy

**Source:** LeetCode 977 — Squares of a Sorted Array

## Description

Given an integer array `nums` sorted in **non-decreasing** order, return an
array of **the squares of each number** sorted in non-decreasing order.

The straightforward approach — square every element and then sort — runs in
`O(n log n)`. The follow-up challenge is to do it in `O(n)` time.

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in **non-decreasing** order.

## Examples

### Example 1
- **Input:** `nums = [-4, -1, 0, 3, 10]`
- **Output:** `[0, 1, 9, 16, 100]`
- **Explanation:** Squaring gives `[16, 1, 0, 9, 100]`; sorted in non-decreasing
  order that is `[0, 1, 9, 16, 100]`.

### Example 2
- **Input:** `nums = [-7, -3, 2, 3, 11]`
- **Output:** `[4, 9, 9, 49, 121]`
- **Explanation:** Squaring gives `[49, 9, 4, 9, 121]`; sorted that is
  `[4, 9, 9, 49, 121]`.

### Example 3
- **Input:** `nums = [-5, -3, -2]`
- **Output:** `[4, 9, 25]`
- **Explanation:** All values are negative, so the largest magnitude (`-5`) is
  at the left end. Squaring gives `[25, 9, 4]`; sorted that is `[4, 9, 25]`.

## Hint

Use **Two Pointers (opposite ends)**: the largest square must come from one of
the two ends, since the biggest magnitudes of a sorted array live at its
extremes. Compare the ends and fill the output from the back forward.
