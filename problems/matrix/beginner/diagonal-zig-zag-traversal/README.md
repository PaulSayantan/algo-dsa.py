# Diagonal / Zig-Zag Traversal

## What it is

**Diagonal traversal** is a family of matrix-scanning techniques built on a single
observation: every cell `(i, j)` of a grid belongs to exactly one diagonal, and the
diagonal it belongs to is identified by a constant.

- **Anti-diagonals** (the `/` direction, going up-right / down-left) share the same
  value of `i + j`. In an `m x n` matrix there are `m + n - 1` of them, indexed
  `0 .. m+n-2`.
- **Main diagonals** (the `\` direction, going down-right / up-left) share the same
  value of `i - j`. There are also `m + n - 1` of them, indexed `-(n-1) .. (m-1)`.

Because the diagonal id is just an arithmetic expression of the coordinates, you can:

1. **Group** cells into buckets keyed by `i + j` or `i - j`, or
2. **Walk** a diagonal directly by repeatedly stepping `(i, j) -> (i±1, j±1)`.

**Zig-zag traversal** adds one twist: as you emit the diagonals one after another,
you *reverse the direction of every other diagonal* so that the reading order snakes
up and down (or left and right) instead of always sweeping the same way. Concretely,
for anti-diagonals you emit even-indexed diagonals bottom-to-top and odd-indexed
diagonals top-to-bottom (or vice versa).

## When to reach for it

- The problem talks about "diagonals", "anti-diagonals", or a boustrophedon /
  "snake" / "zig-zag" reading order over a grid.
- You need to sort, aggregate, or compare values that lie on the same diagonal.
- You want an order where consecutive elements are diagonal neighbors.

## Typical complexity

- **Time:** `O(m * n)` — every cell is visited exactly once (sorting variants add a
  `log` factor per diagonal).
- **Space:** `O(m + n)` for a single diagonal buffer, or `O(m * n)` for the output /
  bucket structures. The pure index-walk (compute `j = d - i`) uses only `O(1)`
  auxiliary space beyond the output.

## Core identities (memorize these)

| Direction        | Constant along diagonal | # diagonals | Index range        |
|------------------|-------------------------|-------------|--------------------|
| Anti-diagonal `/`| `i + j`                 | `m + n - 1` | `0 .. m+n-2`       |
| Main diagonal `\`| `i - j`                 | `m + n - 1` | `-(n-1) .. (m-1)`  |

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Print Matrix Anti-Diagonals](problem-01-print-matrix-diagonals/PROBLEM.md) | Group by `i + j`, emit in order | Easy |
| 2 | [Diagonal Traverse](problem-02-diagonal-traverse/PROBLEM.md) | Zig-zag: reverse alternate `i + j` diagonals | Medium |
| 3 | [Difference of Number of Distinct Values on Diagonals](problem-03-difference-of-distinct-values/PROBLEM.md) | Walk each `\` diagonal from a cell | Medium |
| 4 | [Sort the Matrix Diagonally](problem-04-sort-the-matrix-diagonally/PROBLEM.md) | Bucket by `i - j`, sort, place back | Medium |
| 5 | [Diagonal Traverse II](problem-05-diagonal-traverse-ii/PROBLEM.md) | Group by `i + j` on a *jagged* array | Medium |
