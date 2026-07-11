# Count Occurrences in a Sorted Matrix

**Difficulty:** Medium

**Source:** Classic (matrix variant of "Count occurrences in a sorted array";
related to GeeksforGeeks "Count number of occurrences in a sorted array")

## Description

You are given an `m x n` integer matrix `matrix` sorted in **row-major order**:
each row is sorted in non-decreasing order and the first element of each row is
greater than or equal to the last element of the previous row. Duplicate values
are allowed, and equal values are contiguous when the matrix is read row by row.

Given an integer `target`, return the number of times `target` appears in the
matrix. Solve it in `O(log(m * n))` time.

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 500`
- `-10^9 <= matrix[i][j] <= 10^9`
- The flattened row-major sequence is non-decreasing (duplicates allowed).
- `-10^9 <= target <= 10^9`

## Examples

### Example 1

```
Input:  matrix = [[1, 1, 2],
                  [2, 2, 3]], target = 2
Output: 3
Explanation: Flattened, the array is [1, 1, 2, 2, 2, 3]. The value 2 occupies flat
             indices 2, 3, and 4 — three occurrences.
```

### Example 2

```
Input:  matrix = [[1, 1, 2],
                  [2, 2, 3]], target = 5
Output: 0
Explanation: 5 never appears in the matrix, so the count is 0.
```

### Example 3

```
Input:  matrix = [[4, 4],
                  [4, 4]], target = 4
Output: 4
Explanation: Every cell equals 4, so the flattened array is [4, 4, 4, 4] and the
             count is 4.
```

## Hint

Run **Binary Search in a Fully-Sorted Matrix** twice: find `lower_bound(target)`
(first index `>= target`) and `upper_bound(target)` (first index `> target`). The
count is `upper_bound - lower_bound`. Map flat index `idx` to
`matrix[idx // n][idx % n]`.
