# Minimum Size Subarray Sum

**Difficulty:** Medium

**Source:** LeetCode 209 — Minimum Size Subarray Sum

## Description

Given an array of **positive** integers `nums` and a positive integer `target`,
return the **minimal length** of a contiguous subarray `[nums[l], nums[l+1], ..., nums[r]]`
whose sum is **greater than or equal to** `target`.

If there is no such subarray, return `0` instead.

Because every element is positive, extending a subarray on the right can only
*increase* its sum, and dropping elements from the left can only *decrease* it.
That monotonic behavior is exactly what lets a window grow and shrink cleanly.

## Constraints

- `1 <= target <= 10^9`
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`

## Examples

### Example 1

```
Input:  target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has sum 7 >= 7 and has the minimal length 2.
             No single element reaches 7, so length 2 is optimal.
```

### Example 2

```
Input:  target = 4, nums = [1,4,4]
Output: 1
Explanation: The single element [4] already has sum 4 >= 4, so length 1 suffices.
```

### Example 3

```
Input:  target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
Explanation: The total sum of the whole array is 8 < 11, so no subarray qualifies.
```

## Hint

Use a **Sliding Window (variable size)**. Grow the window on the right to
accumulate the sum, and once the sum reaches `target`, shrink from the left to
find the shortest qualifying window.
