# Broken-Profile / Plug DP (bitmask over columns)

Broken-profile DP (also called **plug DP** or the "connection/contour" method) is a
dynamic-programming technique for counting or optimizing over **tilings and connected
structures on a grid**. Instead of processing the grid a whole row at a time, you sweep
it **cell by cell** and carry a **bitmask "profile"** describing the boundary between the
cells you have already decided and the cells you have not.

## The core idea

Sweep the `n × m` grid in row-major order. Between the processed and unprocessed cells
lies a jagged frontier (the *broken profile*). It touches exactly `m` columns, so a
single integer with `m` bits fully describes it:

- **bit `j` = 1** means the cell just *ahead* of the frontier in column `j` is already
  occupied — a piece placed earlier "plugs" into the current row.
- **bit `j` = 0** means that cell is still empty and must be filled by a piece anchored
  at or after the current cell.

At each cell you branch over the legal ways to cover it (leave it to a vertical domino
that reaches down, start a horizontal domino, place a tromino, etc.), updating the mask.
Because the whole future depends *only* on the profile, states collapse and the DP is
polynomial in the number of cells and exponential only in the (small) width.

## When to reach for it

- Counting **domino / tromino / polyomino tilings** of a grid (the classic *Parquet* and
  *Mondriaan's Dream* problems).
- Placing the **maximum** number of pieces, or optimizing a weighted objective, on a grid
  with blocked cells.
- Any grid problem where a decision in one cell only constrains its immediate neighbors,
  so a one-cell-thick moving boundary captures all needed state.
- Rule of thumb: use it when one grid dimension is small (roughly `min(n, m) ≤ 16-20`).
  Always sweep so the profile spans the **smaller** dimension.

## Complexity

For an `n × m` grid, sweeping cell by cell with a width-`min(n,m)` profile:

- **Time:** `O(n · m · 2^min(n,m))` — each of the `n·m` cells processes up to `2^m` masks
  with `O(1)` transitions.
- **Space:** `O(2^min(n,m))` — two rolling layers of the profile table.

(The alternative "row profile" broadcasting formulation is `O(n · 2^m · 2^m)` in the
naive form; the cell-by-cell broken-profile sweep above is the sharper, standard version.)

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Tiling a 2×N Board](problem-01-tiling-a-2xn-board/PROBLEM.md) | Count domino tilings of a 2×N strip; the gentlest broken-profile sweep. | Easy |
| 2 | [Domino and Tromino Tiling](problem-02-domino-and-tromino-tiling/PROBLEM.md) | LeetCode 790: count 2×N tilings using dominoes **and** L-trominoes, mod 1e9+7. | Medium |
| 3 | [Mondriaan's Dream (N×M domino count)](problem-03-mondriaans-dream-nxm-domino-count/PROBLEM.md) | Count all domino tilings of a full N×M board; the canonical plug-DP exercise. | Medium |
| 4 | [Parquet Tiling with Holes](problem-04-parquet-tiling-with-holes/PROBLEM.md) | Count domino tilings of an N×M board that has blocked cells. | Hard |
| 5 | [Maximum Dominoes on a Grid](problem-05-maximum-dominoes-on-a-grid/PROBLEM.md) | Place the maximum number of dominoes on a grid with obstacles (optimization variant). | Hard |
