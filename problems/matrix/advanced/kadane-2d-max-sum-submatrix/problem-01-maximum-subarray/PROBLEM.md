# Maximum Subarray

**Difficulty:** Medium

**Source:** LeetCode 53 — Maximum Subarray

## Description

Given an integer array `nums`, find the contiguous subarray (containing at
least one element) that has the largest sum, and return that sum.

A *subarray* is a contiguous, non-empty slice of the array. You are choosing a
start index `i` and an end index `j` (with `i <= j`) so that
`nums[i] + nums[i+1] + ... + nums[j]` is as large as possible.

This is the 1D building block for Kadane 2D. Fully internalizing the running
"extend-or-restart" invariant here makes the matrix version straightforward:
Kadane 2D repeatedly compresses a band of matrix rows into a single 1D array
and then calls exactly this routine.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Examples

### Example 1

```
Input:  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
```

**Explanation:** The subarray `[4, -1, 2, 1]` has the largest sum `4 + (-1) + 2 + 1 = 6`.

### Example 2

```
Input:  nums = [1]
Output: 1
```

**Explanation:** The array has a single element, so the only subarray is `[1]` with sum `1`.

### Example 3

```
Input:  nums = [-3, -1, -2]
Output: -1
```

**Explanation:** All elements are negative, so the best we can do is pick the
single largest element `-1`. Because a subarray must be non-empty, we cannot
return `0`.

## Hint

Use **Kadane 2D (max sum submatrix)** — specifically its 1D core (Kadane's
algorithm). Walk left to right keeping the best subarray sum that *ends at the
current index*; at each step decide whether to extend the previous best or
restart from the current element.
