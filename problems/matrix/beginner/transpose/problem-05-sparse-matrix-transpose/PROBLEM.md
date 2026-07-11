# Sparse Matrix Transpose

**Difficulty:** Medium

**Source:** Classic data-structures problem (Sartaj Sahni, "Data Structures, Algorithms and Applications" — sparse matrix / triplet transpose)

## Description

A **sparse matrix** (mostly zeros) is stored compactly as a list of non-zero
entries in **triplet form**: each entry is `[row, col, value]`. Given the
dimensions of the matrix and its list of triplets, return the triplets of the
**transpose** of the matrix.

The transpose swaps rows and columns, so a triplet `[r, c, v]` in the input
becomes `[c, r, v]` in the output, and an `numRows x numCols` matrix transposes
into a `numCols x numRows` matrix.

Return the output triplets sorted in **row-major order**: primarily by row
index ascending, and by column index ascending within the same row. You are
guaranteed the input triplets are given in row-major order and contain no
duplicate coordinates and no zero values.

Implement:

```python
def transpose_sparse(num_rows: int, num_cols: int,
                     triplets: List[List[int]]) -> List[List[int]]
```

## Constraints

- `1 <= num_rows, num_cols <= 10^4`
- `0 <= len(triplets) <= num_rows * num_cols` (capped so it fits in memory)
- Each triplet is `[row, col, value]` with `0 <= row < num_rows`,
  `0 <= col < num_cols`, and `value != 0`.
- Input triplets are in row-major order with distinct `(row, col)` pairs.

## Examples

### Example 1

```
Input:  num_rows = 3, num_cols = 4,
        triplets = [[0,2,5],[1,0,3],[2,1,2],[2,3,1]]
Output: [[0,1,3],[1,2,2],[2,0,5],[3,2,1]]
```

**Explanation:** The dense matrix is
```
0 0 5 0
3 0 0 0
0 2 0 1
```
Its transpose is a 4x3 matrix
```
0 3 0
0 0 2
5 0 0
0 0 1
```
Swapping each triplet's row and column gives `[2,0,5]->[0,2,5]`... then sorting
in row-major order yields `[[0,1,3],[1,2,2],[2,0,5],[3,2,1]]`.

### Example 2

```
Input:  num_rows = 2, num_cols = 2, triplets = [[0,1,7],[1,0,9]]
Output: [[0,1,9],[1,0,7]]
```

**Explanation:** The dense matrix `[[0,7],[9,0]]` transposes to `[[0,9],[7,0]]`.
Triplet `[0,1,7]` becomes `[1,0,7]` and `[1,0,9]` becomes `[0,1,9]`; sorted in
row-major order the output is `[[0,1,9],[1,0,7]]`.

### Example 3

```
Input:  num_rows = 3, num_cols = 3, triplets = []
Output: []
```

**Explanation:** An all-zero matrix has no non-zero entries, so its transpose
also has none.

## Hint

Swapping row and column indices in each triplet is the **Transpose** operation.
Producing the output already sorted in row-major order (without a full
comparison sort) is a counting-sort-style refinement worth thinking about.
