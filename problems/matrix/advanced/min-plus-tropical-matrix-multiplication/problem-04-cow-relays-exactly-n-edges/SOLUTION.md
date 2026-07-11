# Solution — Cow Relays (Shortest Path Using Exactly N Edges)

## Brute Force

A DP over the exact edge count: `dp[e][j]` = shortest path from `S` to `j` using
exactly `e` edges, with the min-plus relaxation
`dp[e][j] = min_t ( dp[e-1][t] + W[t][j] )`. Iterate `e = 1 .. N`.

- **Time:** `O(N · m²)` where `m` is the number of distinct vertices. With
  `N` up to `10^6` and `m` up to `200`, that is `4 * 10^{10}` operations —
  far too slow.
- **Space:** `O(m)` with a rolling vector.

## Optimal Approach (Tropical Matrix Exponentiation + Vertex Compression)

Two independent tricks combine here.

### 1. Vertex compression

The vertex labels are sparse (up to `1000`) but at most `2T ≤ 200` distinct
vertices actually appear. Map each distinct label to a contiguous index
`0 .. m-1`. This keeps the matrix `m × m` (≤ `200 × 200`) instead of
`1000 × 1000`, which is what makes the cubic products affordable.

### 2. Tropical matrix exponentiation

Build the compressed **symmetric** weight matrix (undirected edges):

```
W[a][b] = W[b][a] = min(current, w)     for each edge (w, u, v)
W[i][j] = INF                            where no edge exists
```

Keep parallel edges by taking the min. Then, exactly as in Problems 1 and 3,

```
(W^{⊙N})[i][j] = shortest walk from i to j using EXACTLY N edges
```

Compute `W^{⊙N}` with **fast exponentiation**, seeding with the tropical
identity (`0` diagonal, `INF` off), because `N` is too large for a linear chain.

**Steps:**

1. Collect the distinct endpoints from all edges; assign each an index.
2. Build the `m × m` symmetric `W` with `min` for parallel edges.
3. Compute `R = W^{⊙N}` by repeated squaring in the tropical semiring.
4. Return `R[idx[S]][idx[E]]`.

```python
INF = float("inf")

def tmul(A, B):
    m = len(A)
    C = [[INF] * m for _ in range(m)]
    for i in range(m):
        Ai, Ci = A[i], C[i]
        for t in range(m):
            a = Ai[t]
            if a == INF:
                continue
            Bt = B[t]
            for j in range(m):
                cand = a + Bt[j]
                if cand < Ci[j]:
                    Ci[j] = cand
    return C

def cow_relays(N, edges, S, E):
    labels = sorted({v for (_, a, b) in edges for v in (a, b)})
    idx = {v: i for i, v in enumerate(labels)}
    m = len(labels)
    W = [[INF] * m for _ in range(m)]
    for w, a, b in edges:
        ia, ib = idx[a], idx[b]
        if w < W[ia][ib]:
            W[ia][ib] = W[ib][ia] = w        # undirected + keep min parallel edge
    # tropical fast exponentiation: R = W^{⊙N}
    R = [[0 if i == j else INF for j in range(m)] for i in range(m)]
    base = [row[:] for row in W]
    e = N
    while e > 0:
        if e & 1:
            R = tmul(R, base)
        base = tmul(base, base)
        e >>= 1
    return R[idx[S]][idx[E]]
```

**Why it is correct.** After compression the graph is unchanged (only labels
were renamed), so exactly-`N`-edge shortest walks are preserved. The tropical
power computes those walks (Problem 1 argument), and fast exponentiation yields
the same matrix in `O(m³ log N)` by associativity (Problem 3 argument).
Symmetry (`W[a][b] = W[b][a]`) encodes that each undirected edge can be walked in
either direction.

- **Time:** `O(m³ · log N)` — with `m ≤ 200` and `log₂(10^6) ≈ 20`, about
  `1.6 * 10^8` primitive operations; comfortably fast.
- **Space:** `O(m²)`.

## Key Insights & Edge Cases

- **Compress first.** Without compression the matrix could be `1000 × 1000` and
  the cubic products would blow up (`10^9` per product). Compression to `m ≤ 200`
  is what makes it tractable.
- **Undirected ⇒ symmetric matrix.** Set both `W[a][b]` and `W[b][a]`.
- **Parallel edges / self-references.** Keep the minimum weight among duplicate
  edges. (Cow Relays inputs have no self-loops; if they did, they would be real
  1-edge moves on the diagonal.)
- **Exactly N, so no 0-diagonal.** This problem requires *exactly* `N` edges, so
  do **not** seed `W` with a 0-diagonal — that would let a shorter path pad with
  free stays and undercount edges. (The `0`-diagonal appears only in the
  *identity* used to seed the exponentiation accumulator, which is a different
  matrix from `W`.)
- **Fast exponentiation is mandatory.** `N` up to `10^6` makes the linear
  `O(N·m²)` DP too slow; `log N` products are essential.
- **Guaranteed reachability.** The problem promises an exactly-`N`-edge path
  exists, so `R[S][E]` is finite; defensively, treat `INF` as "no path."
