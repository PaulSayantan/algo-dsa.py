# Min-Plus (Tropical) Matrix Multiplication

## What it is

Ordinary matrix multiplication combines rows and columns with the operations
`(×, +)`:

```
C[i][j] = Σ_k  A[i][k] * B[k][j]
```

**Min-plus** (a.k.a. **tropical**) matrix multiplication replaces that pair of
operations with `(+, min)`:

```
C[i][j] = min_k ( A[i][k] + B[k][j] )
```

- `+` (ordinary addition) plays the role of `×`.
- `min` plays the role of `+`.
- The additive identity `0` becomes `+∞` (min with ∞ is a no-op).
- The multiplicative identity `1` becomes `0` (adding 0 changes nothing).

This forms a *semiring* (the tropical/min-plus semiring), which matters because
matrix multiplication over any semiring is **associative**. Associativity is
exactly what lets us use fast exponentiation.

## Why it is useful

If `W` is a weighted adjacency matrix where `W[i][j]` is the cost of the edge
`i → j` (and `+∞` when there is no edge), then the min-plus product `W ⊙ W`
gives, in entry `(i, j)`, the cheapest **2-edge** walk from `i` to `j`. By
induction:

```
(W^{⊙k})[i][j] = minimum cost of a walk from i to j using EXACTLY k edges
```

So the technique is the tool of choice whenever a problem asks for
**shortest / cheapest paths constrained by a fixed or bounded number of hops
(edges/steps/transitions)** — especially when that hop count `k` is enormous.
A single tropical product is `O(V³)`. Repeated squaring gives
`W^{⊙k}` in `O(V³ · log k)`, which tames values of `k` up to `10^18` that no
edge-relaxation DP could touch.

Putting a `0` on the diagonal (a free self-loop) turns "exactly k edges" into
"**at most** k edges", which is how bounded-stop problems are modeled.

## Typical complexity

| Operation | Time | Space |
|---|---|---|
| One min-plus product of `V×V` matrices | `O(V³)` | `O(V²)` |
| Exactly-`k`-edge distances via repeated squaring | `O(V³ · log k)` | `O(V²)` |
| Exactly-`k`-edge distances by naive chaining (small k) | `O(V³ · k)` | `O(V²)` |

Use the naive chain when `k` is small; switch to repeated squaring when `k` is
large (that is where tropical multiplication truly shines).

## When to reach for it

- The graph is small (`V` typically ≤ a few hundred) but the number of allowed
  hops `k` is large or must be *exact*.
- You need "shortest path using exactly / at most `k` edges."
- The DP transition is "combine two segments by choosing an intermediate state
  and adding their costs, minimizing over the choice" — that *is* a min-plus
  product, so it can be exponentiated.

## Limitations

- Cubic per product: it does not scale to graphs with thousands of vertices.
- Handles negative edges fine (it is a min, not a relaxation), but **negative
  cycles** make "shortest walk of length ≥ k" unbounded — interpret results
  carefully.
- If you only need shortest paths with *no* hop constraint, plain
  Floyd–Warshall or Dijkstra is simpler and faster.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Shortest Path with Exactly K Edges](problem-01-shortest-path-exactly-k-edges/PROBLEM.md) | One `W^{⊙k}` by naive chaining; the core idea | Easy |
| 2 | [Cheapest Flights Within K Stops](problem-02-cheapest-flights-within-k-stops/PROBLEM.md) | "At most" via a 0-diagonal (free self-loop) | Medium |
| 3 | [Min-Cost Walk of Exactly K Edges, Huge K](problem-03-min-cost-walk-exactly-k-edges-huge-k/PROBLEM.md) | Repeated squaring for `k` up to `10^18` | Medium |
| 4 | [Cow Relays (Exactly N Edges, Sparse Labels)](problem-04-cow-relays-exactly-n-edges/PROBLEM.md) | Vertex compression + squaring | Hard |
| 5 | [Minimum-Cost Adjacent Category Sequence](problem-05-min-adjacent-cost-sequence/PROBLEM.md) | Recognizing a hidden tropical product in a DP | Hard |
