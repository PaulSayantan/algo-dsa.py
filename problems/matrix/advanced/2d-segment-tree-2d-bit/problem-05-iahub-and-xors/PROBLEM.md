# Iahub and Xors

**Difficulty:** Hard

**Source:** Codeforces 341D — "Iahub and Xors"

## Description

Iahub has an `n x n` matrix, **1-indexed**, initially all zeros. He must process
`m` operations of two kinds:

- `1 x0 y0 x1 y1` — **query**: output the XOR of all values `a[i][j]` for
  `x0 <= i <= x1` and `y0 <= j <= y1` (an inclusive submatrix).
- `2 x0 y0 x1 y1 v` — **update**: XOR the value `v` into every cell of that same
  submatrix, i.e. `a[i][j] ^= v` for all `x0 <= i <= x1`, `y0 <= j <= y1`.

Process the operations in order and print each query's result.

This is a **range-update, range-query** problem where the aggregate is **XOR**.
XOR is its own inverse, which is exactly the property that lets a Fenwick-based
solution work — but a naive per-cell update is `O(n²)` per op and far too slow.

## Constraints

- `1 <= n <= 1000`
- `1 <= m <= 10^5`
- `1 <= x0 <= x1 <= n`, `1 <= y0 <= y1 <= n`
- `0 <= v < 2^62`
- Coordinates are 1-indexed.

## Examples

### Example 1

```
Input:
3 5
2 1 1 2 2 1
2 1 3 2 3 2
2 3 1 3 3 3
1 2 2 3 3
1 2 2 3 2

Output:
3
2
```

**Explanation:**
After the three updates the matrix is
```
1 1 2
1 1 2
3 3 3
```
- `1 2 2 3 3` — XOR of the submatrix rows 2..3, cols 2..3 =
  `1 ^ 2 ^ 3 ^ 3 = 3`.
- `1 2 2 3 2` — XOR of rows 2..3, col 2 = `1 ^ 3 = 2`.

### Example 2

```
Input:
2 3
2 1 1 2 2 5
1 1 1 2 2
1 1 1 1 1

Output:
0
5
```

**Explanation:**
- Update XORs `5` into every cell of the `2 x 2` matrix, giving all cells `= 5`.
- `1 1 1 2 2` — XOR over all four cells = `5 ^ 5 ^ 5 ^ 5 = 0` (even count
  cancels).
- `1 1 1 1 1` — a single cell `(1,1) = 5`.

## Hint

Use a **2D Binary Indexed Tree in range-update / range-query mode**, adapted for
XOR. The classic sum version keeps **four** BITs keyed by index parity; for XOR
the four buckets are keyed by the **parity of `x` and `y`**, because a cell's
contribution to a prefix XOR flips only over parity-dependent index counts.
