# Unique Paths

**Difficulty:** Medium

**Source:** LeetCode 62 — Unique Paths

## Description

A robot is located at the top-left corner of an `m x n` grid (marked as cell
`(0, 0)`). The robot can only move **either down or right** at any point in time.
The robot is trying to reach the bottom-right corner of the grid (cell
`(m - 1, n - 1)`).

Given the two integers `m` and `n`, return *the number of possible unique paths*
that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to
`2 * 10^9`.

## Constraints

- `1 <= m, n <= 100`
- The answer is guaranteed to be at most `2 * 10^9`.

## Examples

### Example 1

```
Input: m = 3, n = 7
Output: 28
```

**Explanation:** From the top-left corner there are 28 distinct sequences of
right/down moves that end at the bottom-right corner of a 3-row, 7-column grid.

### Example 2

```
Input: m = 3, n = 2
Output: 3
```

**Explanation:** The three unique paths on a 3x2 grid are:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

### Example 3

```
Input: m = 1, n = 1
Output: 1
```

**Explanation:** The robot already starts at the destination, so there is exactly
one path (the empty sequence of moves).

## Hint

Use **Dynamic Programming on Grid**: the number of ways to reach a cell equals the
number of ways to reach the cell directly above it plus the number of ways to reach
the cell directly to its left. Fill the first row and first column with 1s and build
the rest from those two neighbors.
