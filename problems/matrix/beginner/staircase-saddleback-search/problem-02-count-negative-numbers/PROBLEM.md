# Count Negative Numbers in a Sorted Matrix

**Difficulty:** Easy

**Source:** LeetCode 1351 — Count Negative Numbers in a Sorted Matrix

## Description

Given an `m x n` matrix `grid` which is sorted in **non-increasing** order both
row-wise and column-wise (each row is sorted from largest to smallest left to
right, and each column is sorted from largest to smallest top to bottom), return
the **number of negative numbers** in `grid`.

The sorted structure means the negatives always cluster in the **bottom-right**
region of the matrix, separated from the non-negatives by a monotonic "staircase"
boundary. You are asked to count them in better than `O(m·n)` time.

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 100`
- `-100 <= grid[i][j] <= 100`
- Each row is sorted in non-increasing order.
- Each column is sorted in non-increasing order.

## Examples

### Example 1

```
Input:
grid = [[ 4,  3,  2, -1],
        [ 3,  2,  1, -1],
        [ 1,  1, -1, -2],
        [-1, -1, -2, -3]]

Output: 8
```

**Explanation:** The negative numbers are `-1` (row 0), `-1` (row 1), `-1, -2`
(row 2), and `-1, -1, -2, -3` (row 3): `1 + 1 + 2 + 4 = 8`.

### Example 2

```
Input:
grid = [[3, 2],
        [1, 0]]

Output: 0
```

**Explanation:** There are no negative numbers in the matrix.

### Example 3

```
Input:
grid = [[-1]]

Output: 1
```

**Explanation:** The single element `-1` is negative.

## Hint

The matrix is doubly sorted, so walk the boundary between negatives and
non-negatives with **Staircase / Saddleback Search**. Starting from the
bottom-left corner, each step lets you count an entire row or column of negatives
at once — total `O(m + n)`.
