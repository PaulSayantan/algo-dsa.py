# Jump Game VI

**Difficulty:** Medium

**Source:** LeetCode 1696 — Jump Game VI

## Description

You start at index `0` of an integer array `nums` and want to reach the last index `n - 1`. From index `i` you may jump to any index `j` with `i < j <= i + k` (a step of size 1..`k`). Your score is the sum of `nums[j]` for every index `j` you land on, including index `0` and the final index. Return the **maximum** score you can achieve.

Constraints: `1 <= len(nums)`, `1 <= k <= len(nums)`.

## Examples

### Example 1

```
Input:  nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
```

**Explanation:** One optimal path visits indices `0 -> 1 -> 3 -> 5`, scoring `1 + (-1) + 4 + 3 = 7`.

### Example 2

```
Input:  nums = [10,-5,-2,4,0,3], k = 3
Output: 17
```

**Explanation:** Visit indices `0 -> 3 -> 5`, scoring `10 + 4 + 3 = 17`.

## Hint

`dp[i] = nums[i] + max(dp[i-k..i-1])`; keep a decreasing monotonic deque of indices so the best previous `dp` inside the window `[i-k, i-1]` is always at the front.
