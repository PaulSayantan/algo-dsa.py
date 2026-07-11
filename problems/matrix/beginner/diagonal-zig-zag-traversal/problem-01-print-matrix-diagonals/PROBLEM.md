# Print Matrix Anti-Diagonals

**Difficulty:** Easy

**Source:** Classic interview / GeeksforGeeks "Diagonal traversal of matrix" (also
the natural warm-up for LeetCode 498)

## Description

Given an `m x n` integer matrix `mat`, return a flat list of all its elements read
one **anti-diagonal** at a time.

An anti-diagonal is the set of cells that run in the `/` direction — the cells
`(i, j)` for which the sum of the coordinates `i + j` is the same. Process the
diagonals in increasing order of `i + j` (so the top-left corner comes first and the
bottom-right corner comes last). Within a single diagonal, emit the cells in
increasing order of row index `i` (equivalently, top-to-bottom).

This is the *non-alternating* version of diagonal traversal: every diagonal is read
in the same direction. It is the foundation you build the zig-zag version on top of.

## Constraints

- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 100`
- `-10^5 <= mat[i][j] <= 10^5`

## Examples

### Example 1

```
Input:  mat = [[1,2,3],
               [4,5,6],
               [7,8,9]]
Output: [1,2,4,3,5,7,6,8,9]
```

**Explanation:** The diagonals grouped by `i + j` are:
`i+j=0 -> [1]`, `i+j=1 -> [2,4]`, `i+j=2 -> [3,5,7]`, `i+j=3 -> [6,8]`,
`i+j=4 -> [9]`. Reading each diagonal top-to-bottom and concatenating gives
`[1, 2,4, 3,5,7, 6,8, 9]`.

### Example 2

```
Input:  mat = [[1,2],
               [3,4]]
Output: [1,2,3,4]
```

**Explanation:** Diagonals are `[1]`, `[2,3]`, `[4]`. The middle diagonal is read
top-to-bottom as `2` then `3`, producing `[1, 2, 3, 4]`.

### Example 3

```
Input:  mat = [[1,2,3,4]]
Output: [1,2,3,4]
```

**Explanation:** A single row. Each diagonal contains exactly one element, so the
output is just the row itself.

## Hint

Use **Diagonal / Zig-Zag Traversal**: notice that all cells on one anti-diagonal
share the same value of `i + j`. Iterate the diagonal id `d` from `0` to
`m + n - 2`, and for each `d` collect the valid cells.
