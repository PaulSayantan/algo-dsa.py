# Largest All-Zero Submatrix

**Category:** matrix / intermediate

## What is this technique?

The "Largest All-Zero Submatrix" technique finds the biggest axis-aligned
rectangle made entirely of `0`s (or, symmetrically, entirely of `1`s) inside a
binary matrix — in **O(n·m)** time.

It is a two-part combination:

1. **Per-row heights (a running histogram).** Sweep the matrix top to bottom.
   For each cell keep `height[j]` = how many consecutive target cells (say `0`s)
   sit directly above and including the current cell in column `j`. A single `1`
   resets that column's height to `0`. After processing row `i`, the array
   `height[]` describes a histogram whose bars are the columns.

2. **Largest Rectangle in a Histogram (monotonic stack).** For each row's
   histogram, the largest rectangle of target cells whose *bottom* edge lies on
   that row equals the largest rectangle in that histogram. A monotonic
   (increasing) stack computes this in O(m). Take the max over all rows.

Because every cell contributes O(1) amortized work to the stack, the whole scan
is linear in the number of cells.

## When to reach for it

- You need the **largest** (by area) or you need to **count** rectangles/squares
  that are uniform (all `0` or all `1`) in a grid.
- The naive "try every rectangle" is O(n²m²) or worse and times out.
- The problem reduces to a stack of 1D histogram queries — one per row.

## Complexity

| | Cost |
|---|---|
| Time | **O(n·m)** — one pass to build heights, one linear histogram pass per row |
| Space | **O(m)** for the height array + stack (O(n·m) if you materialize a heights matrix) |

## The core subroutine

Everything here rests on **Largest Rectangle in a Histogram** solved with a
monotonic stack. Learn Problem 1 first; the rest are 2D applications of it.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Largest Rectangle in Histogram](problem-01-largest-rectangle-in-histogram/PROBLEM.md) | The 1D monotonic-stack subroutine every 2D solution calls | Medium / Hard |
| 2 | [Largest All-Zero Submatrix](problem-02-largest-all-zero-submatrix/PROBLEM.md) | Per-row heights + histogram → max area of an all-`0` rectangle | Medium |
| 3 | [Maximal Square](problem-03-maximal-square/PROBLEM.md) | Same scan, but the histogram step is capped to squares (side = min(w, h)) | Medium |
| 4 | [Largest Submatrix With Column Rearrangement](problem-04-largest-submatrix-with-rearrangement/PROBLEM.md) | Per-row heights + sort (columns may be reordered) | Medium |
| 5 | [Count Submatrices With All Ones](problem-05-count-submatrices-with-all-ones/PROBLEM.md) | Histogram + monotonic stack that *sums* contributions to count rectangles | Medium / Hard |
