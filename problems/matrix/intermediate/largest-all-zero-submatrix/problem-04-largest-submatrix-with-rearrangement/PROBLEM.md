# Largest Submatrix With Rearrangements

**Difficulty:** Medium

**Source:** LeetCode 1727 — Largest Submatrix With Rearrangements

## Description

You are given a binary matrix `matrix` of size `m x n`. You are allowed to
**reorder the columns** of the matrix in any order, any number of times.

Return the **area of the largest submatrix within `matrix` where every element
is `1`**, after optionally reordering the columns to your advantage.

Because columns can be freely permuted, columns with tall runs of `1`s can be
grouped together — so the histogram trick changes: instead of a monotonic stack
you **sort** each row's heights.

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m * n <= 10^5`
- `matrix[i][j]` is `0` or `1`.

## Examples

### Example 1

```
Input:
matrix = [[0, 0, 1],
          [1, 1, 1],
          [1, 0, 1]]
Output: 4
Explanation: Measuring each column as consecutive 1s ending at a given row, the
bottom row's heights are [2, 0, 3]. Sorted descending they are [3, 2, 0]:
picking the two tallest columns (heights 3 and 2) side by side yields a block of
height 2 across 2 columns = area 4, the best achievable after reordering.
```

### Example 2

```
Input:
matrix = [[1, 0, 1, 0, 1]]
Output: 3
Explanation: Single row. It has three 1s; reordering the columns places them
adjacent, forming a 1 x 3 block of area 3.
```

### Example 3

```
Input:
matrix = [[1, 1, 0],
          [1, 0, 1]]
Output: 2
Explanation: Row 0 has two 1s side by side (area 2). Row 1's heights are
[2, 0, 1]; sorted descending [2, 1, 0], the best is height 2 over 1 column
(area 2) or height 1 over 2 columns (area 2). The maximum overall is 2.
```

## Hint

Use the **Largest All-Zero Submatrix** idea with a twist: compute per-column
heights of consecutive `1`s ending at each row, but since columns may be
reordered, **sort each row's heights in descending order** instead of using a
monotonic stack. The best area for that row is `max over k of heights_sorted[k]
* (k + 1)`.
