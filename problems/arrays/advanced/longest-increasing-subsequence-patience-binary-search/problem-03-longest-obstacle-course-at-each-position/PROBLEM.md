# Longest Obstacle Course at Each Position

**Difficulty:** Hard

**Source:** LeetCode 1964 — Find the Longest Valid Obstacle Course at Each Position

## Description

You want to build an obstacle course. You are given an integer array
`obstacles` of length `n`, where `obstacles[i]` is the height of the `i`-th
obstacle.

For every index `i` (`0 <= i < n`), find the length of the longest obstacle
course you can build such that:

- You choose obstacles from indices `0` to `i` (inclusive), keeping them in
  their original order.
- Each chosen obstacle **must include** the obstacle at index `i` as the last
  one in the course.
- Every obstacle in the course must be **taller than or equal to** the
  obstacle before it (the course is **non-decreasing** in height).

Return an array `ans` of length `n` where `ans[i]` is the length of the
longest valid obstacle course that ends at index `i`.

## Constraints

- `n == obstacles.length`
- `1 <= n <= 10^5`
- `1 <= obstacles[i] <= 10^7`

## Examples

### Example 1

```
Input:  obstacles = [1, 2, 3, 2]
Output: [1, 2, 3, 3]
Explanation:
  i = 0: [1]           -> length 1
  i = 1: [1, 2]        -> length 2
  i = 2: [1, 2, 3]     -> length 3
  i = 3: [1, 2, 2]     -> length 3 (the last 2 attaches after the first 2)
```

### Example 2

```
Input:  obstacles = [2, 2, 1]
Output: [1, 2, 1]
Explanation:
  i = 0: [2]        -> length 1
  i = 1: [2, 2]     -> length 2 (non-decreasing allows equal heights)
  i = 2: [1]        -> length 1 (1 cannot follow either 2)
```

### Example 3

```
Input:  obstacles = [3, 1, 5, 6, 4, 2]
Output: [1, 1, 2, 3, 2, 2]
Explanation:
  i = 0: [3]              -> 1
  i = 1: [1]              -> 1
  i = 2: [3, 5] or [1, 5] -> 2
  i = 3: [3, 5, 6]        -> 3
  i = 4: [3, 4] or [1, 4] -> 2
  i = 5: [1, 2]           -> 2
```

## Hint

Use the Longest Increasing Subsequence (patience / binary search) technique,
but for a **non-decreasing** course. The answer for index `i` is the position
where `obstacles[i]` lands in the `tails` array — record it as you insert,
and remember to use an upper-bound binary search so equal heights still count.
