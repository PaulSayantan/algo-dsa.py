# Solution — Asteroids — Minimum Beam Shots

## Brute Force

Each shot is a choice of a row or a column. There are `2N` possible shots, and we must pick
a subset that covers every asteroid. Trying all `2^(2N)` subsets and checking coverage is
exponential. Greedy heuristics ("always shoot the line with the most asteroids") are
appealing but **incorrect** — greedy can be forced into suboptimal covers.

- **Time:** `O(2^(2N) · A)` where `A` is the number of asteroids.
- **Space:** `O(N)`.

## Optimal Approach — Min Vertex Cover via Max-Flow / Min-Cut on Grid

### The reduction

Build a bipartite graph:

- Left vertices = rows `0 … N-1`.
- Right vertices = columns `0 … N-1`.
- One edge `(r, c)` for **each asteroid** at position `(r, c)`.

A shot at row `r` "selects" the left vertex `r`; a shot at column `c` selects the right
vertex `c`. Destroying every asteroid means: **for every edge, at least one endpoint is
selected.** That is precisely a **vertex cover**. Minimum shots = **minimum vertex cover**.

### König's theorem closes the loop

For a bipartite graph:

> minimum vertex cover size = maximum matching size.

So compute a **maximum bipartite matching** — via max flow — and its size is the answer.

### Flow network

- Super source `S`, super sink `T`.
- `S → r` (cap 1) for every row `r`.
- `r → c` (cap 1) for every asteroid `(r, c)`.
- `c → T` (cap 1) for every column `c`.

Max flow = maximum matching = minimum vertex cover = minimum shots.

### Why it is correct

- **König's theorem** guarantees the numeric equality of max matching and min cover for
  bipartite graphs (the graph here is bipartite by construction: edges only go
  row → column).
- **Integral max flow** on unit capacities yields a valid matching, and Max-Flow Min-Cut
  guarantees it is maximum.
- If you also need the *actual* rows/columns to shoot (not just the count), recover them
  from the min cut: run BFS from `S` in the residual graph; a standard König construction
  picks unreached left vertices plus reached right vertices.

### Step by step

1. Create adjacency: for each asteroid `(r, c)`, append `c` to `adj[r]`.
2. Run Kuhn's / Hopcroft–Karp augmenting-path matching from every row vertex.
3. Return the number of successful augmentations.

### Reference implementation (Kuhn's augmenting paths)

```python
from typing import List

class Solution:
    def min_shots(self, n: int, asteroids: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]           # row -> list of columns
        for r, c in asteroids:
            adj[r].append(c)

        match_col = [-1] * n                   # column -> matched row

        def try_kuhn(r, visited):
            for c in adj[r]:
                if not visited[c]:
                    visited[c] = True
                    if match_col[c] == -1 or try_kuhn(match_col[c], visited):
                        match_col[c] = r
                        return True
            return False

        matching = 0
        for r in range(n):
            if adj[r]:
                if try_kuhn(r, [False] * n):
                    matching += 1
        return matching
```

- **Time:** `O(V · E) = O(N · A)` for Kuhn's; `O(E · √V) = O(A · √N)` for Hopcroft–Karp /
  Dinic. Both handle `N = 500` easily.
- **Space:** `O(N + A)`.

## Key Insights & Edge Cases

- The bipartite sides are **rows and columns**, not cells — a common modeling mistake is to
  make one vertex per asteroid, which loses the "one shot clears a whole line" structure.
- **König's theorem is the crux:** minimum vertex cover is NP-hard in general graphs, but
  bipartite structure makes it equal to max matching, hence polynomial.
- **No asteroids ⇒ 0 shots** (Example 3): every row's adjacency list is empty, matching is
  0.
- Duplicate asteroids on the same `(r, c)` (excluded here) would just be parallel edges and
  wouldn't change the cover.
- The answer never exceeds `N` (shoot every occupied row) and never exceeds the number of
  distinct occupied rows or columns.
