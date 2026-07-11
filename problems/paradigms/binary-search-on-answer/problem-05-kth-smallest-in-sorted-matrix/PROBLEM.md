# Kth Smallest Element in a Sorted Matrix

**Difficulty:** Medium

**Source:** LeetCode 378 (Kth Smallest Element in a Sorted Matrix)

## Description

Given an `n x n` matrix where **each row and each column is sorted in ascending
order**, return the `k`-th smallest element in the matrix.

Note that it is the `k`-th smallest element **in sorted order**, counting
duplicate values separately — not the `k`-th *distinct* element.

You must find a solution with memory complexity better than `O(n^2)`.

## Constraints

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 300`
- `-10^9 <= matrix[i][j] <= 10^9`
- All rows and columns of `matrix` are sorted in non-decreasing order.
- `1 <= k <= n^2`

## Examples

### Example 1

```
Input:  matrix = [[ 1,  5,  9],
                  [10, 11, 13],
                  [12, 13, 15]], k = 8
Output: 13
```

Explanation: The elements in sorted order are
`[1, 5, 9, 10, 11, 12, 13, 13, 15]`. The `8`-th smallest (1-indexed) is `13`
(the second `13`, counted separately from the first).

### Example 2

```
Input:  matrix = [[-5]], k = 1
Output: -5
```

Explanation: The matrix has a single element, so the `1`-st smallest is `-5`.

### Example 3

```
Input:  matrix = [[1, 2], [1, 3]], k = 2
Output: 1
```

Explanation: Sorted order is `[1, 1, 2, 3]`. The `2`-nd smallest is `1` — the
duplicate value is counted separately.

## Hint

Do not sort all `n^2` elements. Instead **Binary Search on Answer** over the
*value* range `[matrix[0][0], matrix[n-1][n-1]]`. For a candidate value `v`, count
how many matrix entries are `<= v`; this count is monotonic in `v`, so you can
search for the smallest `v` whose count is at least `k`.
