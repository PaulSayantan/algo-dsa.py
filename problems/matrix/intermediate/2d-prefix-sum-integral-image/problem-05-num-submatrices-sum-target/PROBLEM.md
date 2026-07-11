# Number of Submatrices That Sum to Target

**Difficulty:** Hard

**Source:** LeetCode 1074 — Number of Submatrices That Sum to Target

## Description

Given a `matrix` and a `target`, return the number of non-empty submatrices that
sum to `target`.

A submatrix `(x1, y1, x2, y2)` is the set of all cells `matrix[x][y]` with
`x1 <= x <= x2` and `y1 <= y <= y2`.

Two submatrices `(x1, y1, x2, y2)` and `(x1', y1', x2', y2')` are different if
they differ in any coordinate — for example, if `x1 != x1'`. Count every
distinct coordinate quadruple whose sum equals `target`.

## Constraints

- `1 <= matrix.length <= 100`
- `1 <= matrix[0].length <= 100`
- `-1000 <= matrix[i][j] <= 1000`
- `-10^8 <= target <= 10^8`

## Examples

### Example 1

```
Input: matrix = [[0, 1, 0],
                 [1, 1, 1],
                 [0, 1, 0]], target = 0
Output: 4
Explanation: The four submatrices summing to 0 are the four corner cells
(each equal to 0): (0,0,0,0), (0,2,0,2), (2,0,2,0), (2,2,2,2).
```

### Example 2

```
Input: matrix = [[1, -1],
                 [-1, 1]], target = 0
Output: 5
Explanation: The submatrices summing to 0 are: the full 2x2 matrix (sum 0),
the top row [1,-1], the bottom row [-1,1], the left column [1,-1], and the
right column [-1,1]. That is 5 submatrices.
```

### Example 3

```
Input: matrix = [[904]], target = 0
Output: 0
Explanation: The only submatrix is the single cell 904, which is not 0.
```

## Hint

Fix a pair of rows (or columns) and collapse the band between them into a 1D
array of column sums using a **2D Prefix Sum (Integral Image)** (or row-wise
prefix sums); then count 1D subarrays that sum to `target` with a hash map of
running prefix sums.
