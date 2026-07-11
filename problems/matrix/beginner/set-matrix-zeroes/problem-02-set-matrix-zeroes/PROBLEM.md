# Set Matrix Zeroes

**Difficulty:** Medium

**Source:** LeetCode 73 — Set Matrix Zeroes

## Description

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its **entire
row and entire column** to `0`. You must do it **in place**.

The naive way is to record every `(row, col)` that contains a zero and then zero
out those lines. But if you do this while scanning the matrix, the zeros you
write will trigger *more* rows and columns to be zeroed — a chain reaction that
wipes the whole matrix. The interesting version asks you to solve it using only
`O(1)` extra space: instead of allocating separate `rowZero[]` and `colZero[]`
arrays, reuse the matrix's **first row and first column** as those flag arrays.

## Constraints

- `m == matrix.length`
- `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-2^31 <= matrix[i][j] <= 2^31 - 1`

## Examples

### Example 1

```
Input:  matrix = [[1,1,1],
                  [1,0,1],
                  [1,1,1]]
Output: [[1,0,1],
         [0,0,0],
         [1,0,1]]
```

**Explanation:** The single `0` sits at row 1, column 1. Its entire row (row 1)
and entire column (column 1) become `0`; every other cell is untouched.

### Example 2

```
Input:  matrix = [[0,1,2,0],
                  [3,4,5,2],
                  [1,3,1,5]]
Output: [[0,0,0,0],
         [0,4,5,0],
         [0,3,1,0]]
```

**Explanation:** Zeros appear at `(0,0)` and `(0,3)`. Columns 0 and 3 and row 0
are all zeroed. The remaining cells `(1,1)=4`, `(1,2)=5`, `(2,1)=3`, `(2,2)=1`
have no zero in their row or column, so they keep their values.

### Example 3

```
Input:  matrix = [[1,2,3]]
Output: [[1,2,3]]
```

**Explanation:** A single row with no zeros. Nothing changes.

## Hint

This is the canonical **Set Matrix Zeroes** technique: use the matrix's own
first row and first column as the `rowZero`/`colZero` flag storage. Track
whether the first row and first column themselves must be zeroed with two
scalar booleans, and process the outer row/column last so their flags are not
clobbered prematurely.
