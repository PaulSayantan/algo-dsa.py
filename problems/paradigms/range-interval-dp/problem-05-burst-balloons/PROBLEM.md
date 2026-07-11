# Burst Balloons

**Difficulty:** Hard

**Source:** LeetCode 312 — Burst Balloons

## Description

You are given `n` balloons, indexed from `0` to `n - 1`. Each balloon is painted
with a number on it represented by an array `nums`. You are asked to burst all
the balloons.

If you burst the `i`-th balloon, you will get
`nums[i - 1] * nums[i] * nums[i + 1]` coins. If `i - 1` or `i + 1` goes out of
bounds of the array, then treat it as if there is a balloon with a `1` painted
on it (a virtual `1` on each side).

Return the **maximum coins** you can collect by bursting the balloons wisely.

## Constraints

- `n == nums.length`
- `1 <= n <= 300`
- `0 <= nums[i] <= 100`

## Examples

### Example 1
```
Input:  nums = [3, 1, 5, 8]
Output: 167
Explanation: Treat the array as [1] 3 1 5 8 [1].
Burst order 1 -> 5 -> 3 -> 8:
- burst 1: 3*1*5 = 15,   nums -> [3, 5, 8]
- burst 5: 3*5*8 = 120,  nums -> [3, 8]
- burst 3: 1*3*8 = 24,   nums -> [8]
- burst 8: 1*8*1 = 8,    nums -> []
Total = 15 + 120 + 24 + 8 = 167, the maximum possible.
```

### Example 2
```
Input:  nums = [1, 5]
Output: 10
Explanation: Treat as [1] 1 5 [1].
Burst 1 first: 1*1*5 = 5, then burst 5: 1*5*1 = 5. Total = 10.
(Bursting 5 first gives 1*5*1=5 then 1*1*1=1, total 6 — worse.)
```

### Example 3
```
Input:  nums = [7]
Output: 7
Explanation: Only one balloon. Bursting it yields 1*7*1 = 7.
```

## Hint

Think **Range / Interval DP**, but with a twist: instead of "which balloon to
burst first", pick the balloon `k` that is burst **last** within an interval, so
its neighbors are the fixed interval boundaries.
