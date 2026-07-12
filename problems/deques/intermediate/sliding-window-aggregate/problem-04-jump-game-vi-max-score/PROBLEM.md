# Jump Game VI — Maximum Score

**Difficulty:** Medium

**Source:** LeetCode 1696 — Jump Game VI

## Description

You start at index `0` of a 0-indexed integer array `nums` of length `n` and want to reach index `n - 1`. From index `i` you may jump to any index in the range `[i + 1, i + k]` (staying within bounds). Your score is the **sum** of `nums[j]` over every index `j` you land on, including index `0` and index `n - 1`. Return the maximum score you can achieve.

Constraints: `1 <= k <= n`; values may be negative.

## Examples

### Example 1

```
Input:  nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
```

**Explanation:** Take the path `0 -> 1 -> 3 -> 5`: `1 + (-1) + 4 + 3 = 7`.

### Example 2

```
Input:  nums = [10,-5,-2,4,0,3], k = 3
Output: 17
```

**Explanation:** Take the path `0 -> 3 -> 5`: `10 + 4 + 3 = 17`.

## Hint

Let `dp[i] = nums[i] + max(dp[i-k..i-1])`. Maintain that windowed maximum with a decreasing monotonic deque so each `dp[i]` is O(1) amortized.
