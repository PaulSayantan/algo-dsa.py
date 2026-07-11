# Solution — Cheapest Flights Within K Stops

## Brute Force

DFS/BFS from `src`, tracking cost and the number of stops used so far, pruning
when the stop budget is exceeded. Without memoization this explores up to
`O(n^{k+1})` partial routes and is only viable for tiny inputs.

- **Time:** `O(n^{k+1})`.
- **Space:** `O(k)` recursion depth.

The standard efficient answer is **Bellman–Ford limited to `k + 1`
relaxation rounds** (`O(k · E)`), which is the practical LeetCode solution.
Below we use the tropical-matrix view because it generalizes cleanly and makes
the "at most vs. exactly" subtlety explicit — the topic of this folder.

## Optimal Approach (Min-Plus / Tropical Matrix Multiplication)

**The "at most" trick.** A pure edge matrix gives *exactly*-`e`-edge costs. To
allow *fewer* than `e` edges, add a **free self-loop**: set the diagonal to `0`.
Staying at a vertex costs nothing, so a route that "really" uses `f < e` flights
can pad itself with `e - f` free stays and still be counted in the exactly-`e`
product. Thus, with the 0-diagonal:

```
(M^{⊙e})[i][j] = cheapest route from i to j using AT MOST e flights
```

**Setup.**

```
M[i][i] = 0                 for all i           (free stay)
M[i][j] = price(i -> j)      if a flight exists
M[i][j] = INF                otherwise
```

**Answer.** "At most `k` stops" = "at most `k + 1` flights", so compute
`M^{⊙(k+1)}` and read `(src, dst)`.

**Why it is correct.** With the 0-diagonal, `M ⊙ M` at `(i, j)` takes
`min_t (M[i][t] + M[t][j])`. Choosing `t = i` or `t = j` (the free-stay option)
reproduces any single-flight cost, while other `t` give genuine two-flight
routes — so `M^{⊙2}` = "at most 2 flights." Induction extends this to any power.
Associativity of tropical multiplication guarantees the power is well-defined.

**Steps:**

1. Build `M` with `0` on the diagonal and flight prices off-diagonal (`INF`
   where no flight).
2. Compute `R = M^{⊙(k+1)}` (naive chaining is fine: `n ≤ 100`, `k ≤ n`).
3. Return `R[src][dst]`, or `-1` if it is `INF`.

```python
INF = float("inf")

def tropical_mul(A, B):
    n = len(A)
    C = [[INF] * n for _ in range(n)]
    for i in range(n):
        Ai, Ci = A[i], C[i]
        for t in range(n):
            a = Ai[t]
            if a == INF:
                continue
            Bt = B[t]
            for j in range(n):
                cand = a + Bt[j]
                if cand < Ci[j]:
                    Ci[j] = cand
    return C

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        M = [[INF] * n for _ in range(n)]
        for i in range(n):
            M[i][i] = 0                       # free self-loop => "at most"
        for a, b, w in flights:
            M[a][b] = min(M[a][b], w)
        R = M
        for _ in range(k):                    # M^(k+1): k extra products
            R = tropical_mul(R, M)
        ans = R[src][dst]
        return -1 if ans == INF else ans
```

- **Time:** `O(k · n³)` — `k` tropical products, each `O(n³)`.
- **Space:** `O(n²)`.

(The layered Bellman–Ford view of the same recurrence runs in `O(k · E)`, which
is faster on sparse graphs. The matrix view wins when the graph is dense and,
especially, when the hop bound is astronomically large — then swap the linear
chain for repeated squaring, `O(n³ log k)`; see Problem 3.)

## Key Insights & Edge Cases

- **The diagonal is the whole trick.** `0` on the diagonal converts "exactly
  `k+1` edges" into "at most `k+1` edges." Forgetting it makes the algorithm
  demand a route with the *exact* number of flights and return `-1` for shorter
  optimal routes.
- **`k` vs `k+1`.** Stops are one fewer than flights: `k` stops ⇒ `k + 1` legs
  ⇒ raise `M` to the `(k+1)`-th power (`k` multiplications after starting from
  `M`).
- **`k = 0`.** Only direct flights count. `M^{⊙1} = M`, whose off-diagonal is
  exactly the direct prices — matches Example 3 (answer 500).
- **Unreachable within budget.** If `R[src][dst]` is `INF`, return `-1`.
- **No negative cycles here.** Prices are positive, so the free-stay diagonal
  never creates a cheaper-by-looping artifact. (With negative edges, a
  0-diagonal is still safe because a self-loop of weight 0 can never *reduce*
  cost.)
- **Overflow / INF safety.** Skip `INF` source entries before adding so you
  never compute `INF + finite` as a spurious value.
