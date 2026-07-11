# Binary Search

**Difficulty:** Easy

**Source:** LeetCode 704 — Binary Search

## Description

Given an array of integers `nums` which is sorted in **ascending order**, and an
integer `target`, write a function to search for `target` in `nums`. If `target`
exists, return its **index**. Otherwise, return `-1`.

All integers in `nums` are **unique**. You must write an algorithm with
`O(log n)` runtime complexity.

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 < nums[i], target < 10^4`
- All the integers in `nums` are **unique**.
- `nums` is sorted in ascending order.

## Examples

### Example 1

```
Input:  nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4.
```

### Example 2

```
Input:  nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1
Explanation: 2 does not exist in nums, so the function returns -1.
```

### Example 3

```
Input:  nums = [5], target = 5
Output: 0
Explanation: The single element equals the target, at index 0.
```

## Hint

Use **Binary Search**: track an inclusive range `[lo, hi]`, compare the middle
element to the target, and discard the half that cannot contain the target.
