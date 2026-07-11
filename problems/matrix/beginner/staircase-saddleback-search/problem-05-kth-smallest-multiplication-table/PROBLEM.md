# Kth Smallest Number in a Multiplication Table

**Difficulty:** Hard

**Source:** LeetCode 668 — Kth Smallest Number in a Multiplication Table

## Description

Nearly everyone has used the multiplication table. The multiplication table of
size `m x n` is an integer matrix `mat` where `mat[i][j] == i * j`
(**1-indexed**, so `i` ranges over `1..m` and `j` over `1..n`).

Given three integers `m`, `n`, and `k`, return the **k-th smallest element** in
the `m x n` multiplication table (counting duplicates in sorted order).

The catch: `m` and `n` can be up to `3 * 10^4`, so the table has up to `9 * 10^8`
entries — far too many to build or sort. But the table is a doubly-sorted matrix
that you never need to materialize: `mat[i][j] = i * j` is available on demand.

## Constraints

- `1 <= m, n <= 3 * 10^4`
- `1 <= k <= m * n`

## Examples

### Example 1

```
Input: m = 3, n = 3, k = 5

Output: 3
```

**Explanation:** The 3x3 multiplication table is

```
1  2  3
2  4  6
3  6  9
```

Sorted in order: `[1, 2, 2, 3, 3, 4, 6, 6, 9]`. The 5th smallest value is `3`.

### Example 2

```
Input: m = 2, n = 3, k = 6

Output: 6
```

**Explanation:** The 2x3 table is

```
1  2  3
2  4  6
```

Sorted: `[1, 2, 2, 3, 4, 6]`. The 6th (largest here) value is `6`.

### Example 3

```
Input: m = 1, n = 5, k = 4

Output: 4
```

**Explanation:** The single-row table is `1 2 3 4 5`; the 4th smallest is `4`.

## Hint

The table is implicitly sorted along both dimensions but is far too large to
build. Binary-search on the **answer value** in `[1, m*n]`; for a candidate `x`,
count how many table entries are `<= x`. That count is itself a **Staircase /
Saddleback Search** over the implicit grid — for each row `i`, `min(x // i, n)`
entries are `<= x`, which is the same row-by-row elimination done in closed form.
