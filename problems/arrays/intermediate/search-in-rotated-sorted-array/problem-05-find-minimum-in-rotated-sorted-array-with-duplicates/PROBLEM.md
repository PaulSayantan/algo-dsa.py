# Find Minimum in Rotated Sorted Array II

**Difficulty:** Hard

**Source:** LeetCode 154 — Find Minimum in Rotated Sorted Array II

## Description

Suppose an array of length `n` sorted in ascending order is rotated between `1`
and `n` times. For example, the array `nums = [0,1,4,4,5,6,7]` might become:

- `[4,5,6,7,0,1,4]` if it was rotated `4` times.
- `[0,1,4,4,5,6,7]` if it was rotated `7` times (back to the original order).

Given the sorted rotated array `nums` that **may contain duplicates**, return
the **minimum element** of this array.

You must minimize the number of operations as much as possible.

## Constraints

- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- `nums` is sorted and rotated between `1` and `n` times.
- `nums` **may contain duplicates**.

## Examples

**Example 1**

```
Input:  nums = [1,3,5]
Output: 1
Explanation: Rotated back to sorted order; the minimum is the first element, 1.
```

**Example 2**

```
Input:  nums = [2,2,2,0,1]
Output: 0
Explanation: The original array [0,1,2,2,2] was rotated 3 times. The minimum
value is 0, even though 2 appears multiple times.
```

**Example 3**

```
Input:  nums = [3,3,1,3]
Output: 1
Explanation: Duplicated 3s at both ends make the sorted half ambiguous, but the
minimum is the single 1 in the middle.
```

## Hint

Use the Search in Rotated Sorted Array technique, comparing `nums[mid]` with
`nums[hi]`. Handle the tie `nums[mid] == nums[hi]` by decrementing `hi` by one —
this is the step that can degrade the worst case to O(n).
