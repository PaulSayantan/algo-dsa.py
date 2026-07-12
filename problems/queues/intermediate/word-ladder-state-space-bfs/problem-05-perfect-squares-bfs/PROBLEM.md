# Perfect Squares (BFS)

**Difficulty:** Medium

**Source:** LeetCode 279 — Perfect Squares

## Description

Given an integer `n`, return the least number of perfect-square numbers (`1, 4, 9, 16, ...`) that sum to `n`. A perfect square may be used more than once.

Frame it as a shortest-path search: each remaining amount is a state, and subtracting any perfect square `<= remaining` is an edge of cost 1. BFS from `n` to `0` gives the fewest terms.

Constraints: `1 <= n <= 10^4`.

## Examples

### Example 1

```
Input:  n=12
Output: 3
```

**Explanation:** `12 = 4 + 4 + 4`, three perfect squares. No two-square sum equals 12.

## Hint

States are remaining values; neighbors subtract a perfect square. A BFS layer from `n` down to `0` counts the minimum number of squares.
