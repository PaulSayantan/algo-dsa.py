# Count Square Submatrices with All Ones

**Difficulty:** Medium

**Source:** LeetCode 1277 — Count Square Submatrices with All Ones

## Description

Given an `m x n` matrix of `0`s and `1`s, return **how many square submatrices contain
only `1`s**.

A square submatrix is any contiguous, axis-aligned square block of cells (side length
`1, 2, 3, ...`) in which every entry is `1`. Squares of different sizes and different
positions are counted separately, so a large all-`1` region contributes many squares.

## Constraints

- `1 <= arr.length <= 300`
- `1 <= arr[0].length <= 300`
- `0 <= arr[i][j] <= 1`

## Examples

### Example 1

```
Input: matrix = [[0,1,1,1],
                 [1,1,1,1],
                 [0,1,1,1]]
Output: 15
```

**Explanation:** There are **10** squares of side 1 (one per `1` cell), **4** squares of
side 2, and **1** square of side 3. Total = `10 + 4 + 1 = 15`.

### Example 2

```
Input: matrix = [[1,0,1],
                 [1,1,0],
                 [1,1,0]]
Output: 7
```

**Explanation:** There are **6** squares of side 1 (one per `1` cell) and **1** square of
side 2 (the bottom-left 2x2 block). Total = `6 + 1 = 7`.

### Example 3

```
Input: matrix = [[0,0],
                 [0,0]]
Output: 0
```

**Explanation:** There are no `1`s, so there are no all-`1` square submatrices.

## Hint

Reuse the **Largest Square** DP: `dp[i][j]` is the side of the largest all-`1` square ending
at `(i, j)`. That value also equals the *number* of all-`1` squares whose bottom-right corner
is `(i, j)`, so summing `dp` over the whole grid gives the count.
