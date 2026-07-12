# Jump Game VI

**Difficulty:** Medium

**Source:** LeetCode 1696 — Jump Game VI

## Description

Starting at index 0 of `nums`, each move jumps forward between 1 and `k` indices. The score is the sum of `nums` values at visited indices (including index 0 and the last index). Return the maximum score to reach the last index.

## Examples

### Example 1

```
Input:  nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
```

## Hint

dp[i] = nums[i] + max(dp[i-k..i-1]); maintain the window max of dp with a decreasing deque.
