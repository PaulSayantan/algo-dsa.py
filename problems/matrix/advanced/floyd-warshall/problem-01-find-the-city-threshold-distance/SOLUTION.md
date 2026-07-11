# Solution — Find the City at a Threshold Distance

## Brute Force

Run a single-source shortest-path search (Dijkstra or Bellman–Ford) **from every city** to obtain that city's distances to all others, then count how many are within the threshold.

- With Dijkstra from each source: `O(V · E log V)` time, `O(V + E)` space per run.
- This works and is asymptotically better on sparse graphs, but with `V ≤ 100` the code is longer and the constant factors of a heap-based search offer no practical win here.

## Optimal Approach (Floyd–Warshall)

Because we need distances between **all pairs** and `V ≤ 100` (so `V³ ≤ 10^6`), Floyd–Warshall is the cleanest fit.

### Steps

1. Initialize a `V × V` matrix `dist` with `INF` everywhere, `0` on the diagonal.
2. For each edge `(u, v, w)`, set `dist[u][v] = dist[v][u] = min(existing, w)` (bidirectional; keep the minimum in case of parallel edges).
3. Run the triple loop, `k` outermost:
   ```
   for k in range(n):
       for i in range(n):
           for j in range(n):
               if dist[i][k] + dist[k][j] < dist[i][j]:
                   dist[i][j] = dist[i][k] + dist[k][j]
   ```
4. For each city `i`, count `reach[i] = |{ j != i : dist[i][j] <= distanceThreshold }|`.
5. Return the city minimizing `reach[i]`, breaking ties toward the **larger** index. Iterating `i` from `0` upward and using `<=` when comparing (so a later, equal-or-smaller count overwrites) naturally yields the largest index.

### Why it is correct

After the outer loop finishes iteration `k`, the invariant is: `dist[i][j]` equals the shortest path from `i` to `j` using only intermediate vertices in `{0, ..., k}`. When `k` reaches `V - 1`, every vertex is an allowed intermediate, so `dist[i][j]` is the true shortest distance. All weights are positive, so no negative-cycle concerns arise.

### Reference implementation

```python
def findTheCity(self, n, edges, distanceThreshold):
    INF = float("inf")
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)
        dist[v][u] = min(dist[v][u], w)

    for k in range(n):
        for i in range(n):
            dik = dist[i][k]
            if dik == INF:
                continue
            for j in range(n):
                if dik + dist[k][j] < dist[i][j]:
                    dist[i][j] = dik + dist[k][j]

    best_city, best_count = 0, n + 1
    for i in range(n):
        count = sum(
            1 for j in range(n) if i != j and dist[i][j] <= distanceThreshold
        )
        if count <= best_count:          # <= keeps the larger index on ties
            best_count = count
            best_city = i
    return best_city
```

### Complexity

- Time: `O(V³)` for the triple loop, plus `O(V²)` for the counting pass → `O(V³)`.
- Space: `O(V²)` for the distance matrix.

## Key Insights & Edge Cases

- **Tie-break correctly.** "Smallest count, largest index." Using `<=` while scanning `i` ascending is a clean way to keep the largest index among equal minima.
- **Parallel edges.** The constraints say pairs are distinct, but taking `min` when populating the matrix is a good habit regardless.
- **The `k`-loop must be outermost.** Swapping the loop order breaks the DP invariant and yields wrong distances.
- **Early `continue` on `INF`** for `dist[i][k]` is a small but real constant-factor speedup and avoids `INF + INF` overflow issues (harmless with Python floats, but relevant if you use a large sentinel int).
- **Disconnected cities** stay at `INF` and correctly never count toward a threshold.
