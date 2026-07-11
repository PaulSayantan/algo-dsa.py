# Mondriaan's Dream — Count Domino Tilings of an N×M Board

**Difficulty:** Medium

*Classic competitive-programming problem — POJ 2411 / UVa 10359 "Mondriaan's Dream"; also the AtCoder/e-maxx "broken profile" reference problem.*

## Description

Squares and rectangles fascinated the famous Dutch painter Piet Mondriaan. One night, after
producing the drawings in his "toilet series", he dreamt of filling a large rectangle with
small rectangles of width 2 and height 1 (`2 × 1` dominoes) in varied ways.

Given the dimensions of the large rectangle — `n` rows and `m` columns — count the number
of distinct ways to **completely tile** it using `1 × 2` dominoes. Each domino may be placed
horizontally or vertically, tiles must not overlap, and none may stick out of the board.

Two tilings are different if any cell is paired with a different neighbor.

For `n = 0` and `m = 0` there is exactly one (empty) tiling. If `n · m` is odd, the board
cannot be tiled and the answer is `0`.

## Constraints

- `1 <= n, m <= 12`
- The answer fits in a 64-bit signed integer for boards up to `12 × 12`.
- You may assume the profile is built over the smaller dimension (`min(n, m) <= 12`).

## Examples

### Example 1
```
Input:  n = 2, m = 2
Output: 2
Explanation: Two vertical dominoes, or two horizontal dominoes stacked. That is 2 tilings.
```

### Example 2
```
Input:  n = 3, m = 3
Output: 0
Explanation: A 3×3 board has 9 cells (odd). A domino covers 2 cells, so no perfect tiling
exists and the count is 0.
```

### Example 3
```
Input:  n = 4, m = 4
Output: 36
Explanation: There are 36 distinct ways to tile the 4×4 board with 1×2 dominoes.
```

### Example 4
```
Input:  n = 3, m = 4
Output: 11
Explanation: The 3×4 board (12 cells) has 11 distinct domino tilings.
```

### Example 5
```
Input:  n = 8, m = 8
Output: 12988816
Explanation: The full 8×8 chessboard has 12,988,816 domino tilings — a classic result.
```

## Hint

Use **Broken-Profile / Plug DP (bitmask over columns)**. Sweep the grid cell by cell in
row-major order and keep a width-`m` bitmask: bit `j` says whether the cell about to be
processed in column `j` is already occupied by a vertical domino reaching in from the row
above. Orient the sweep so the profile spans the smaller dimension.
