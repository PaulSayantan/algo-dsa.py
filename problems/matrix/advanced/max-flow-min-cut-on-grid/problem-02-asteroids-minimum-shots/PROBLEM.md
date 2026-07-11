# Asteroids — Minimum Beam Shots

**Difficulty:** Medium

**Source:** POJ 3041 "Asteroids" (classic minimum-vertex-cover / König's theorem problem)

## Description

You command a ship on an `N × N` grid. Some cells contain an asteroid. Your weapon fires a
beam that, in a single shot, destroys **every asteroid in one entire row or one entire
column**. You may aim the beam at any row or any column, and you may fire as many times as
you like.

Return the **minimum number of shots** needed to destroy every asteroid.

Model the grid as a bipartite graph: put the `N` rows on one side, the `N` columns on the
other, and for each asteroid at `(r, c)` add an edge between row `r` and column `c`. Firing
at a row "picks" that row vertex; firing at a column picks that column vertex. Destroying
every asteroid means every edge must touch a picked vertex — a **minimum vertex cover**. By
**König's theorem**, the minimum vertex cover of a bipartite graph equals its **maximum
matching**, which a single max-flow computation delivers.

## Constraints

- `1 <= N <= 500`
- `asteroids` is a list of `[r, c]` pairs with `0 <= r, c < N`.
- No duplicate asteroid coordinates.
- `0 <= len(asteroids) <= N * N`.

## Examples

### Example 1

```
Input:
N = 3
asteroids = [[0,1],[1,0],[1,1],[1,2],[2,1]]
(grid, '#' = asteroid)
  .#.
  ###
  .#.
Output: 2
Explanation: Fire once at row 1 (destroys (1,0),(1,1),(1,2)) and once at column 1
(destroys (0,1),(1,1),(2,1)). Two shots clear the whole '+' shape. No single shot can
do it because the asteroids span two different rows and columns.
```

### Example 2

```
Input:
N = 3
asteroids = [[0,0],[0,2],[1,1],[2,0],[2,2]]
(grid)
  #.#
  .#.
  #.#
Output: 3
Explanation: The asteroids form the two diagonals meeting at the center. A maximum
matching pairs row0-col0, row1-col1, row2-col2 (size 3), so by König's theorem the
minimum cover — and thus the minimum number of shots — is 3.
```

### Example 3

```
Input:
N = 2
asteroids = []
Output: 0
Explanation: There are no asteroids, so zero shots are required.
```

## Hint

Rows and columns form the two sides of a bipartite graph, with one edge per asteroid.
The answer is the minimum vertex cover, which by König's theorem equals the maximum
matching — compute it with **Max-Flow / Min-Cut on Grid**.
