# Domino Tiling with Holes

**Difficulty:** Medium

**Source:** Classic (UVa 11419 / CSES "Chessboard and Queens" family, textbook bipartite-matching problem)

## Description

You are given an `R × C` grid. Each cell is either empty (`'.'`) or blocked (`'#'`).
You want to place as many `1 × 2` **dominoes** as possible. Each domino covers exactly
two orthogonally adjacent **empty** cells (horizontally or vertically). No two dominoes
may overlap, and no domino may cover a blocked cell.

Return the **maximum number of dominoes** that can be placed.

The trick is that this is exactly a **maximum bipartite matching**. Color the grid like a
chessboard: cell `(r, c)` is *black* if `(r + c)` is even, otherwise *white*. Every domino
covers exactly one black and one white cell, so dominoes correspond one-to-one with a set
of edges that never reuse a cell — a matching between the black empty cells and the white
empty cells.

## Constraints

- `1 <= R, C <= 100`
- Each cell of `grid` is either `'.'` (empty) or `'#'` (blocked).
- A domino must lie entirely on empty cells.

## Examples

### Example 1

```
Input:
grid = [
  "...",
  "..."
]
Output: 3
Explanation: A 2×3 board of 6 empty cells can be perfectly tiled by 3 dominoes
(e.g. three vertical dominoes), leaving no cell uncovered.
```

### Example 2

```
Input:
grid = [
  ".#",
  ".."
]
Output: 1
Explanation: The empty cells are (0,0), (1,0), (1,1) — a chain of three cells.
Any placement covers two of them with one domino and leaves the third exposed,
so at most 1 domino fits.
```

### Example 3

```
Input:
grid = [
  "...",
  "...",
  "..."
]
Output: 4
Explanation: A 3×3 board has 9 empty cells. The chessboard coloring gives 5 cells of
one color and 4 of the other, so a matching can pair at most 4 cells with the other
side: at most 4 dominoes, leaving exactly one cell uncovered.
```

## Hint

Two-color the board and build a bipartite graph between black and white empty cells;
the answer is a maximum matching. Solve it with **Max-Flow / Min-Cut on Grid** (a unit
source into every black cell, a unit sink out of every white cell).
