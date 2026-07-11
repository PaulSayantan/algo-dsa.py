# Largest All-Zero Submatrix

**Difficulty:** Medium

**Source:** Classic interview / competitive-programming problem (the
all-`0` twin of LeetCode 85 "Maximal Rectangle", which uses `1`s).

## Description

You are given an `n x m` binary matrix `grid` whose entries are `0` or `1`.
Find the **area of the largest axis-aligned rectangle that contains only `0`s**.
The area is the number of cells in the rectangle (its height times its width).

If the matrix contains no `0` at all, the answer is `0`.

This is the canonical application of the technique: convert each row into a
histogram of "how many `0`s stack up from above", then run the largest-rectangle
subroutine on every row and keep the best.

## Constraints

- `1 <= n, m <= 200`
- `grid[i][j]` is `0` or `1`.

## Examples

### Example 1

```
Input:
grid = [[0, 0, 1],
        [0, 0, 1],
        [0, 0, 0]]
Output: 6
Explanation: The top-left 3-rows x 2-cols block (rows 0..2, columns 0..1) is all
zeros: 3 * 2 = 6. The lone zero at (2,2) cannot extend that block into a larger
rectangle because (0,2) and (1,2) are 1s.
```

### Example 2

```
Input:
grid = [[1, 0, 0],
        [0, 0, 0],
        [1, 0, 0]]
Output: 6
Explanation: Columns 1 and 2 are entirely zero across all 3 rows, forming a
3 x 2 = 6 all-zero rectangle. The zeros in column 0 are isolated by 1s.
```

### Example 3

```
Input:
grid = [[1, 1],
        [1, 1]]
Output: 0
Explanation: There are no zeros, so no all-zero rectangle exists.
```

## Hint

Use the **Largest All-Zero Submatrix** technique: build a per-row height
array where `height[j]` counts consecutive `0`s ending at the current row in
column `j` (a `1` resets it to 0), then feed each row's histogram to the
largest-rectangle-in-histogram monotonic-stack routine.
