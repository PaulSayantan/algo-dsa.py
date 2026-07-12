# Perfect Squares

**Difficulty:** Medium

**Source:** LeetCode 279 — Perfect Squares

## Description

Given an integer `n`, return the least number of perfect-square numbers (`1, 4, 9, 16, ...`) that sum to `n`. The same square may be used multiple times.

Constraints: `0 <= n <= 10^4` (with `n = 0` the empty sum gives `0`).

## Examples

### Example 1

```
Input:  n = 12
Output: 3
```

**Explanation:** `12 = 4 + 4 + 4`.

### Example 2

```
Input:  n = 13
Output: 2
```

**Explanation:** `13 = 4 + 9`.

## Hint

Model each reachable running total as a graph node and BFS in layers: each layer adds one more square, so the first layer that reaches `n` is the minimum count.
