# Longest Increasing Subsequence

**Difficulty:** Medium

**Source:** LeetCode 300 — Longest Increasing Subsequence

## Description

Given an integer array `nums`, return the length of the longest **strictly
increasing subsequence**.

A subsequence is an array derived from `nums` by deleting some or no elements
without changing the order of the remaining elements. For example,
`[3, 6, 2, 7]` is a subsequence of `[0, 3, 1, 6, 2, 2, 7]`.

The chosen elements do not have to be contiguous, but their relative order
must be preserved and each element must be strictly greater than the previous
one in the subsequence.

## Constraints

- `1 <= nums.length <= 2500`
- `-10^4 <= nums[i] <= 10^4`
- Follow-up: can you design an algorithm that runs in `O(n log n)` time?

## Examples

### Example 1

```
Input:  nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Explanation: One longest increasing subsequence is [2, 3, 7, 101],
             which has length 4. ([2, 3, 7, 18] also has length 4.)
```

### Example 2

```
Input:  nums = [0, 1, 0, 3, 2, 3]
Output: 4
Explanation: The subsequence [0, 1, 2, 3] has length 4, and no longer
             strictly increasing subsequence exists.
```

### Example 3

```
Input:  nums = [7, 7, 7, 7, 7, 7, 7]
Output: 1
Explanation: All elements are equal, so no strictly increasing pair exists.
             The longest increasing subsequence is any single element,
             giving length 1.
```

## Hint

Use the Longest Increasing Subsequence (patience / binary search) technique:
maintain a `tails` array whose length is the answer, and use binary search to
find where each new value belongs.
