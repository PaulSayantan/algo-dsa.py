# Max Value of Equation

**Difficulty:** Hard

**Source:** LeetCode 1499 — Max Value of Equation

## Description

Given `points` sorted by x-coordinate and an integer `k`, return the maximum value of `yi + yj + |xi - xj|` over pairs with `|xi - xj| <= k` and `i < j`.

## Examples

### Example 1

```
Input:  points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
Output: 4
```

## Hint

For j, maximize (yj + xj) + max over window of (yi - xi); keep that window max in a monotonic deque of (yi - xi, xi).
