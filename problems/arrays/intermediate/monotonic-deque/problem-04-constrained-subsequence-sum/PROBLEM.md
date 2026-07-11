# Constrained Subsequence Sum

**Difficulty:** Hard

**Source:** LeetCode 1425 — Constrained Subsequence Sum

## Description

Given an integer array `nums` and an integer `k`, return the **maximum sum** of a
non-empty **subsequence** of `nums` such that for every two consecutive elements
in the subsequence, `nums[i]` and `nums[j]` (with `i < j` being their original
indices), the condition `j - i <= k` holds.

A subsequence is obtained by deleting some (possibly zero) elements without
changing the order of the remaining elements. The constraint applies only to
elements that are **adjacent in the chosen subsequence**: their original indices
must be within `k` of each other.

## Constraints

- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Examples

### Example 1

```
Input:  nums = [10, 2, -10, 5, 20], k = 2
Output: 37
```

**Explanation:** The subsequence is `[10, 2, 5, 20]` (original indices
`0, 1, 3, 4`). Consecutive index gaps are `1, 2, 1`, all `<= 2`, and the sum is
`10 + 2 + 5 + 20 = 37`.

### Example 2

```
Input:  nums = [-1, -2, -3], k = 1
Output: -1
```

**Explanation:** Every element is negative, so the best non-empty subsequence is
the single element `-1`.

### Example 3

```
Input:  nums = [10, -2, -10, -5, 20], k = 2
Output: 23
```

**Explanation:** The tempting `[10, 20]` (indices `0, 4`) is invalid because the
gap `4 > k = 2`. A valid optimal subsequence is `[10, -2, -5, 20]` (indices
`0, 1, 3, 4`) with consecutive gaps `1, 2, 1`, all `<= 2`, summing to
`10 - 2 - 5 + 20 = 23`.

## Hint

Define `dp[i] = nums[i] + max(0, best dp in [i-k, i-1])`. The "best dp in the
previous `k` positions" is a sliding-window maximum — maintain it with a
**Monotonic Deque** to get `O(n)` overall.
