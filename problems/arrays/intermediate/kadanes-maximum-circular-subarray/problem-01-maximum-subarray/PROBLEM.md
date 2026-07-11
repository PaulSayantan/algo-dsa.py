# Maximum Subarray

**Difficulty:** Easy (Medium on LeetCode)

**Source:** LeetCode 53 — Maximum Subarray

## Description

Given an integer array `nums`, find the **contiguous, non-empty subarray**
with the largest sum, and return that sum.

A subarray is a contiguous, non-empty sequence of elements within the array.
Only the value of the maximum sum is required — you do not have to return the
subarray itself.

This is the **linear** (non-circular) version of the maximum-subarray problem
and the foundation every circular variant builds on. Master the single-pass
solution here before moving to the wrap-around problems in this folder.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Examples

### Example 1

```
Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The subarray [4, -1, 2, 1] (indices 3..6) has the largest sum, 6.
```

### Example 2

```
Input: nums = [1]
Output: 1
Explanation: The only subarray is [1]; its sum is 1.
```

### Example 3

```
Input: nums = [5, 4, -1, 7, 8]
Output: 23
Explanation: The entire array [5, 4, -1, 7, 8] sums to 23, which is the
maximum. Even though -1 is negative, dropping it would split the array and
lose the large positive tail.
```

## Hint

Sweep once, keeping a running "best sum of a subarray ending here." At each
element decide whether to extend the previous run or start fresh at the
current element. This is the base case of Kadane's — Maximum Circular Subarray.
