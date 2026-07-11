# Search a 2D Matrix

**Difficulty:** Medium

**Source:** LeetCode 74 — Search a 2D Matrix

## Description

You are given an `m x n` integer matrix `matrix` with the following two properties:

1. Each row is sorted in non-decreasing order (left to right).
2. The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` if `target` is in `matrix`, and `false`
otherwise.

Because of the two properties above, reading the matrix row by row produces a
single sorted list of all `m * n` values. Your job is to decide membership as
efficiently as possible — the expected solution runs in `O(log(m * n))` time.

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-10^4 <= matrix[i][j] <= 10^4`
- `-10^4 <= target <= 10^4`

## Examples

### Example 1

```
Input:  matrix = [[1, 3, 5, 7],
                  [10, 11, 16, 20],
                  [23, 30, 34, 60]], target = 3
Output: true
Explanation: Reading row-major, the sequence is
             [1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60].
             The value 3 is present (row 0, column 1), so the answer is true.
```

### Example 2

```
Input:  matrix = [[1, 3, 5, 7],
                  [10, 11, 16, 20],
                  [23, 30, 34, 60]], target = 13
Output: false
Explanation: 13 would sit between 11 and 16 in the flattened sequence, but it is
             not actually present, so the answer is false.
```

### Example 3

```
Input:  matrix = [[1]], target = 1
Output: true
Explanation: A 1x1 matrix contains exactly the value 1, which equals target.
```

## Hint

Treat the whole matrix as one flat sorted array of length `m * n` and apply
**Binary Search in a Fully-Sorted Matrix**. Map a flat index `idx` back to a cell
with `matrix[idx // n][idx % n]` — no need to actually flatten the grid.
