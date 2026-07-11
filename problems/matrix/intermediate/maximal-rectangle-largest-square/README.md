# Maximal Rectangle / Largest Square

A family of matrix problems that all ask the same underlying question: **given a binary
grid, find (or count) the biggest all-`1` region**, where "biggest" is either the largest
axis-aligned rectangle or the largest square.

There are two workhorse techniques, and knowing when each applies is the whole game:

1. **DP for squares.** For the *largest square* of `1`s, define
   `dp[i][j]` = side length of the largest all-`1` square whose **bottom-right corner** is
   `(i, j)`. Then
   `dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1` when `matrix[i][j] == 1`.
   The three neighbors (up, left, diagonal) must *all* support at least side `k` for the
   corner to extend to side `k+1`. This same `dp` table also lets you **count** every square
   submatrix (each cell contributes `dp[i][j]` squares).

2. **Histogram + monotonic stack per row for rectangles.** For the *largest rectangle*
   (which need not be square), scan rows top to bottom and maintain, for each column, the
   number of consecutive `1`s ending at the current row (`heights[j]`). Each row is then a
   histogram, and the answer for that row is the *largest rectangle in a histogram*, solved
   in `O(cols)` with a monotonic (increasing) stack. The best over all rows is the answer.

The histogram-per-row reduction is the key trick: it turns a 2-D problem into `rows`
independent 1-D histogram problems. Variations of it also solve column-rearrangement and
rectangle-counting questions.

## Complexity at a glance

| Technique | Time | Space |
|---|---|---|
| Largest-square DP | `O(rows * cols)` | `O(cols)` with a rolling row |
| Count square submatrices (DP) | `O(rows * cols)` | `O(cols)` |
| Largest rectangle in a histogram (stack) | `O(n)` | `O(n)` |
| Maximal rectangle (histogram per row) | `O(rows * cols)` | `O(cols)` |

## Problems

| # | Problem | Technique | Difficulty |
|---|---------|-----------|------------|
| 1 | [Maximal Square](problem-01-maximal-square/PROBLEM.md) | Largest-square DP | Medium |
| 2 | [Count Square Submatrices with All Ones](problem-02-count-square-submatrices/PROBLEM.md) | Largest-square DP (summed) | Medium |
| 3 | [Largest Rectangle in Histogram](problem-03-largest-rectangle-in-histogram/PROBLEM.md) | Monotonic stack (the core subroutine) | Hard |
| 4 | [Largest Submatrix With Column Rearrangement](problem-04-largest-submatrix-with-column-rearrangement/PROBLEM.md) | Per-row heights + sort | Medium |
| 5 | [Maximal Rectangle](problem-05-maximal-rectangle/PROBLEM.md) | Histogram per row + monotonic stack | Hard |
| 6 | [Count Submatrices With All Ones](problem-06-count-submatrices-with-all-ones/PROBLEM.md) | Per-row heights + monotonic stack counting | Hard |

Suggested order: start with the square DP (1, 2), master the histogram subroutine (3),
then combine ideas for the rectangle problems (4, 5, 6).
