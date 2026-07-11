# Spiral Matrix

**Difficulty:** Medium

**Source:** LeetCode 54 — Spiral Matrix

## Description

Given an `m x n` matrix, return all elements of the matrix in **spiral order**.

Spiral order starts at the top-left corner and proceeds **clockwise**: move
right across the top row, then down the right column, then left across the
bottom row, then up the left column, and continue spiraling inward until every
element has been listed exactly once.

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`

## Examples

### Example 1

```
Input:  matrix = [[1,2,3],
                  [4,5,6],
                  [7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

Explanation: Right along the top row `1,2,3`; down the right column `6,9`; left
along the bottom row `8,7`; up the left column `4`; finally the lone inner cell
`5`.

### Example 2

```
Input:  matrix = [[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

Explanation: Top row `1,2,3,4`; right column `8,12`; bottom row `11,10,9`; left
column `5`; then the inner row `6,7`.

### Example 3

```
Input:  matrix = [[7]]
Output: [7]
```

Explanation: A single cell is already its own spiral.

## Hint

Track four boundaries — `top`, `bottom`, `left`, `right` — and peel one ring
off the matrix per loop. This is a classic **Spiral Traversal**.
