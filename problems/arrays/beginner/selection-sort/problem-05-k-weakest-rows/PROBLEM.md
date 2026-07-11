# The K Weakest Rows in a Matrix

**Difficulty:** Medium

**Source:** LeetCode 1337 — "The K Weakest Rows in a Matrix".

## Description

You are given an `m x n` binary matrix `mat` of `1`s (representing soldiers) and `0`s (representing
civilians). The soldiers are positioned in front of the civilians — that is, in each row **all the
`1`s appear to the left of all the `0`s**.

A row `i` is **weaker** than a row `j` if one of the following is true:

- The number of soldiers in row `i` is **less** than the number of soldiers in row `j`, or
- Both rows have the **same** number of soldiers and `i < j` (the smaller index is weaker).

Return the **indices** of the `k` weakest rows in the matrix, ordered from weakest to strongest.

The intended approach: compute each row's `(soldier_count, index)` key, then use a **partial
Selection Sort** to pull out the `k` smallest keys — you only need `k` passes, not a full sort.

## Constraints

- `m == mat.length`
- `n == mat[i].length`
- `2 <= n, m <= 100`
- `1 <= k <= m`
- `matrix[i][j]` is either `0` or `1`.
- In each row, all `1`s appear before all `0`s.

## Examples

### Example 1

```
Input:  mat = [[1,1,0,0,0],
               [1,1,1,1,0],
               [1,0,0,0,0],
               [1,1,0,0,0]],
        k = 3
Output: [2, 0, 3]
```

**Explanation:** Soldier counts per row are `row0=2, row1=4, row2=1, row3=2`. Ordering by
`(count, index)` ascending gives `row2 (1), row0 (2), row3 (2), row1 (4)`. The 3 weakest are
`[2, 0, 3]`. Rows 0 and 3 tie on count `2`, so the smaller index (0) comes first.

### Example 2

```
Input:  mat = [[1,0,0,0],
               [1,1,1,1],
               [1,0,0,0],
               [1,0,0,0]],
        k = 2
Output: [0, 2]
```

**Explanation:** Counts are `row0=1, row1=4, row2=1, row3=1`. Ascending by `(count, index)`:
`row0 (1,0), row2 (1,2), row3 (1,3), row1 (4,1)`. The 2 weakest are `[0, 2]`.

### Example 3

```
Input:  mat = [[1,1],
               [1,0]],
        k = 1
Output: [1]
```

**Explanation:** Counts are `row0=2, row1=1`. Row 1 has fewer soldiers, so it is the single weakest
row: `[1]`.

## Hint

Reduce each row to a `(soldier_count, row_index)` pair. Then apply **Selection Sort** for just `k`
passes, each time selecting the pair that is smallest by `(count, index)`. Comparing tuples handles
the tiebreak automatically.
