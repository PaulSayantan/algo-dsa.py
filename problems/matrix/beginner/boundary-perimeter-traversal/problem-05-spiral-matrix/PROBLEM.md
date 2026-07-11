# Spiral Matrix

**Difficulty:** Medium

**Source:** LeetCode 54 — "Spiral Matrix"

## Description

Given an `m x n` matrix, return **all elements of the matrix in spiral order**.

Spiral order starts at the top-left corner and walks clockwise: across the top row, down
the right column, back across the bottom row, up the left column, and then repeats on the
next inner ring, spiraling inward until every element has been visited exactly once.

This is **boundary traversal applied repeatedly**: each loop of the spiral is the
perimeter of the current sub-matrix, after which the borders shrink inward by one and the
next (smaller) perimeter is traversed.

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`

## Examples

### Example 1

```
Input:  matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
Explanation: Outer ring clockwise gives 1,2,3,6,9,8,7,4; the only cell left, the
             interior 5, is the final element.
```

### Example 2

```
Input:  matrix = [[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]]
Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
Explanation: Outer ring: 1,2,3,4,8,12,11,10,9,5. The inner sub-row 6,7 is then traversed
             left to right, giving 6,7.
```

### Example 3 (single column)

```
Input:  matrix = [[7],
                  [9],
                  [6]]
Output: [7, 9, 6]
Explanation: A single column: the first "ring" is just the column read top to bottom;
             the shrink guards prevent re-reading it.
```

## Hint

Use **Boundary / Perimeter Traversal** in a loop: traverse the current outer ring, then
move `top`, `bottom`, `left`, `right` inward by one and repeat. Guard the bottom-row and
left-column sweeps with `top <= bottom` / `left <= right` so the final row or column is
not emitted twice.
