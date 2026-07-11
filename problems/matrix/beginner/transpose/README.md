# Transpose

**Transpose** is the operation of flipping a matrix over its main diagonal:
every element `m[i][j]` is swapped with `m[j][i]`. Rows become columns and
columns become rows. For an `m x n` matrix the result is an `n x m` matrix
whose entry at `(i, j)` equals the original entry at `(j, i)`.

```
original            transpose
1 2 3               1 4
4 5 6      ->        2 5
                     3 6
```

## When to reach for it

- You need to turn **row access into column access** (or vice-versa) — e.g.
  summing/scanning columns is awkward, so transpose and scan rows instead.
- You are asked to **rotate a matrix by 90°**. Rotation is just a transpose
  composed with a row/column reversal, and this is the cleanest in-place trick.
- You need to test a structural property such as **symmetry** (a matrix is
  symmetric iff it equals its own transpose).
- You are converting between **row-major and column-major** layouts, or
  transposing a **sparse** representation.

## Complexity

- **Time:** `O(m * n)` — every element is visited a constant number of times.
- **Space:**
  - Out-of-place (build a new `n x m` matrix): `O(m * n)` extra space.
  - In-place (square matrix only): `O(1)` extra space by swapping across the
    diagonal, iterating only the upper triangle (`j > i`).

> In-place transpose is only straightforward for **square** matrices. For a
> rectangular matrix the shape changes (`m x n -> n x m`), so you must allocate
> a new matrix (or use a non-trivial cycle-following algorithm).

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Transpose Matrix](problem-01-transpose-matrix/PROBLEM.md) | Return the transpose of a (possibly rectangular) matrix. | Easy |
| 2 | [Symmetric Matrix Check](problem-02-symmetric-matrix-check/PROBLEM.md) | Decide whether a square matrix equals its own transpose. | Easy |
| 3 | [Rotate Image (90° Clockwise)](problem-03-rotate-image-clockwise/PROBLEM.md) | Rotate a square matrix 90° clockwise in place. | Medium |
| 4 | [Rotate Image (90° Counterclockwise)](problem-04-rotate-image-counterclockwise/PROBLEM.md) | Rotate a square matrix 90° counterclockwise in place. | Medium |
| 5 | [Sparse Matrix Transpose](problem-05-sparse-matrix-transpose/PROBLEM.md) | Transpose a matrix stored in compressed triplet form. | Medium |
