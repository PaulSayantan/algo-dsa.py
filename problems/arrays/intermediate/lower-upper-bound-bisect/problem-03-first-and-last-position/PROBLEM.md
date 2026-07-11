# Find First and Last Position of Element in Sorted Array

**Difficulty:** Medium

**Source:** LeetCode 34 — Find First and Last Position of Element in Sorted Array

## Description

Given an array of integers `nums` sorted in **non-decreasing** order, find the starting and ending
position of a given `target` value.

Return `[first_index, last_index]`. If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

## Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `nums` is sorted in non-decreasing order.
- `-10^9 <= target <= 10^9`

## Examples

### Example 1
```
Input:  nums = [5, 7, 7, 8, 8, 10], target = 8
Output: [3, 4]
Explanation: The value 8 occupies indices 3 and 4, so the first and last
             positions are 3 and 4.
```

### Example 2
```
Input:  nums = [5, 7, 7, 8, 8, 10], target = 6
Output: [-1, -1]
Explanation: 6 does not appear in the array at all.
```

### Example 3
```
Input:  nums = [], target = 0
Output: [-1, -1]
Explanation: The array is empty, so the target cannot be present.
```

## Hint

The run of equal values `[first, last]` is bracketed by two boundaries. The **first** occurrence is
the **lower bound** of `target`; the position just past the **last** occurrence is the **upper
bound** of `target`. Use two **Lower/Upper Bound (bisect)** searches.
