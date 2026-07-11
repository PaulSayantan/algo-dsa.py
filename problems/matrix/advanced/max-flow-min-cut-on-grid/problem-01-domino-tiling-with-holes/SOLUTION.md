# Solution — Domino Tiling with Holes

## Brute Force

Try every subset of possible domino positions and keep the largest overlap-free subset.
There are `O(RC)` candidate domino slots and `2^(RC)` subsets, so this is exponential.
Even backtracking that places dominoes cell-by-cell is exponential in the number of empty
cells in the worst case.

- **Time:** exponential, `O(2^(RC))`.
- **Space:** `O(RC)` recursion depth.

Correct but hopeless for a `100 × 100` board.

## Optimal Approach — Bipartite Matching via Max-Flow / Min-Cut on Grid

### The key reduction

Color the board like a chessboard: `(r, c)` is **black** when `(r + c)` is even, otherwise
**white**. Every `1 × 2` domino covers two adjacent cells, and adjacent cells always have
**opposite** colors. So:

> A set of non-overlapping dominoes ⇔ a set of edges (black–white adjacencies) in which no
> cell is used twice ⇔ a **matching** in the bipartite graph `G = (Black ∪ White, E)`,
> where `E` connects each empty black cell to each adjacent empty white cell.

Maximum dominoes = **maximum matching**, which we compute as a max flow.

### Building the flow network

Nodes: a super source `S`, a super sink `T`, one node per empty black cell, one per empty
white cell.

Edges (all capacity 1):

1. `S → b` for every empty **black** cell `b`.
2. `b → w` for every empty **white** cell `w` orthogonally adjacent to `b`.
3. `w → T` for every empty **white** cell `w`.

Because every capacity out of `S` and into `T` is 1, an integral max flow saturates a set
of black cells and a disjoint set of white cells linked by matched middle edges — exactly a
matching. The **value of the max flow = number of dominoes**.

### Why it is correct

- **Integrality:** with integer capacities, augmenting-path max flow yields an integral
  flow, so each middle edge carries 0 or 1 unit — a clean matching.
- **Feasibility:** the unit capacities `S → b` and `w → T` guarantee each cell is used by
  at most one domino, matching the non-overlap rule.
- **Optimality:** by the Max-Flow Min-Cut theorem the flow is maximum, and by König's
  theorem this maximum matching is the largest possible domino set.

### Step by step

1. Read the grid; index each empty cell.
2. For each empty black cell, add `S → b` (cap 1) and, for each of its 4 neighbors that is
   empty and white, add `b → w` (cap 1).
3. For each empty white cell add `w → T` (cap 1).
4. Run a max-flow algorithm (Hopcroft–Karp, or Dinic on the unit-capacity network).
5. Return the flow value.

### Reference implementation (Hopcroft–Karp / Hungarian augmenting flavor)

```python
from typing import List

class Solution:
    def max_dominoes(self, grid: List[str]) -> int:
        R, C = len(grid), len(grid[0])
        # adj[b] = list of white cells adjacent to black cell b (both empty)
        adj = {}
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '.' and (r + c) % 2 == 0:  # black cell
                    nbrs = []
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == '.':
                            nbrs.append((nr, nc))
                    adj[(r, c)] = nbrs

        match_white = {}  # white cell -> matched black cell

        def augment(b, seen):
            for w in adj[b]:
                if w in seen:
                    continue
                seen.add(w)
                if w not in match_white or augment(match_white[w], seen):
                    match_white[w] = b
                    return True
            return False

        matches = 0
        for b in adj:
            if augment(b, set()):
                matches += 1
        return matches
```

- **Time:** `O(E · √V)` with Hopcroft–Karp / Dinic on the unit-capacity graph, where
  `V = O(RC)` and `E = O(RC)`; i.e. `O((RC)^1.5)`. The simple augmenting version above is
  `O(V · E) = O((RC)^2)` worst case, still fine for `100 × 100`.
- **Space:** `O(V + E) = O(RC)`.

## Key Insights & Edge Cases

- **Every domino is one black + one white cell** — this is the whole reason a matching
  works. Skipping the 2-coloring and matching arbitrary adjacencies would double-count.
- The answer is bounded by `min(#black empty, #white empty)`; Example 3 (5 vs 4 cells)
  hits this bound with 4.
- Build edges only from black to white so each pairing appears once; iterating all 4
  neighbors of a white cell too would create parallel reverse edges (harmless for
  correctness but wasteful).
- **Edge cases:** a board with fewer than 2 empty cells, or one whose empty cells form odd
  isolated pockets, yields fewer dominoes; an all-blocked grid returns 0.
- Grids with an odd number of empty cells can never be perfectly tiled; there is always at
  least one uncovered cell.
