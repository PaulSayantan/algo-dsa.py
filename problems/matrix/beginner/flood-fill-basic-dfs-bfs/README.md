# Flood Fill (basic DFS/BFS)

**Category:** matrix / beginner

## What it is

Flood Fill is the grid analogue of the "paint bucket" tool. Starting from a
seed cell, you visit every cell that is *connected* to it (usually
4-directionally: up/down/left/right) and shares some property — the same color,
the same land/water value, or a reachability condition. Each visited cell is
recolored or marked, and the search recurses into its neighbors.

Mechanically it is just a **graph traversal** (DFS or BFS) where:

- **Nodes** = grid cells `(r, c)`.
- **Edges** = pairs of adjacent cells that satisfy a connectivity predicate
  (e.g. "same original color", "both are land").
- **Visited set** = the grid itself, mutated in place, or a separate boolean
  matrix.

The single most important invariant is: **never enqueue/recurse into a cell you
have already claimed.** In classic flood fill you avoid this by checking the
cell's current value before recursing; forgetting it (especially when the new
color equals the old color) causes infinite recursion.

## When to reach for it

- You need to identify, count, measure, or recolor a **connected region** in a
  grid or image.
- Counting connected components (islands), computing region area, capturing
  enclosed regions, or multi-source reachability from grid borders.
- Any problem phrased as "cells connected to each other by moving
  up/down/left/right that all share property X".

DFS (recursion or explicit stack) and BFS (queue) both work; the choice rarely
affects correctness. Prefer BFS (iterative) when the grid is large enough that
recursion could overflow the call stack.

## Complexity

For an `m x n` grid, flood fill visits each cell at most once and inspects a
constant number of neighbors per cell:

- **Time:** `O(m * n)`
- **Space:** `O(m * n)` worst case — the recursion/stack/queue depth can grow to
  the whole grid when it is one big region.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Flood Fill](problem-01-flood-fill/PROBLEM.md) | Canonical seed-based recolor | Easy |
| 2 | [Number of Islands](problem-02-number-of-islands/PROBLEM.md) | Count connected components | Medium |
| 3 | [Max Area of Island](problem-03-max-area-of-island/PROBLEM.md) | Region area returned by the fill | Medium |
| 4 | [Number of Enclaves](problem-04-number-of-enclaves/PROBLEM.md) | Flood from borders, count the rest | Medium |
| 5 | [Surrounded Regions](problem-05-surrounded-regions/PROBLEM.md) | Mark border-safe region, flip the rest | Medium |
| 6 | [Pacific Atlantic Water Flow](problem-06-pacific-atlantic-water-flow/PROBLEM.md) | Reverse multi-source flood, intersect | Medium/Hard |
