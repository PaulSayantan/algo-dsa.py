# Traveling Salesman (Held-Karp) — Solution

## Brute Force

Enumerate every ordering of the `n - 1` non-start cities, compute each tour's
cost, and take the minimum.

- **Time:** `O(n! * n)` — `(n-1)!` permutations, `O(n)` to sum each tour.
  For `n = 15` this is about `87 * 10^9` operations — impractical.
- **Space:** `O(n)` for the current permutation.

The waste: two different permutations that visit the *same set* of cities and
end at the *same* city share all their future decisions, yet brute force
recomputes them independently.

## Optimal Approach (Bitmask DP — Held-Karp)

### State

Let `dp[mask][last]` = the minimum cost of a path that

- starts at city `0`,
- visits **exactly** the set of cities encoded by `mask` (bit `i` set means
  city `i` is on the path), and
- currently ends at city `last`, where bit `last` must be set in `mask`.

The insight is that once you know the visited *set* and *where you are*, the
cost of the best continuation does not depend on the order you visited the set.
That is the optimal-substructure property that collapses `(n-1)!` orderings
into `2^n * n` states.

### Recurrence

- **Base case:** `dp[1][0] = 0` — mask `000...1` contains only city 0, sitting
  at city 0 with zero cost. Everything else starts at `infinity`.
- **Transition:** from state `(mask, last)` move to an unvisited city `nxt`:

  ```
  new_mask = mask | (1 << nxt)
  dp[new_mask][nxt] = min(dp[new_mask][nxt], dp[mask][last] + dist[last][nxt])
  ```

- **Answer:** close the cycle by returning to city 0 from the full mask:

  ```
  full = (1 << n) - 1
  answer = min(dp[full][last] + dist[last][0] for last in 1..n-1)
  ```

  For `n == 1` the answer is `0` (no edges to traverse).

### Why it is correct

Any optimal tour `0 -> ... -> last -> 0` has a prefix `0 -> ... -> last` whose
cost is minimal among all paths visiting the same set and ending at `last` —
otherwise we could swap in the cheaper prefix and improve the tour, a
contradiction. `dp[mask][last]` computes exactly that minimal prefix cost, and
the final step adds the single return edge. Processing masks in increasing
integer order ensures each `dp[mask][last]` is finalized before it is used to
build a larger mask (adding a bit strictly increases the integer).

### Reference implementation

```python
def tsp_min_cost(dist):
    n = len(dist)
    if n == 1:
        return 0
    INF = float("inf")
    full = (1 << n) - 1
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0  # start at city 0, only city 0 visited

    for mask in range(1 << n):
        if not (mask & 1):        # every path must include the start city
            continue
        for last in range(n):
            if dp[mask][last] == INF or not (mask & (1 << last)):
                continue
            for nxt in range(n):
                if mask & (1 << nxt):
                    continue
                nm = mask | (1 << nxt)
                cand = dp[mask][last] + dist[last][nxt]
                if cand < dp[nm][nxt]:
                    dp[nm][nxt] = cand

    return min(dp[full][last] + dist[last][0] for last in range(1, n))
```

- **Time:** `O(2^n * n^2)` — `2^n` masks times `n` "last" cities times `n`
  candidate next cities. For `n = 15`: `2^15 * 225 ≈ 7.4 * 10^6`. Fast.
- **Space:** `O(2^n * n)` for the DP table.

## Key Insights & Edge Cases

- **Fix the start city.** Anchoring at city 0 removes the `n`-fold rotational
  redundancy of a cycle and lets `dp[1][0] = 0` be the sole base case.
- **`dp[mask][last]` requires bit `last` set in `mask`.** Skip states that
  violate this; they are meaningless.
- **`n = 1`** must be special-cased to `0`, since the return-edge min over
  `range(1, n)` would otherwise be empty.
- **Asymmetric costs** are handled correctly because the recurrence uses the
  directed edge `dist[last][nxt]`; it never assumes `dist[i][j] == dist[j][i]`.
- **Path variant (LeetCode 847/943):** if you only need to *visit* all nodes
  (no return to start, any start), drop the `+ dist[last][0]` term and
  initialize `dp[1 << i][i] = 0` for every `i`.
- **Reconstruction:** store a parent pointer per state to recover the actual
  tour, not just its cost.
