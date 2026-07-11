# Find Minimum in Rotated Sorted Array

**Difficulty:** Medium

**Source:** LeetCode 153 — Find Minimum in Rotated Sorted Array

## Description

Suppose an array of length `n` sorted in ascending order is rotated between `1`
and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

- `[4,5,6,7,0,1,2]` if it was rotated `4` times.
- `[0,1,2,4,5,6,7]` if it was rotated `7` times (back to the original order).

Notice that rotating the array `4` times moves the last four elements to the
front. Given the sorted rotated array `nums` of **unique** elements, return the
**minimum element** of this array.

You must write an algorithm that runs in `O(log n)` time.

## Constraints

- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All the integers of `nums` are **unique**.
- `nums` is sorted and rotated between `1` and `n` times.

## Examples

**Example 1**

```
Input:  nums = [3,4,5,1,2]
Output: 1
Explanation: The original sorted array was [1,2,3,4,5], rotated 3 times so that
the last three elements moved to the front. The minimum, 1, sits at the pivot.
```

**Example 2**

```
Input:  nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array [0,1,2,4,5,6,7] was rotated 4 times. The
smallest value is 0.
```

**Example 3**

```
Input:  nums = [11,13,15,17]
Output: 11
Explanation: The array was rotated n times, so it is fully sorted and the
minimum is simply the first element.
```

## Hint

Use the Search in Rotated Sorted Array technique: binary search for the pivot by
comparing `nums[mid]` with `nums[hi]` to decide which half still holds the
minimum.
