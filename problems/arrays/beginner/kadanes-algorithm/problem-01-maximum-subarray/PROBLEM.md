# Maximum Subarray

**Difficulty:** Easy

**Source:** LeetCode 53 — Maximum Subarray

## Description

Given an integer array `nums`, find the contiguous subarray (containing at
least one number) which has the largest sum, and return that sum.

A *subarray* is a contiguous, non-empty slice of the original array. You must
return the value of the maximum sum itself, not the subarray.

Note that the array may contain negative numbers, and it may consist entirely
of negative numbers — in that case the answer is the single largest (least
negative) element, since the subarray must be non-empty.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Examples

### Example 1

```
Input:  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The subarray [4, -1, 2, 1] has the largest sum, 4 + (-1) + 2 + 1 = 6.
```

### Example 2

```
Input:  nums = [1]
Output: 1
Explanation: The only subarray is [1], whose sum is 1.
```

### Example 3

```
Input:  nums = [5, 4, -1, 7, 8]
Output: 23
Explanation: The entire array [5, 4, -1, 7, 8] sums to 23, the maximum possible.
```

## Hint

Scan the array once, maintaining the best subarray sum that ends at the current
position. At each step decide whether to extend the previous subarray or start
a new one — this is **Kadane's Algorithm**.
