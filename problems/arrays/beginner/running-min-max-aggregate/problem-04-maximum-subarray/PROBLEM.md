# Maximum Subarray

**Difficulty:** Medium

**Source:** LeetCode 53 — Maximum Subarray (classic Kadane's algorithm)

## Description

Given an integer array `nums`, find the contiguous subarray (containing at
least one number) which has the largest sum, and return that sum.

A subarray is a contiguous, non-empty slice of the array.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- The subarray must contain at least one element (you cannot pick an empty
  subarray, so the answer for an all-negative array is its largest single
  element).

## Examples

### Example 1

```
Input:  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The subarray [4, -1, 2, 1] has the largest sum = 6.
```

### Example 2

```
Input:  nums = [1]
Output: 1
Explanation: The only subarray is [1], whose sum is 1.
```

### Example 3

```
Input:  nums = [-3, -1, -2]
Output: -1
Explanation: Every number is negative, so the best we can do is pick the single
largest element, -1. A non-empty subarray is required.
```

## Hint

Keep a **Running best sum ending at the current index**: either extend the
previous best-ending-here by the current element, or start fresh at the current
element. Track the maximum of these running values (Kadane's algorithm).
