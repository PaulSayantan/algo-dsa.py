# Maximum Score of a Good Subarray

**Difficulty:** Medium

**Source:** LeetCode 1793 — Maximum Score of a Good Subarray

## Description

Given an integer array `nums` and an index `k`, a *good subarray* is a contiguous subarray `nums[i..j]` with `i <= k <= j`. Its score is `min(nums[i..j]) * (j - i + 1)`. Return the maximum possible score of a good subarray.

Constraints: `1 <= len(nums)`; `0 <= k < len(nums)`; values are non-negative integers.

## Examples

### Example 1

```
Input:  nums = [1,4,3,7,4,5], k = 3
Output: 15
```

**Explanation:** The subarray `[4,3,7,4,5]` (indices 1..5) has minimum `3` and length `5`, giving `3 * 5 = 15`.

### Example 2

```
Input:  nums = [5,5,4,5,4,1,1,1], k = 0
Output: 20
```

**Explanation:** The subarray `[5,5,4,5,4]` (indices 0..4) has minimum `4` and length `5`, giving `4 * 5 = 20`, the best of any window covering index `0`.

## Hint

Think of `nums` as histogram bar heights: for each bar as the minimum, find how far it extends left/right until a strictly shorter bar (its previous/next-smaller boundaries via a monotonic stack); if that maximal span covers index `k`, its `height * width` is a candidate.
