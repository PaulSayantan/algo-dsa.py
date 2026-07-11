# Rotate 90° (Transpose + Reverse)

## What it is

Rotating a matrix by 90° is one of the most common matrix manipulation tasks.
Instead of moving elements one ring at a time, we decompose the rotation into two
simple, well-understood passes:

1. **Transpose** — reflect the matrix across its main diagonal, i.e. swap
   `M[i][j]` with `M[j][i]`. After this pass, columns have become rows.
2. **Reverse** — reverse each row (or reverse the order of the rows).

The direction of the rotation is decided by *which* reverse you apply:

| Goal | Recipe |
|------|--------|
| Rotate **90° clockwise** | Transpose, then reverse **each row** |
| Rotate **90° counter-clockwise** | Transpose, then reverse **the order of rows** (reverse columns) |

(Equivalently: reverse-then-transpose produces the opposite direction of
transpose-then-reverse, so several combinations work — just verify on a small
example.)

## When to reach for it

- You must rotate a square matrix (image, grid, tile) by a multiple of 90°.
- You want an **in-place** rotation for a square matrix with only O(1) extra memory.
- A problem hides a rotation inside it (simulate gravity, compare grids under
  rotation, rotate a box), and rotation is the clean sub-step.

## Complexity

- **Time:** `O(m · n)` — every element is touched a constant number of times
  (once for transpose, once for reverse). For a square `n × n` matrix that is `O(n²)`.
- **Space:** `O(1)` extra for a square in-place rotation (swaps only). For a
  non-square transpose you must allocate a new `n × m` matrix, giving `O(m · n)`.

## Why it works

Transpose sends element at `(i, j)` to `(j, i)`. Reversing each row of an
`n × n` matrix sends `(j, i)` to `(j, n-1-i)`. Composing the two maps
`(i, j) → (j, n-1-i)`, which is exactly the coordinate transform of a 90°
clockwise rotation. Because each pass is a bijection on the cells, no data is
lost and the result is a genuine rotation.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Transpose Matrix](problem-01-transpose-matrix/PROBLEM.md) | Build the transpose of an `m × n` matrix — the first half of the technique. | Easy |
| 2 | [Determine Whether Matrix Can Be Obtained By Rotation](problem-02-determine-matrix-by-rotation/PROBLEM.md) | Check if `mat` equals `target` after 0–3 rotations of 90°. | Easy |
| 3 | [Rotate Image](problem-03-rotate-image/PROBLEM.md) | Rotate an `n × n` matrix 90° clockwise in place. | Medium |
| 4 | [Rotate Matrix Counter-Clockwise](problem-04-rotate-matrix-counterclockwise/PROBLEM.md) | Rotate an `n × n` matrix 90° counter-clockwise in place. | Medium |
| 5 | [Rotating the Box](problem-05-rotating-the-box/PROBLEM.md) | Apply gravity, then rotate the box 90° clockwise. | Medium |
