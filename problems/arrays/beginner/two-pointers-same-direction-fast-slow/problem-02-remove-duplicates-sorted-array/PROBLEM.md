# Remove Duplicates from Sorted Array

**Difficulty:** Easy

**Source:** LeetCode 26 (Remove Duplicates from Sorted Array)

## Description

Given an integer array `nums` sorted in **non-decreasing order**, remove the
duplicates **in place** so that each unique element appears only **once**. The
relative order of the elements should be kept the **same**.

Since it is impossible to change the length of the array in some languages, you
must instead have the result placed in the **first part** of the array `nums`.
More formally, if there are `k` unique elements, then the first `k` elements of
`nums` should hold the final result in their original order. The elements beyond
the first `k` positions do not matter.

Return `k`, the number of unique elements.

You must do this using only O(1) extra space.

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in non-decreasing order.

## Examples

### Example 1

```
Input:  nums = [1, 1, 2]
Output: 2, nums = [1, 2, _]
```

**Explanation:** Your function should return `k = 2`, with the first two elements
of `nums` being `1` and `2`. There are two unique values.

### Example 2

```
Input:  nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
```

**Explanation:** Your function should return `k = 5`, with the first five
elements of `nums` being `0, 1, 2, 3, 4`. The distinct values are
`{0, 1, 2, 3, 4}`.

### Example 3

```
Input:  nums = [7]
Output: 1, nums = [7]
```

**Explanation:** A single element is already unique, so `k = 1`.

## Hint

Use **Two Pointers (same direction / fast-slow)**. Because the array is sorted,
equal values are adjacent — a *writer* pointer only needs to compare a candidate
against the last element it kept to decide whether it is a new unique value.
