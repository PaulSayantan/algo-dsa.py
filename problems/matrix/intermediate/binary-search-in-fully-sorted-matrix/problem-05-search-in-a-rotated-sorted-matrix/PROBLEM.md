# Search in a Rotated Sorted Matrix

**Difficulty:** Hard

**Source:** Classic (matrix variant of LeetCode 33 — Search in Rotated Sorted
Array)

## Description

You are given an `m x n` integer matrix `matrix` of **distinct** integers. When
the matrix is read in row-major order (row 0 left to right, then row 1, and so
on), the resulting length-`m*n` array is a **rotated sorted array**: it was
originally sorted in strictly increasing order, then rotated left at some unknown
pivot `k` (`0 <= k < m*n`). For example, a sorted flattening `[0,1,2,3,4,5,6,7,8]`
rotated by 5 becomes `[5,6,7,8,0,1,2,3,4]`.

Given an integer `target`, return its position in the matrix as a two-element list
`[row, col]`, or `[-1, -1]` if `target` is not present. Solve it in
`O(log(m * n))` time.

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 300`
- All `m * n` values are **distinct**.
- The row-major flattening is a sorted array rotated at an unknown pivot.
- `-10^4 <= matrix[i][j] <= 10^4`
- `-10^4 <= target <= 10^4`

## Examples

### Example 1

```
Input:  matrix = [[4, 5, 6],
                  [7, 8, 0],
                  [1, 2, 3]], target = 8
Output: [1, 1]
Explanation: Flattened row-major, the array is [4, 5, 6, 7, 8, 0, 1, 2, 3] — the
             sorted array [0..8] rotated left by 5. The value 8 sits at flat index
             4, i.e. row 4//3 = 1, column 4%3 = 1.
```

### Example 2

```
Input:  matrix = [[4, 5, 6],
                  [7, 8, 0],
                  [1, 2, 3]], target = 3
Output: [2, 2]
Explanation: 3 sits at flat index 8 in [4, 5, 6, 7, 8, 0, 1, 2, 3], i.e. row
             8//3 = 2, column 8%3 = 2.
```

### Example 3

```
Input:  matrix = [[4, 5, 6],
                  [7, 8, 0],
                  [1, 2, 3]], target = 10
Output: [-1, -1]
Explanation: 10 does not appear anywhere in the matrix, so the answer is
             [-1, -1].
```

## Hint

Apply **Binary Search in a Fully-Sorted Matrix**, but with the rotated-array twist
from LeetCode 33: at each `mid`, one half of the current range is still sorted —
detect which, and decide whether `target` lies inside it. Map flat index `idx` to
`matrix[idx // n][idx % n]`.
