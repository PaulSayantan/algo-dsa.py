# Minimum Path Sum

**Difficulty:** Medium

**Source:** LeetCode 64 — Minimum Path Sum

## Description

Given an `m x n` grid filled with non-negative numbers, find a path from the
top-left corner to the bottom-right corner which **minimizes the sum of all numbers
along its path**.

You can only move **either down or right** at any point in time.

Return the minimum sum.

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 200`
- `0 <= grid[i][j] <= 200`

## Examples

### Example 1

```
Input: grid = [[1,3,1],
               [1,5,1],
               [4,2,1]]
Output: 7
```

**Explanation:** The path `1 -> 3 -> 1 -> 1 -> 1` (right, right, down, down) yields
the minimum sum `1 + 3 + 1 + 1 + 1 = 7`. No other right/down path is cheaper.

### Example 2

```
Input: grid = [[1,2,3],
               [4,5,6]]
Output: 12
```

**Explanation:** The path `1 -> 2 -> 3 -> 6` sums to `12`. The alternative
`1 -> 4 -> 5 -> 6 = 16` and `1 -> 2 -> 5 -> 6 = 14` are both larger.

### Example 3

```
Input: grid = [[5]]
Output: 5
```

**Explanation:** A single cell grid; the only path is the start cell itself.

## Hint

Use **Dynamic Programming on Grid**: the cheapest way to reach a cell is its own
value plus the cheaper of the two ways to reach it — from directly above or from
directly to the left.
