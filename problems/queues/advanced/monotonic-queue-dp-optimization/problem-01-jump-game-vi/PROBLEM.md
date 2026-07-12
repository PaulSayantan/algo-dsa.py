# Jump Game VI

**Difficulty:** Medium

**Source:** LeetCode 1696 — Jump Game VI

## Description

You start at index 0 of `nums` and each move jumps forward 1..`k` indices. Your score is the sum of `nums` at visited indices. Return the maximum score to reach the last index.

## Examples

### Example 1

```
Input:  nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
```

## Hint

dp[i] = nums[i] + max(dp[i-k..i-1]); maintain that window max with a monotonic deque.
