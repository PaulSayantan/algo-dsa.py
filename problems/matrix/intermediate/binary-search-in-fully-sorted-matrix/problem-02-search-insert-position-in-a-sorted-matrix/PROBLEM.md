# Search Insert Position in a Sorted Matrix

**Difficulty:** Medium

**Source:** Classic (matrix variant of LeetCode 35 — Search Insert Position)

## Description

You are given an `m x n` integer matrix `matrix` that is sorted in **row-major
order**: each row is sorted in non-decreasing order, and the first element of each
row is greater than or equal to the last element of the previous row. Reading the
matrix row by row therefore yields one sorted array of `m * n` values.

Given an integer `target`, return the **flat index** (a value in `[0, m*n]`) at
which `target` is found, or where it would be inserted to keep the row-major
sequence sorted. This is the classic `lower_bound`: the number of elements
strictly less than `target`, i.e. the index of the first element that is `>=
target`. If `target` is greater than every element, return `m * n`.

Do this in `O(log(m * n))` time.

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 300`
- `-10^6 <= matrix[i][j] <= 10^6`
- All values within the flattened sequence are in non-decreasing order (duplicates
  are allowed).
- `-10^6 <= target <= 10^6`

## Examples

### Example 1

```
Input:  matrix = [[1, 3, 5],
                  [6, 8, 9]], target = 5
Output: 2
Explanation: Flattened, the array is [1, 3, 5, 6, 8, 9]. The value 5 sits at flat
             index 2 (row 0, column 2), so the insert position is 2.
```

### Example 2

```
Input:  matrix = [[1, 3, 5],
                  [6, 8, 9]], target = 7
Output: 4
Explanation: 7 is not present. It belongs between 6 (index 3) and 8 (index 4), so
             it would be inserted at flat index 4 to keep the sequence sorted.
```

### Example 3

```
Input:  matrix = [[1, 3, 5],
                  [6, 8, 9]], target = 10
Output: 6
Explanation: 10 is larger than every element (there are 6 of them), so it would be
             appended at flat index 6 == m * n.
```

## Hint

Run **Binary Search in a Fully-Sorted Matrix** in its `lower_bound` form: search
for the first flat index whose value is `>= target`, mapping index `idx` to the
cell `matrix[idx // n][idx % n]`.
