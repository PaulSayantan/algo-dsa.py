# Search in Rotated Sorted Array II

**Difficulty:** Medium

**Source:** LeetCode 81 — Search in Rotated Sorted Array II

## Description

There is an integer array `nums` sorted in non-decreasing order (**not
necessarily with distinct values**). Before being passed to your function,
`nums` is rotated at an unknown pivot index `k` (`0 <= k < nums.length`) so that
the resulting array is
`[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`
(0-indexed). For example, `[0,1,2,4,4,4,5,6,6,7]` might be rotated at pivot
index `5` and become `[4,5,6,6,7,0,1,2,4,4]`.

Given the array `nums` **after** the rotation and an integer `target`, return
`true` if `target` is in `nums`, or `false` if it is not.

You must decrease the overall operation steps as much as possible.

## Constraints

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is guaranteed to be rotated at some pivot.
- `-10^4 <= target <= 10^4`
- `nums` may contain **duplicates**.

## Examples

**Example 1**

```
Input:  nums = [2,5,6,0,0,1,2], target = 0
Output: true
Explanation: 0 is present (at index 3 and 4), so the answer is true.
```

**Example 2**

```
Input:  nums = [2,5,6,0,0,1,2], target = 3
Output: false
Explanation: 3 never appears in nums, so the answer is false.
```

**Example 3**

```
Input:  nums = [1,0,1,1,1], target = 0
Output: true
Explanation: The duplicated 1s at both ends hide which half is sorted, but a
single 0 is present, so the answer is true.
```

## Hint

Use the Search in Rotated Sorted Array technique, but add a guard for the case
`nums[lo] == nums[mid] == nums[hi]`: when you cannot tell which half is sorted,
shrink both ends by one and continue.
