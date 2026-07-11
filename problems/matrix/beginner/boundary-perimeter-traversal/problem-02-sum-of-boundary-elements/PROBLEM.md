# Sum of Boundary Elements of a Matrix

**Difficulty:** Easy

**Source:** Classic matrix warm-up (GeeksforGeeks — "Sum of boundary elements of a matrix")

## Description

Given an `m x n` integer matrix, return the **sum of all boundary (perimeter)
elements** — the elements in the first row, the last row, the first column, and the
last column. Interior elements are excluded.

The catch is **not to double-count the four corner cells**, each of which belongs to two
sides at once. For a matrix with `m > 1` and `n > 1`, exactly `2*(m + n) - 4` distinct
cells contribute to the sum.

## Constraints

- `1 <= m, n <= 1000`
- `-10^4 <= matrix[i][j] <= 10^4`
- The matrix is rectangular.

## Examples

### Example 1

```
Input:  matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
Output: 40
Explanation: Boundary elements are 1,2,3,4,6,7,8,9 (everything except the interior 5).
             1+2+3+4+6+7+8+9 = 40.
```

### Example 2

```
Input:  matrix = [[1, 1, 1, 1],
                  [1, 9, 9, 1],
                  [1, 1, 1, 1]]
Output: 10
Explanation: The border is all 1s: there are 2*(3+4)-4 = 10 boundary cells, each equal
             to 1, so the sum is 10. The two interior 9s are not counted.
```

### Example 3 (single row — corners must not be double-counted differently)

```
Input:  matrix = [[5, 6, 7]]
Output: 18
Explanation: A single row is entirely boundary. 5+6+7 = 18. Naively adding "first
             column + last column + first row + last row" would over-count, so the
             degenerate shape must be handled carefully.
```

## Hint

Use **Boundary / Perimeter Traversal**: sum the top and bottom rows fully, then sum only
the *interior* of the left and right columns (excluding the corner rows already added),
guarding for single-row and single-column matrices so nothing is added twice.
