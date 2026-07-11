# Jump Game VI

**Difficulty:** Medium

**Source:** LeetCode 1696 — Jump Game VI

## Description

You are given a 0-indexed integer array `nums` and an integer `k`.

You start at index `0`. In one move, from index `i` you may jump to any index
`j` with `i < j <= i + k` (that is, forward by between `1` and `k` positions,
without going past the end of the array).

Your **score** is the sum of `nums[j]` for every index `j` you land on,
**including** the starting index `0` and the final index `n - 1`.

Return the **maximum score** you can obtain by reaching the last index `n - 1`.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`

## Examples

### Example 1

```
Input:  nums = [1, -1, -2, 4, -7, 3], k = 2
Output: 7
```

**Explanation:** One optimal path is `0 -> 1 -> 3 -> 5` (indices), collecting
`1 + (-1) + 4 + 3 = 7`. Every jump moves forward by at most `k = 2`.

### Example 2

```
Input:  nums = [10, -5, -2, 4, 0, 3], k = 3
Output: 17
```

**Explanation:** The path `0 -> 3 -> 5` collects `10 + 4 + 3 = 17`. Each jump of
length `3` is allowed since `k = 3`.

### Example 3

```
Input:  nums = [1, -5, -20, 4, -1, 3, -6, -3], k = 2
Output: 0
```

**Explanation:** The best reachable total to the last index is `0`, achieved by
a path such as `0 -> 1 -> 3 -> 5 -> 7`, collecting `1 - 5 + 4 + 3 - 3 = 0`.

## Hint

Let `dp[i]` be the best score to reach index `i`. Then
`dp[i] = nums[i] + max(dp[j])` over `j in [i-k, i-1]`. That inner "max over the
previous `k` values" is a **Monotonic Deque** sliding-window maximum, turning an
`O(n*k)` DP into `O(n)`.
