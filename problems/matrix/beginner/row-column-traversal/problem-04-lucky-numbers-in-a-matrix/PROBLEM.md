# Lucky Numbers in a Matrix

**Difficulty:** Easy

**Source:** LeetCode 1380 — Lucky Numbers in a Matrix

## Description

Given an `m x n` matrix of **distinct** numbers, return all **lucky numbers** in the
matrix in any order.

A **lucky number** is an element of the matrix such that it is the **minimum element in
its row** and, at the same time, the **maximum element in its column**.

## Constraints

- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 50`
- `1 <= mat[i][j] <= 10^5`
- All elements in the matrix are **distinct**.

## Examples

### Example 1

```
Input:  mat = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
```

**Explanation:** 15 is the minimum of its row (`15, 16, 17`) and the maximum of its
column (column 0 is `3, 9, 15`, whose max is 15). So 15 is the only lucky number.

### Example 2

```
Input:  mat = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
```

**Explanation:** 12 is the minimum of its row (`15, 16, 17, 12`) and the maximum of its
column (`2, 7, 12`). So 12 is the only lucky number.

### Example 3

```
Input:  mat = [[7,8],[1,2]]
Output: [7]
```

**Explanation:** 7 is the minimum of its row (`7, 8`) and the maximum of its column
(`7, 1`), so it is lucky. 1 is a row minimum but not a column maximum (its column is
`8, 2`), so it is not lucky.

## Hint

Use **Row/Column Traversal**: in one pass collect the minimum of every row, in another
pass collect the maximum of every column, then report any value present in both sets.
