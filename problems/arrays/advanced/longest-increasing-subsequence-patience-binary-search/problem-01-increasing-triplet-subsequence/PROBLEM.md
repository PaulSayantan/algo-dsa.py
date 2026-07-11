# Increasing Triplet Subsequence

**Difficulty:** Medium

**Source:** LeetCode 334 — Increasing Triplet Subsequence

## Description

Given an integer array `nums`, return `true` if there exists a triple of
indices `(i, j, k)` such that `i < j < k` and
`nums[i] < nums[j] < nums[k]`. If no such indices exist, return `false`.

In other words, decide whether the array contains a strictly increasing
subsequence of length exactly 3 (or more). The three chosen elements do
**not** need to be adjacent — only their relative order in the array must be
preserved.

This is the smallest interesting instance of the Longest Increasing
Subsequence family: instead of asking for the *length* of the longest
increasing subsequence, it only asks whether that length reaches 3.

## Constraints

- `1 <= nums.length <= 5 * 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- Follow-up: can you do it in `O(n)` time and `O(1)` extra space?

## Examples

### Example 1

```
Input:  nums = [1, 2, 3, 4, 5]
Output: true
Explanation: The whole array is increasing, so many triples work,
             e.g. (nums[0], nums[1], nums[2]) = (1, 2, 3) with 1 < 2 < 3.
```

### Example 2

```
Input:  nums = [5, 4, 3, 2, 1]
Output: false
Explanation: The array is strictly decreasing, so not even an increasing
             pair exists, let alone a triple.
```

### Example 3

```
Input:  nums = [2, 1, 5, 0, 4, 6]
Output: true
Explanation: The triple of indices (3, 4, 5) gives values (0, 4, 6),
             and 0 < 4 < 6.
```

## Hint

Think about the Longest Increasing Subsequence (patience / binary search)
technique. The `tails` array that patience sorting maintains never needs to
grow past size 2 here — you only care whether a third "pile" would ever be
opened.
