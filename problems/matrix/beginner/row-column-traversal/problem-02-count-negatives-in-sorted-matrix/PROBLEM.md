# Count Negative Numbers in a Sorted Matrix

**Difficulty:** Easy

**Source:** LeetCode 1351 — Count Negative Numbers in a Sorted Matrix

## Description

Given an `m x n` matrix `grid` which is sorted in **non-increasing order** both
row-wise and column-wise (each row reads from largest to smallest left to right, and
each column reads from largest to smallest top to bottom), return the number of
**negative** numbers in `grid`.

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 100`
- `-100 <= grid[i][j] <= 100`

## Examples

### Example 1

```
Input:  grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
```

**Explanation:** There are 8 negative numbers in the matrix: `-1, -1, -1, -2, -1, -1,
-2, -3`.

### Example 2

```
Input:  grid = [[3,2],[1,0]]
Output: 0
```

**Explanation:** No value in the matrix is negative.

### Example 3

```
Input:  grid = [[-1]]
Output: 1
```

**Explanation:** The single cell holds `-1`, which is negative, so the count is 1.

## Hint

Use **Row/Column Traversal**: scan every cell with a nested row-then-column loop and
increment a counter whenever the value is less than 0. (The sorted structure enables a
faster staircase search, but the plain traversal already meets the constraints.)
