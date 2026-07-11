# Solution — Rectangular Job Assignment

## Brute Force

Choose, for the `n` workers, an ordered selection of `n` distinct jobs out of
`m` (a `P(m, n)` arrangement) and sum the costs; keep the minimum.

```python
from itertools import permutations

def min_rectangular_assignment_brute(cost):
    n, m = len(cost), len(cost[0])
    best = float("inf")
    for jobs in permutations(range(m), n):        # ordered pick of n jobs
        best = min(best, sum(cost[i][jobs[i]] for i in range(n)))
    return best
```

- **Time:** `O(P(m, n) * n) = O(m! / (m - n)! * n)` — factorial, explodes fast.
- **Space:** `O(n)`.

## Optimal Approach — Hungarian Algorithm

The unbalanced (rectangular) assignment problem reduces to the balanced one:

1. **Pad to a square** `m x m` matrix by appending `m - n` dummy worker rows of
   all zeros. A dummy worker matched to a job contributes `0`, effectively
   marking that job "unassigned by a real worker".
2. Run the standard `O(m^3)` Hungarian Algorithm on the square matrix.
3. The returned minimum total cost equals the cost of the real assignment,
   because the dummy rows add `0`.

Alternatively (and more efficiently), run a Hungarian variant that natively
handles `n <= m`: iterate over the `n` real rows only, keeping `m` columns and
letting unmatched columns keep `p[j] = 0`. That avoids materializing the dummy
rows and runs in `O(n * m^2)`.

### Why it is correct

Each valid assignment is an injective worker→job map (a matching saturating all
workers). Minimum-cost bipartite matching with `n <= m` is exactly solved by
Hungarian. The zero-cost dummy rows in the padded version cannot lower or raise
the real workers' contribution, so the optimum is preserved.

```python
from typing import List

def min_rectangular_assignment(cost: List[List[int]]) -> int:
    n, m = len(cost), len(cost[0])                  # n <= m
    INF = float("inf")
    u = [0] * (n + 1); v = [0] * (m + 1)
    p = [0] * (m + 1); way = [0] * (m + 1)          # p[j] = row matched to job j
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

- **Time:** `O(n * m^2)` with the native `n <= m` variant (`O(m^3)` if you pad).
- **Space:** `O(n * m)` input + `O(m)` working arrays.

## Key Insights & Edge Cases

- **Which side is smaller?** Always ensure the Hungarian loop iterates over the
  *smaller* dimension (`min(n, m)` rows). If instead you have more workers than
  jobs (`n > m`), transpose the matrix first so the outer loop runs over jobs.
- **Padding value:** dummy rows must be **zero** for a minimization objective. If
  instead you were forced to assign *all* jobs and some workers could be idle,
  the roles of padding swap — pad the shorter side and reason about which
  leftovers are free.
- **`n == m`:** degenerates to the classic square assignment (Example 2).
- **Non-negative costs** here mean the padded zero rows never become the cheapest
  by accident in a way that corrupts real rows — a dummy just absorbs a spare
  job.
- **Large values:** with `cost <= 10^6` and up to `200` rows, totals stay well
  within 64-bit range.
