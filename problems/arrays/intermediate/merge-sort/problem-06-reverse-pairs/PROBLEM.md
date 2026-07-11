# Reverse Pairs

**Difficulty:** Hard

**Source:** LeetCode 493 — Reverse Pairs

## Description

Given an integer array `nums`, return the number of **reverse pairs** in the
array.

A **reverse pair** is a pair `(i, j)` where:

- `0 <= i < j < nums.length`, and
- `nums[i] > 2 * nums[j]`.

This is a stricter cousin of the inversion-count problem: the comparison is
`nums[i] > 2 * nums[j]` rather than `nums[i] > nums[j]`. Because the condition
being counted (`> 2 * x`) differs from the ordering used to sort, the counting and
the merging must be done in **two separate passes** within each merge.

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`
- Note that `2 * nums[j]` can overflow 32-bit integers; use 64-bit arithmetic in
  languages where that matters (Python integers are unbounded).

## Examples

### Example 1

```
Input:  nums = [1, 3, 2, 3, 1]
Output: 2
```

**Explanation:** The reverse pairs are:
- `(1, 4)` -> `nums[1] = 3 > 2 * nums[4] = 2 * 1 = 2`.
- `(3, 4)` -> `nums[3] = 3 > 2 * nums[4] = 2 * 1 = 2`.

### Example 2

```
Input:  nums = [2, 4, 3, 5, 1]
Output: 3
```

**Explanation:** The reverse pairs are:
- `(1, 4)` -> `nums[1] = 4 > 2 * nums[4] = 2 * 1 = 2`.
- `(2, 4)` -> `nums[2] = 3 > 2 * nums[4] = 2 * 1 = 2`.
- `(3, 4)` -> `nums[3] = 5 > 2 * nums[4] = 2 * 1 = 2`.

### Example 3

```
Input:  nums = [1, 2, 3, 4, 5]
Output: 0
```

**Explanation:** The array is ascending and all values are positive, so no
`nums[i]` exceeds twice a later element; there are no reverse pairs.

## Hint

Use **Merge Sort**. Before merging two sorted halves, run a separate two-pointer
pass to count pairs where a left-half element exceeds twice a right-half element;
then merge normally. Counting and merging use different comparisons, so keep them
as two passes.
