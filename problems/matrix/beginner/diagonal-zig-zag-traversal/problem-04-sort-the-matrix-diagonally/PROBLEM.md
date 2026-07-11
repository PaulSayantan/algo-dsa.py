# Sort the Matrix Diagonally

**Difficulty:** Medium

**Source:** LeetCode 1329 — "Sort the Matrix Diagonally"

## Description

A **matrix diagonal** is a diagonal line of cells starting from some cell in either
the topmost row or leftmost column and going in the bottom-right direction (the `\`
direction) until it reaches the boundary of the matrix. For example, the matrix
diagonal starting from `mat[2][0]`, where `mat` is a `6 x 3` matrix, includes cells
`mat[2][0]`, `mat[3][1]`, and `mat[4][2]`.

Given an `m x n` matrix `mat` of integers, **sort each matrix diagonal in ascending
order** and return the resulting matrix.

All cells on one such diagonal share the same value of `i - j`; only cells within the
same diagonal are compared and reordered.

## Constraints

- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 100`
- `1 <= mat[i][j] <= 100`

## Examples

### Example 1

```
Input:  mat = [[3,3,1,1],
               [2,2,1,2],
               [1,1,1,2]]
Output: [[1,1,1,1],
         [1,2,2,2],
         [1,2,3,3]]
```

**Explanation:** Consider the main diagonal `i-j=0`: cells `mat[0][0]=3`,
`mat[1][1]=2`, `mat[2][2]=1`. Sorted ascending they become `1,2,3`, so they are
written back down the diagonal as `mat[0][0]=1`, `mat[1][1]=2`, `mat[2][2]=3`. Every
other diagonal is sorted the same way independently.

### Example 2

```
Input:  mat = [[11,25,66,1,69,7],
               [23,55,17,45,15,52],
               [75,31,36,44,58,8],
               [22,27,33,25,68,4],
               [84,28,14,11,5,50]]
Output: [[5,17,4,1,52,7],
         [11,11,25,45,8,69],
         [14,23,25,44,58,15],
         [22,27,31,36,50,66],
         [84,28,75,33,55,68]]
```

**Explanation:** Each `\` diagonal is gathered, sorted ascending, and written back.
For instance the diagonal `84,28,33,...` and every other diagonal is reordered
independently while cells stay on their own diagonal.

### Example 3

```
Input:  mat = [[1]]
Output: [[1]]
```

**Explanation:** A single cell is a diagonal of length 1, already sorted.

## Hint

Use **Diagonal / Zig-Zag Traversal**: bucket every cell by the constant `i - j`,
sort each bucket, then write the sorted values back down each diagonal.
