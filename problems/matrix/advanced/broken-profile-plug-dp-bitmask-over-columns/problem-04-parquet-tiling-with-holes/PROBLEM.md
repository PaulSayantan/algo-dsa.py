# Parquet Tiling with Holes

**Difficulty:** Hard

*Classic "Parquet" broken-profile problem (SPOJ GNY07H / e-maxx "broken profile" with obstacles); a direct generalization of Mondriaan's Dream to boards with blocked cells.*

## Description

A parquet floor is an `n × m` grid, but some cells are **broken** (holes) and must **not** be
covered. Given the grid with holes marked, count the number of ways to tile every **free**
cell using `1 × 2` dominoes (placed horizontally or vertically). Broken cells are left
uncovered; free cells must all be covered exactly once; dominoes may not overlap, cover a
hole, or stick out of the board.

You are given the grid as a list of strings of equal length: `'.'` marks a free cell and
`'#'` marks a hole. Return the number of complete tilings of the free region.

If the number of free cells is odd, or the free region simply cannot be perfectly tiled,
the answer is `0`.

## Constraints

- `1 <= n, m <= 12`
- Each row string has length `m`; each character is `'.'` (free) or `'#'` (hole).
- The answer fits in a 64-bit signed integer for boards up to `12 × 12`.
- Build the profile over the smaller dimension for efficiency.

## Examples

### Example 1
```
Input:  grid = ["....",
                 "....",
                 "....",
                 "...."]
Output: 36
Explanation: With no holes this is a plain 4×4 board, which has 36 domino tilings.
```

### Example 2
```
Input:  grid = ["##..",
                 "....",
                 "....",
                 "...."]
Output: 18
Explanation: The two top-left cells (0,0) and (0,1) are holes. The remaining 14 free cells
can be perfectly tiled in 18 distinct ways.
```

### Example 3
```
Input:  grid = ["#...",
                 "....",
                 "...#"]
Output: 5
Explanation: A 3×4 board (12 cells) with holes at (0,0) and (2,3), leaving 10 free cells.
There are 5 ways to tile the free region with dominoes.
```

### Example 4
```
Input:  grid = ["#...",
                 "....",
                 "....",
                 "...#"]
Output: 0
Explanation: The classic "mutilated board" argument. Removing two same-colored corners of a
4×4 checkerboard leaves 8 black and 6 white cells (or vice versa); each domino covers one of
each color, so a perfect tiling is impossible and the count is 0.
```

## Hint

Use **Broken-Profile / Plug DP (bitmask over columns)**. Run the same cell-by-cell sweep as
the hole-free count, but treat a broken cell as "already occupied": you neither place a piece
on it nor let a vertical domino from above land on it. The width-`min(n,m)` profile is
unchanged; only the per-cell transition gains a "skip the hole" branch.
