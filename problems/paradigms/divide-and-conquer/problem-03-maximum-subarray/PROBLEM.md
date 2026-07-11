# Maximum Subarray

**Difficulty:** Medium

**Source:** LeetCode 53 (Maximum Subarray)

## Description

Given an integer array `nums`, find the **contiguous subarray** (containing at least
one number) that has the **largest sum**, and return that sum.

A subarray is a contiguous, non-empty slice of the array.

While Kadane's algorithm solves this in `O(n)`, the problem is a classic Divide and
Conquer exercise (CLRS §4.1): the maximum subarray of a range either lies entirely in
the left half, entirely in the right half, or **crosses the midpoint** — and the
crossing case is what the combine step computes.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Examples

### Example 1

```
Input:  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
```

Explanation: The subarray `[4, -1, 2, 1]` has sum `4 + (-1) + 2 + 1 = 6`, the largest
of any contiguous subarray.

### Example 2

```
Input:  nums = [1]
Output: 1
```

Explanation: The only subarray is `[1]`, so the answer is `1`.

### Example 3

```
Input:  nums = [-3, -1, -2]
Output: -1
```

Explanation: Every element is negative, so the best we can do is the single largest
element `-1` (the subarray must be non-empty).

## Hint

Use **Divide and Conquer**: split at the midpoint. The best subarray is the maximum of
three quantities — the best subarray fully in the left half, the best fully in the
right half, and the best subarray that **crosses the midpoint** (extend a running sum
leftward from `mid` and rightward from `mid+1` and add them).
