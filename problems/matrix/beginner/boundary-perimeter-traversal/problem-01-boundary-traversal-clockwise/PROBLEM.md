# Boundary Traversal of a Matrix (Clockwise)

**Difficulty:** Easy

**Source:** GeeksforGeeks — "Boundary Traversal of matrix" (classic interview problem)

## Description

Given an `m x n` integer matrix, return a list of all the elements that lie on the
**boundary** (the outer ring) of the matrix, visited in **clockwise** order starting
from the top-left corner.

The clockwise order is:

1. The entire **top row**, left to right.
2. The **rightmost column** (excluding the corner already taken from the top row),
   top to bottom.
3. The entire **bottom row**, right to left (only if there is more than one row).
4. The **leftmost column** (excluding the corners already taken), bottom to top
   (only if there is more than one column).

Interior elements must **not** appear in the result, and each boundary element must
appear **exactly once** (no corner should be repeated).

## Constraints

- `1 <= m, n <= 1000`
- `-10^6 <= matrix[i][j] <= 10^6`
- The matrix is rectangular (every row has the same length).

## Examples

### Example 1

```
Input:  matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
Output: [1, 2, 3, 6, 9, 8, 7, 4]
Explanation: Top row 1,2,3 → right column 6,9 → bottom row (reversed) 8,7 →
             left column (reversed) 4. The interior element 5 is skipped.
```

### Example 2

```
Input:  matrix = [[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]]
Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5]
Explanation: Top row 1,2,3,4 → right column 8,12 → bottom row reversed 11,10,9 →
             left column reversed 5. Interior elements 6 and 7 are skipped.
```

### Example 3 (single row — degenerate case)

```
Input:  matrix = [[10, 20, 30]]
Output: [10, 20, 30]
Explanation: With only one row, the whole row is the boundary. The bottom-row and
             left-column sweeps must be skipped to avoid re-emitting elements.
```

## Hint

Use **Boundary / Perimeter Traversal**: track four edges (`top`, `bottom`, `left`,
`right`) and perform four directed sweeps, guarding the bottom-row and left-column
sweeps so that a single row or single column is never emitted twice.
