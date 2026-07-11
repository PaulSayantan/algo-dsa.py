# Solution — Campus Bikes II

## Brute Force

With `n, m <= 10`, enumerate every way to give each worker a distinct bike. A
choice is an injection from workers to bikes; sum the Manhattan distances and
keep the minimum.

```python
from itertools import permutations

def assignBikes_brute(workers, bikes):
    n, m = len(workers), len(bikes)
    def dist(w, b):
        return abs(w[0] - b[0]) + abs(w[1] - b[1])
    best = float("inf")
    for perm in permutations(range(m), n):     # pick n bikes in order
        best = min(best, sum(dist(workers[i], bikes[perm[i]]) for i in range(n)))
    return best
```

- **Time:** `O(m! / (m-n)! * n)` — `P(m, n)` injections, each `O(n)`. For
  `m = 10` this is up to ~3.6M * 10, borderline.
- **Space:** `O(n)`.

A cleaner exponential solution used in interviews is **bitmask DP**: process
workers one at a time, `dp[mask]` = min distance after assigning workers to the
bikes in `mask`. That is `O(m * 2^m)` time / `O(2^m)` space and is the "expected"
LeetCode answer. But it grows exponentially in `m`.

## Optimal Approach — Hungarian Algorithm

This is a **minimum-cost bipartite perfect matching** on the workers' side:

1. Build the cost matrix `cost[i][j] = |wx_i - bx_j| + |wy_i - by_j|` — an
   `n x m` matrix (`n` workers, `m` bikes, `n <= m`).
2. Because it is rectangular, either
   - **pad** it to `m x m` by adding `m - n` dummy worker rows of all zeros (a
     dummy worker "assigned" to a bike contributes 0), **or**
   - use a Hungarian variant that natively supports `n <= m` (the reference
     below adds only real rows and lets `p[j]` stay `0` for unused bikes).
3. Run the `O(m^3)` Hungarian Algorithm; the result is the minimum total
   distance.

### Why it is correct

The set of valid assignments is exactly the set of injective worker→bike maps,
i.e. matchings that saturate every worker. Minimum-cost bipartite matching is
solved exactly by Hungarian. Padding with zero-cost dummy workers is safe: a
dummy contributes `0` regardless of which leftover bike it takes, so it never
alters the optimal cost of the real workers.

```python
from typing import List

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        n, m = len(workers), len(bikes)                 # n <= m
        cost = [[abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                 for j in range(m)] for i in range(n)]
        INF = float("inf")
        u = [0] * (n + 1); v = [0] * (m + 1)
        p = [0] * (m + 1); way = [0] * (m + 1)          # p[j] = row matched to bike j
        for i in range(1, n + 1):
            p[0] = i; j0 = 0
            minv = [INF] * (m + 1); used = [False] * (m + 1)
            while True:
                used[j0] = True; i0 = p[j0]; delta = INF; j1 = -1
                for j in range(1, m + 1):
                    if not used[j]:
                        cur = cost[i0 - 1][j - 1] - u[i0] - v[j]
                        if cur < minv[j]:
                            minv[j] = cur; way[j] = j0
                        if minv[j] < delta:
                            delta = minv[j]; j1 = j
                for j in range(m + 1):
                    if used[j]:
                        u[p[j]] += delta; v[j] -= delta
                    else:
                        minv[j] -= delta
                j0 = j1
                if p[j0] == 0:
                    break
            while j0:
                j1 = way[j0]; p[j0] = p[j1]; j0 = j1
        return sum(cost[p[j] - 1][j - 1] for j in range(1, m + 1) if p[j] != 0)
```

- **Time:** `O(n * m^2)` (equivalently `O(m^3)` after padding).
- **Space:** `O(n * m)` for the matrix, `O(m)` for potentials/matching.

## Key Insights & Edge Cases

- **Rectangular input:** the defining feature here is `n <= m`. Either pad to a
  square or use the `n <= m` Hungarian variant shown; both give the same answer.
- **Single worker (`n == 1`):** the answer is just the minimum distance to any
  bike (Example 3) — Hungarian degenerates to a simple min.
- **Ties don't matter:** if several bikes are equidistant, any optimal choice is
  fine; the algorithm returns the correct total either way.
- **Distances are non-negative** by construction, so no potential-initialization
  tricks are needed.
- For these small constraints bitmask DP is the standard accepted solution; use
  Hungarian to see how the same problem scales to larger `n, m`.
