# Find Rotation Count in a Rotated Sorted Array

**Difficulty:** Medium

**Source:** GeeksforGeeks — "Find the Rotation Count in Rotated Sorted Array"
(classic interview variant of LeetCode 153)

## Description

An ascending sorted array of **distinct** integers has been rotated clockwise an
unknown number of times. Each rotation moves the last element to the front, so
after `k` rotations the array
`[a0, a1, ..., a(n-1)]` becomes
`[a(n-k), ..., a(n-1), a0, a1, ..., a(n-k-1)]`.

Given the rotated array `nums`, return the number of rotations `k` that were
applied. Equivalently, return the **index of the minimum element**, because that
is exactly how many positions the original head was pushed to the right.

You must solve it in `O(log n)` time.

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- All values of `nums` are **unique**.
- `nums` is an ascending array rotated `k` times, where `0 <= k < nums.length`.

## Examples

**Example 1**

```
Input:  nums = [15,18,2,3,6,12]
Output: 2
Explanation: The sorted array [2,3,6,12,15,18] was rotated 2 times. The minimum
value 2 sits at index 2, and 2 rotations were applied.
```

**Example 2**

```
Input:  nums = [7,9,11,12,5]
Output: 4
Explanation: The sorted array [5,7,9,11,12] was rotated 4 times. The minimum
value 5 is at index 4.
```

**Example 3**

```
Input:  nums = [1,2,3,4]
Output: 0
Explanation: The array is fully sorted (rotated 0 times), so the minimum is at
index 0 and the rotation count is 0.
```

## Hint

Use the Search in Rotated Sorted Array technique: the rotation count equals the
index of the minimum, which you can locate with a pivot binary search comparing
`nums[mid]` against `nums[hi]`.
