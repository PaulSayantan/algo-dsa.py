# Find First and Last Position of Element in Sorted Array

**Difficulty:** Medium

**Source:** LeetCode 34 — Find First and Last Position of Element in Sorted Array

## Description

Given an array of integers `nums` sorted in **non-decreasing order**, find the
starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

## Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `nums` is a **non-decreasing** array (duplicates allowed).
- `-10^9 <= target <= 10^9`

## Examples

### Example 1

```
Input:  nums = [5, 7, 7, 8, 8, 10], target = 8
Output: [3, 4]
Explanation: The value 8 first appears at index 3 and last appears at index 4.
```

### Example 2

```
Input:  nums = [5, 7, 7, 8, 8, 10], target = 6
Output: [-1, -1]
Explanation: 6 is not in the array, so both positions are -1.
```

### Example 3

```
Input:  nums = [], target = 0
Output: [-1, -1]
Explanation: The array is empty, so the target cannot be found.
```

## Hint

Run **Binary Search** twice: once to find the *leftmost* index of the target
(the lower bound) and once to find the *rightmost* index (just before the upper
bound). Duplicates make a single equality search insufficient.
