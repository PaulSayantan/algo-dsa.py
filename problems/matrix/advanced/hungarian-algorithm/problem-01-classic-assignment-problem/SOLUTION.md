# Solution — Classic Assignment Problem

## Brute Force

Enumerate every way to match workers to jobs. A valid assignment is a
permutation `p` of `{0, ..., n-1}` where worker `i` takes job `p[i]`. Sum the
cost of each permutation and keep the minimum.

```python
from itertools import permutations

def min_assignment_cost_brute(cost):
    n = len(cost)
    return min(sum(cost[i][p[i]] for i in range(n)) for p in permutations(range(n)))
```

- **Time:** `O(n! * n)` — there are `n!` permutations, each costing `O(n)` to sum.
- **Space:** `O(n)` for the current permutation.

This is fine for `n <= ~10` but explodes immediately afterward (`13! > 6e9`).

A better exponential approach is bitmask DP over the set of used jobs:
`dp[mask]` = min cost to assign the first `popcount(mask)` workers to the job
subset `mask`. That is `O(n * 2^n)` time and `O(2^n)` space — good for
`n <= ~20` but still exponential.

## Optimal Approach — Hungarian Algorithm

The Hungarian (Kuhn–Munkres) algorithm solves the assignment problem in
**`O(n^3)`**. The version below is the `O(n^3)` "potentials + shortest
augmenting path" formulation (Jonker–Volgenant style), which is compact and
fast in practice.

### Why it is correct

The algorithm maintains **dual variables** (potentials) `u[i]` for each row and
`v[j]` for each column such that the *reduced cost*

```
reduced(i, j) = cost[i][j] - u[i] - v[j] >= 0   for all i, j
```

An edge `(i, j)` is **tight** when `reduced(i, j) == 0`. By LP duality (the
assignment problem is an integral LP whose optimum is attained at a permutation
matrix), if we can find a **perfect matching using only tight edges**, that
matching is provably a minimum-cost assignment. The algorithm adds one row at a
time, finding a shortest augmenting path in the graph of tight edges and
adjusting potentials (by `delta`, the smallest slack) whenever no tight edge
extends the search. Each of the `n` rows is incorporated with an `O(n^2)`
augmentation, giving `O(n^3)` overall.

### Step-by-step

1. Keep arrays `u[0..n]`, `v[0..m]`, `p[0..m]` (`p[j]` = the row currently
   matched to column `j`), and `way[0..m]` (to reconstruct the augmenting path).
2. For each new row `i`, place it in a virtual column `0` and run a Dijkstra-like
   search over columns using slack values `minv[j] = min over visited rows of
   reduced(row, j)`.
3. Repeatedly pick the unvisited column `j1` with the smallest slack `delta`,
   mark it visited, and update potentials: add `delta` to `u` of every visited
   row, subtract `delta` from `v` of every visited column, and subtract `delta`
   from the slack of every unvisited column. This keeps all reduced costs
   non-negative while creating at least one new tight edge.
4. When the search reaches an unmatched column, walk `way[]` backward to flip the
   matching along the augmenting path — increasing the matching size by one.
5. After all `n` rows are matched, sum `cost[p[j]][j]` over matched columns.

### Reference implementation

```python
from typing import List

def min_assignment_cost(cost: List[List[int]]) -> int:
    n = len(cost)
    m = len(cost[0])            # here m == n; the code also handles m > n
    INF = float("inf")
    u = [0] * (n + 1)
    v = [0] * (m + 1)
    p = [0] * (m + 1)           # p[j] = 1-indexed row matched to column j
    way = [0] * (m + 1)
    for i in range(1, n + 1):
        p[0] = i
        j0 = 0
        minv = [INF] * (m + 1)
        used = [False] * (m + 1)
        while True:
            used[j0] = True
            i0 = p[j0]
            delta = INF
            j1 = -1
            for j in range(1, m + 1):
                if not used[j]:
                    cur = cost[i0 - 1][j - 1] - u[i0] - v[j]
                    if cur < minv[j]:
                        minv[j] = cur
                        way[j] = j0
                    if minv[j] < delta:
                        delta = minv[j]
                        j1 = j
            for j in range(m + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta
            j0 = j1
            if p[j0] == 0:
                break
        while j0:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
    return sum(cost[p[j] - 1][j - 1] for j in range(1, m + 1) if p[j] != 0)
```

- **Time:** `O(n^3)`.
- **Space:** `O(n)` extra beyond the input matrix (the `u/v/p/way/minv/used`
  arrays are all `O(n)`).

## Key Insights & Edge Cases

- **Row/column reduction is free:** subtracting a constant from a whole row or a
  whole column changes the total cost of *every* assignment by the same amount,
  so the optimal assignment is unchanged. This is the intuition behind the
  potentials `u` and `v`.
- **`n == 1`:** the answer is simply `cost[0][0]`.
- **Negative costs are fine:** the algorithm never assumes non-negative input
  costs — only the *reduced* costs are kept non-negative. (Maximization problems
  can be turned into minimization by negating the matrix.)
- **1-indexing:** the reference uses 1-based indices for `u/v/p` with a sentinel
  column `0`; keep the `-1` offsets when reading from `cost`.
- **Overflow:** with costs up to `10^6` and `n` up to `200`, totals fit
  comfortably in 64-bit integers; Python integers are unbounded so this is a
  non-issue here.
