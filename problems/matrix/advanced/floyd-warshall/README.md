# Floyd–Warshall

**Floyd–Warshall** computes **all-pairs shortest paths** (APSP) in a weighted graph by running dynamic programming directly over the weighted adjacency matrix. It answers "what is the shortest distance from *every* vertex to *every* other vertex?" in a single `O(V³)` pass.

## The core idea

Let `dist[i][j]` be the length of the shortest path from `i` to `j`. Process vertices one at a time as **allowed intermediate stops**. After considering vertex `k` as a possible waypoint, `dist[i][j]` holds the shortest path from `i` to `j` that only uses intermediate vertices drawn from `{0, 1, ..., k}`. The transition is a single relaxation:

```
dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

The **loop order matters**: the outer loop must be over `k` (the intermediate vertex), with `i` and `j` inside it. Iterating `k` last would be wrong.

```
for k in range(V):        # intermediate vertex — MUST be outermost
    for i in range(V):    # source
        for j in range(V): # destination
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

## When to reach for it

- You need **all pairs** of shortest distances, not just from a single source.
- The graph is **small and dense** — `V` up to a few hundred (`V³` around 10⁷–10⁸).
- Edge weights may be **negative** (unlike Dijkstra), as long as there is no negative cycle.
- The relation is a **transitive closure** or "min-plus / boolean / product" accumulation over paths (reachability, prerequisites, division chains, bottleneck). The same triple loop solves many problems where the operator is not literally `+/min`.
- You also want easy **negative-cycle detection**: after the algorithm, `dist[i][i] < 0` for some `i` means a negative cycle exists.

## When NOT to use it

- Single-source only on a large graph → use Dijkstra (`O(E log V)`) or Bellman–Ford.
- Large `V` (thousands+) with a sparse graph → running Dijkstra from every source (`O(V·E log V)`) is usually far faster than `O(V³)`.

## Complexity

| | Cost |
|---|---|
| Time | `O(V³)` |
| Space | `O(V²)` for the distance matrix |

## Problems

| # | Problem | Technique fit | Difficulty |
|---|---------|---------------|------------|
| 1 | [Find the City With the Smallest Number of Neighbors at a Threshold Distance](problem-01-find-the-city-threshold-distance/PROBLEM.md) | Plain APSP, then count reachable neighbors | Medium |
| 2 | [Minimum Cost to Convert String I](problem-02-minimum-cost-to-convert-string/PROBLEM.md) | APSP over a fixed 26-node alphabet graph | Medium |
| 3 | [Course Schedule IV](problem-03-course-schedule-iv-transitive-closure/PROBLEM.md) | Boolean transitive closure (reachability) | Medium |
| 4 | [Evaluate Division](problem-04-evaluate-division/PROBLEM.md) | Product-accumulating variant of the triple loop | Medium |
| 5 | [Count Subtrees With Max Distance Between Cities](problem-05-count-subtrees-max-distance/PROBLEM.md) | APSP as a subroutine, then enumerate connected vertex subsets | Hard |
