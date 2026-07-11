# Kth Smallest Element in a Sorted Matrix

**Difficulty:** Medium

**Source:** LeetCode 378 — Kth Smallest Element in a Sorted Matrix

## Description

Given an `n x n` matrix `matrix` where each of the rows and columns is sorted in
ascending order, return the **k-th smallest element** in the matrix.

Note that it is the k-th smallest element **in sorted order**, counting
duplicates — not the k-th *distinct* element.

You must find a solution with better than `O(n^2)` memory complexity (so no fully
materializing and sorting all `n^2` values).

## Constraints

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 300`
- `-10^9 <= matrix[i][j] <= 10^9`
- All the rows and columns of `matrix` are guaranteed to be sorted in
  non-decreasing order.
- `1 <= k <= n^2`

## Examples

### Example 1

```
Input:
matrix = [[ 1,  5,  9],
          [10, 11, 13],
          [12, 13, 15]]
k = 8

Output: 13
```

**Explanation:** Sorting all entries gives
`[1, 5, 9, 10, 11, 12, 13, 13, 15]`. The 8th smallest value (1-indexed) is `13`.

### Example 2

```
Input:
matrix = [[-5]]
k = 1

Output: -5
```

**Explanation:** There is only one element, and it is the 1st smallest.

### Example 3

```
Input:
matrix = [[1, 2],
          [1, 3]]
k = 2

Output: 1
```

**Explanation:** Sorted order is `[1, 1, 2, 3]`. The 2nd smallest is `1` — the
duplicate counts as its own position.

## Hint

Binary-search on the **answer value** (not on an index) between the smallest and
largest entries. For a candidate value `x`, count how many matrix entries are
`<= x` in `O(n)` using **Staircase / Saddleback Search** from the bottom-left
corner. Shrink the value range until it converges on the k-th smallest.
