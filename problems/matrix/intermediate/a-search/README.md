# A\* Search

## What it is

**A\* (pronounced "A-star") search** is a best-first shortest-path algorithm that finds
the minimum-cost path from a start state to a goal by expanding states in order of an
**estimated total cost**

```
f(n) = g(n) + h(n)
```

where `g(n)` is the *known* cost of the cheapest path found so far from the start to
`n`, and `h(n)` is a **heuristic** — a cheap-to-compute estimate of the remaining cost
from `n` to the goal. A priority queue (min-heap) always pops the state with the
smallest `f`. Setting `h ≡ 0` makes A\* degenerate into **Dijkstra**; a perfect `h`
(the exact remaining distance) would make it walk straight to the goal. A\* is the
sweet spot in between: it uses the heuristic to *aim* the search at the goal so it
explores far fewer states than uninformed BFS/Dijkstra, while still guaranteeing the
optimal path.

On a grid, states are cells (or richer tuples like `(row, col, extra_state)`), edges
connect neighboring cells, and `h` is typically a geometric lower bound on the
remaining distance (Manhattan, Chebyshev, or Euclidean).

## Correctness conditions

A\* returns an optimal path **iff** the heuristic is *admissible*:

- **Admissible:** `h(n) ≤ true_remaining_cost(n)` for every `n` — it never
  *overestimates*. This alone guarantees optimality for the tree-search form.
- **Consistent (monotone):** `h(n) ≤ cost(n, n') + h(n')` for every edge `n → n'`.
  Consistency implies admissibility and additionally guarantees that the first time
  a node is popped its `g` value is already final, so no node needs re-expansion.

For unit-step 4-directional grids the **Manhattan distance** is consistent; for
8-directional (king-move) grids the **Chebyshev distance** is consistent; when
diagonal moves cost `√2`, the **Euclidean distance** is consistent.

## When to reach for it

Reach for A\* when you need the **single shortest path to a specific goal** (not
distances to everything) and you can cheaply compute a lower bound on the remaining
cost:

- Point-to-point shortest path on a large grid where BFS/Dijkstra would explore most
  of the map but a good heuristic can prune huge portions.
- Search over an implicit / exponential state space (sliding puzzles, board
  configurations) where a domain heuristic (misplaced tiles, sum of Manhattan
  distances) dramatically cuts the frontier.
- Path problems with extra state baggage (remaining fuel, obstacles you may remove)
  where the geometric distance to the goal is still a valid lower bound.

If there is **no goal** (you want distance to *all* cells) or **no useful heuristic**
(`h = 0`), plain BFS / Dijkstra is simpler and just as good — A\* only helps when the
heuristic carries information.

## Core template

```python
import heapq

def a_star(start, goal, neighbors, cost, h):
    g = {start: 0}
    pq = [(h(start), 0, start)]          # (f = g + h, g, node)
    while pq:
        f, gc, node = heapq.heappop(pq)
        if node == goal:
            return gc                    # optimal cost
        if gc > g.get(node, float("inf")):
            continue                     # stale duplicate, skip
        for nxt in neighbors(node):
            ng = gc + cost(node, nxt)
            if ng < g.get(nxt, float("inf")):
                g[nxt] = ng
                heapq.heappush(pq, (ng + h(nxt), ng, nxt))
    return -1                            # goal unreachable
```

The `f`-value in the heap tuple drives the ordering; the "stale duplicate" guard lets
us push improved entries lazily instead of doing a decrease-key.

## Complexity

Let `V` be the number of reachable states and `E` the number of edges (on a grid,
`E = O(V)` since each cell has a constant number of neighbors).

- **Time:** worst case `O(E + V log V)` — the same bound as Dijkstra with a binary
  heap, because with a poor heuristic A\* degrades to Dijkstra. With a good, informed
  heuristic the number of expanded states is typically **far smaller** than `V`, which
  is the whole point.
- **Space:** `O(V)` for the `g`-score map, the heap, and the (optional) parent
  pointers.

The heuristic never changes the worst-case bound; it changes the *typical* number of
expansions, which is what makes A\* fast in practice.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Shortest Path in Binary Matrix](problem-01-shortest-path-in-binary-matrix/PROBLEM.md) | 8-directional grid; Chebyshev heuristic guides A\* to the corner | Medium |
| 2 | [Minimum Knight Moves](problem-02-minimum-knight-moves/PROBLEM.md) | Infinite board; custom knight-distance heuristic prunes the frontier | Medium |
| 3 | [Shortest Path with Obstacle Elimination](problem-03-shortest-path-with-obstacle-elimination/PROBLEM.md) | State `(r, c, k_left)`; Manhattan heuristic on an augmented graph | Hard |
| 4 | [Sliding Puzzle](problem-04-sliding-puzzle/PROBLEM.md) | A\* over an exponential state space using a Manhattan-sum heuristic | Hard |
| 5 | [Cut Off Trees for Golf Event](problem-05-cut-off-trees-for-golf/PROBLEM.md) | Many ordered point-to-point queries, each an A\* shortest path | Hard |
