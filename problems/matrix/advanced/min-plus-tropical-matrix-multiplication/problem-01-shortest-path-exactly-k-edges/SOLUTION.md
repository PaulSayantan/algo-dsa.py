# Solution — Shortest Path with Exactly K Edges

## Brute Force

Enumerate every walk of exactly `k` edges from `u` with a DFS/recursion,
tracking the running cost, and record the cheapest that ends at `v`.

Because a walk may reuse vertices and edges, the branching factor is the
out-degree (up to `n`) and the depth is `k`, giving up to `n^k` walks.

- **Time:** `O(n^k)` — exponential, only usable for tiny `k` and `n`.
- **Space:** `O(k)` recursion depth.

A better baseline is a layered DP:
`dp[e][j]` = min cost of an `e`-edge walk from `u` to `j`, with
`dp[e][j] = min_t ( dp[e-1][t] + W[t][j] )`. That is `O(k · n²)` time and is
already correct — and notice its transition is *literally* a min-plus
matrix-vector product. Generalizing the vector to a full matrix gives the
tropical-power method below.

## Optimal Approach (Min-Plus / Tropical Matrix Multiplication)

**Setup.** Build `W`, the `n×n` weighted adjacency matrix:

```
W[i][j] = weight(i -> j)   if the edge exists
W[i][j] = INF              otherwise
```

**Core identity.** Define the tropical product

```
(A ⊙ B)[i][j] = min over t of ( A[i][t] + B[t][j] )
```

Interpretation: if `A[i][t]` is the best cost of an `a`-edge walk `i → t` and
`B[t][j]` is the best cost of a `b`-edge walk `t → j`, then choosing the best
split point `t` and adding gives the best `(a+b)`-edge walk `i → j`. By
induction, `(W^{⊙k})[i][j]` is the minimum cost of an **exactly-`k`-edge** walk
from `i` to `j`.

**Why it is correct.** Every `k`-edge walk has a unique vertex `t` after its
first `a` edges. The DP over the split point considers all such `t`, so no walk
is missed; the `min` picks the cheapest. The tropical semiring is associative,
so the product is well-defined regardless of how we group multiplications.

**Steps (naive chaining, ideal here since `k ≤ 20`):**

1. Build `W` from the edge list, `INF` for missing edges.
2. Start with `result = W` (this represents exactly-1-edge costs).
3. Repeat `k - 1` times: `result = result ⊙ W` (each step adds one edge).
4. Read `result[u][v]`; if it is `INF`, return `-1`, else return it.

```python
def tropical_mul(A, B):
    n, m, p = len(A), len(B[0]), len(B)
    C = [[INF] * m for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        Ci = C[i]
        for t in range(p):
            a = Ai[t]
            if a == INF:
                continue
            Bt = B[t]
            for j in range(m):
                cand = a + Bt[j]
                if cand < Ci[j]:
                    Ci[j] = cand
    return C

def shortest_path_k_edges(n, edges, u, v, k):
    W = [[INF] * n for _ in range(n)]
    for a, b, w in edges:
        W[a][b] = min(W[a][b], w)   # keep cheapest parallel edge
    result = W
    for _ in range(k - 1):
        result = tropical_mul(result, W)
    ans = result[u][v]
    return -1 if ans == INF else ans
```

- **Time:** `O(k · n³)` — `k-1` tropical products, each `O(n³)`.
- **Space:** `O(n²)` for the matrices.

When `k` is large, replace the linear chain with **repeated squaring** to reach
`O(n³ · log k)`; see Problem 3, which is dedicated to that variant.

## Key Insights & Edge Cases

- **Exactly vs. at most.** This problem wants *exactly* `k` edges. Do **not**
  put `0` on the diagonal — that would silently allow shorter walks (a free
  self-loop). The pure edge matrix (INF diagonal unless a real self-loop
  exists) enforces "exactly `k`."
- **Parallel edges.** If the input can list two edges `i → j`, keep the minimum
  weight with `W[a][b] = min(W[a][b], w)`.
- **No walk exists.** If `result[u][v]` stays `INF`, return `-1` (Example 3).
- **`k = 1`.** The answer is just `W[u][v]` (or `-1`) — the loop runs zero
  times, which is correct.
- **INF arithmetic.** Guard against adding to `INF` (skip `INF` entries) so you
  never produce a bogus finite value from overflow; using `float('inf')` makes
  the `min` naturally ignore impossible transitions.
- **Self-loops in input.** If the graph genuinely contains an edge `i → i` with
  some weight, set `W[i][i]` to that weight — this is a real 1-edge move, unlike
  the artificial 0-diagonal used for "at most `k`" problems.
