# Longest Increasing Subsequence II

**Difficulty:** Hard

**Source:** LeetCode 2407 — Longest Increasing Subsequence II

## Description

You are given an integer array `nums` and an integer `k`. Find the length of the
longest subsequence of `nums` that satisfies **both**:

1. The subsequence is **strictly increasing**.
2. The difference between **adjacent** elements in the subsequence is **at most `k`**
   (i.e. for consecutive picked elements `a` then `b`, `0 < b - a <= k`).

A *subsequence* is obtained by deleting zero or more elements without changing the
order of the remaining elements.

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i], k <= 10^5`

## Examples

### Example 1

```
Input:  nums = [4, 2, 1, 4, 3, 4, 5, 8, 15], k = 3
Output: 5
```

**Explanation:** The subsequence `[1, 3, 4, 5, 8]` is strictly increasing and every
adjacent gap (`3-1=2`, `4-3=1`, `5-4=1`, `8-5=3`) is at most `k = 3`. Its length is
`5`. Note `15` cannot extend it because `15 - 8 = 7 > 3`.

### Example 2

```
Input:  nums = [7, 4, 5, 1, 8, 12, 4, 7], k = 5
Output: 4
```

**Explanation:** One optimal subsequence is `[4, 5, 8, 12]`: gaps `1, 3, 4` are all
`<= 5`, length `4`. (`12 -> ...` cannot be extended forward within the array.)

### Example 3

```
Input:  nums = [1, 5], k = 1
Output: 1
```

**Explanation:** `5 - 1 = 4 > k = 1`, so the two elements cannot be adjacent in the
subsequence. The best is any single element, length `1`.

## Hint

Do a DP over values: `dp[v]` = longest valid subsequence ending with value `v`. The
transition needs the **maximum `dp` over the value window `[v - k, v - 1]`**. Maintain
that with a **Segment Tree over the value domain supporting range-max query + point
update**, turning an `O(n^2)` DP into `O(n log n)`.
