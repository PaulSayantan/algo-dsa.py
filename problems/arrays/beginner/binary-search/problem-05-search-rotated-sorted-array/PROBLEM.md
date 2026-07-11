# Search in Rotated Sorted Array

**Difficulty:** Medium

**Source:** LeetCode 33 — Search in Rotated Sorted Array

## Description

There is an integer array `nums` sorted in ascending order (with **distinct**
values). Prior to being passed to your function, `nums` is possibly **rotated**
at an unknown pivot index `k` (`0 <= k < nums.length`), so that the array
becomes `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`
(0-indexed).

For example, `[0, 1, 2, 4, 5, 6, 7]` might be rotated at pivot index 3 to become
`[4, 5, 6, 7, 0, 1, 2]`.

Given the array `nums` **after** the possible rotation and an integer `target`,
return the **index** of `target` if it is in `nums`, or `-1` if it is not.

You must write an algorithm with `O(log n)` runtime complexity.

## Constraints

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values of `nums` are **unique**.
- `nums` is an ascending array that is **possibly rotated**.
- `-10^4 <= target <= 10^4`

## Examples

### Example 1

```
Input:  nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4
Explanation: 0 is located at index 4 in the rotated array.
```

### Example 2

```
Input:  nums = [4, 5, 6, 7, 0, 1, 2], target = 3
Output: -1
Explanation: 3 is not present in the array, so return -1.
```

### Example 3

```
Input:  nums = [1], target = 0
Output: -1
Explanation: The only element is 1, which is not the target.
```

## Hint

Use **Binary Search**. At each `mid`, one of the two halves `[lo, mid]` or
`[mid, hi]` is guaranteed to be *sorted*. Decide which half is sorted, check
whether the target falls inside that sorted range, and recurse into the correct
side.
