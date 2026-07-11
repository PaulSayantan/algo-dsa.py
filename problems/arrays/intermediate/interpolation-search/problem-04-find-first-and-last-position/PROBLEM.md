# Find First and Last Position of Element in Sorted Array

**Difficulty:** Medium

Source: LeetCode 34 — "Find First and Last Position of Element in Sorted Array"

## Description

Given an array of integers `nums` sorted in **non-decreasing** order, find the starting and ending
index of a given `target` value. Return `[first, last]`. If `target` is not found, return
`[-1, -1]`.

The reference problem requires O(log n) time. When the keys are numeric and roughly uniform, you
can use two **Interpolation Search** passes — one biased toward the left boundary, one toward the
right — to locate the two ends of the block of equal values.

## Constraints

- `0 <= len(nums) <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `nums` is sorted in non-decreasing order (duplicates allowed).
- `-10^9 <= target <= 10^9`

## Examples

### Example 1
```
Input:  nums = [5, 7, 7, 8, 8, 10], target = 8
Output: [3, 4]
Explanation: 8 first appears at index 3 and last appears at index 4.
```

### Example 2
```
Input:  nums = [5, 7, 7, 8, 8, 10], target = 6
Output: [-1, -1]
Explanation: 6 is not in the array.
```

### Example 3
```
Input:  nums = [], target = 0
Output: [-1, -1]
Explanation: The array is empty, so the target cannot be found.
```

## Hint

Do two **Interpolation Search** passes: after an exact hit, keep searching to the left to find the
first occurrence, and to the right to find the last. Remember the interpolation formula needs a
guard when `nums[lo] == nums[hi]` (which happens with runs of duplicates).
