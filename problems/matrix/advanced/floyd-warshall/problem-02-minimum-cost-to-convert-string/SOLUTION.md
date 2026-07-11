# Solution — Minimum Cost to Convert String I

## Brute Force

For each string position where `source[p] != target[p]`, run a fresh shortest-path search (e.g. Dijkstra) from `source[p]` to `target[p]` over the letter graph.

- Up to `n = 10^5` positions, each search touching up to 26 nodes and 2000 edges → roughly `O(n · E log V)`. This repeats identical work because there are only 26 possible source letters.
- Correct, but wasteful: the letter-to-letter distances never change, so recomputing them per position is pure overhead.

## Optimal Approach (Floyd–Warshall)

The key observation: there are only **26 letters**, so the "cheapest cost to turn letter `x` into letter `y`" is a fixed `26 × 26` table. Precompute it once, then answer each position in `O(1)`.

### Steps

1. Build a `26 × 26` matrix `dist`, `INF` off-diagonal and `0` on the diagonal.
2. For each rule `(original[i], changed[i], cost[i])`, set
   `dist[o][c] = min(dist[o][c], cost[i])` (keep the cheapest among duplicate rules).
3. Run Floyd–Warshall with `k` outermost over all 26 letters to get all-pairs cheapest conversion costs.
4. Walk the strings together. For each position `p`:
   - If `source[p] == target[p]`, add 0.
   - Else look up `dist[source[p]][target[p]]`. If it is `INF`, return `-1`.
   - Otherwise add it to the running total.
5. Return the total.

### Why it is correct

A conversion can be a chain of rules (`a → b → c`), and its cost is the sum of the rule costs along the chain. That is exactly the definition of a shortest path in the letter graph with additive positive edge weights. Floyd–Warshall's invariant guarantees `dist[x][y]` is the minimum-cost chain from `x` to `y` once all letters have been considered as intermediates. Costs are positive, so no negative cycles are possible.

### Reference implementation

```python
def minimumCost(self, source, target, original, changed, cost):
    INF = float("inf")
    dist = [[INF] * 26 for _ in range(26)]
    for i in range(26):
        dist[i][i] = 0
    for o, c, w in zip(original, changed, cost):
        a, b = ord(o) - 97, ord(c) - 97
        dist[a][b] = min(dist[a][b], w)

    for k in range(26):
        for i in range(26):
            if dist[i][k] == INF:
                continue
            for j in range(26):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    total = 0
    for s, t in zip(source, target):
        if s == t:
            continue
        w = dist[ord(s) - 97][ord(t) - 97]
        if w == INF:
            return -1
        total += w
    return total
```

### Complexity

- Time: `O(26³)` for the matrix (constant) + `O(L)` where `L = len(original)` to load edges + `O(n)` to scan the strings → **`O(n + L + 26³)`**, effectively linear in the input.
- Space: `O(26²)` = `O(1)` for the matrix.

## Key Insights & Edge Cases

- **Small fixed node set** turns a per-query shortest path into a one-time precomputation — the whole point of using APSP here.
- **Duplicate rules** for the same `(x, y)` pair: keep the minimum cost.
- **Self-conversions** are free; skip equal positions so an unreachable but unneeded letter never forces `-1`.
- **Impossible conversion**: any needed lookup equal to `INF` means the whole answer is `-1`.
- Because costs can be up to `10^6` and chains up to 26 long, the max single-conversion cost fits comfortably in a 64-bit int; the running total across `10^5` positions also fits.
- Guarding `dist[i][k] == INF` before the inner loop avoids meaningless `INF + INF` work.
