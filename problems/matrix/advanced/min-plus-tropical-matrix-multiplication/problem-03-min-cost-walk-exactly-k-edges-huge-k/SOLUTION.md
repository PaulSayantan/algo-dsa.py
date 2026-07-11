# Solution — Min-Cost Walk of Exactly K Edges (Huge K)

## Brute Force

The layered DP over edge count works but its running time is proportional to
`k`:

```
dp[0]      = row vector: 0 at u, INF elsewhere
dp[e][j]   = min_t ( dp[e-1][t] + W[t][j] )
answer     = dp[k][v]
```

This is `O(k · n²)` (a min-plus matrix-vector product per edge). Correct, but
with `k` up to `10^18` it would run for longer than the age of the universe.

- **Time:** `O(k · n²)` — infeasible for huge `k`.
- **Space:** `O(n)` (rolling vector) or `O(n²)` if chaining full matrices.

## Optimal Approach (Tropical Matrix Multiplication + Fast Exponentiation)

**Key property.** Min-plus matrix multiplication is **associative** (the tropical
semiring is a semiring), so

```
W^{⊙k} = W ⊙ W ⊙ ... ⊙ W    (k factors)
```

can be regrouped freely. That unlocks **binary exponentiation** (repeated
squaring): decompose `k` into its binary digits and combine squared powers.

**Tropical identity.** Fast exponentiation needs a multiplicative identity to
seed the accumulator. In the tropical semiring it is the matrix `I` with

```
I[i][i] = 0     (a length-0 walk that stays put costs nothing)
I[i][j] = INF   (i != j)
```

because `I ⊙ M = M ⊙ I = M`: `min_t (I[i][t] + M[t][j])` is minimized at `t = i`
(the only finite `I[i][t]`), giving `0 + M[i][j] = M[i][j]`.

**Steps:**

1. Build the tropical identity `R = I`.
2. Set `base = W`.
3. While `k > 0`:
   - if the low bit of `k` is 1, `R = R ⊙ base`;
   - `base = base ⊙ base`;
   - `k >>= 1`.
4. Return `R[u][v]`, or `-1` if `INF`.

```python
INF = float("inf")

def tmul(A, B):
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

def min_cost_walk_k_edges(n, W, u, v, k):
    R = [[0 if i == j else INF for j in range(n)] for i in range(n)]  # tropical I
    base = [row[:] for row in W]
    while k > 0:
        if k & 1:
            R = tmul(R, base)
        base = tmul(base, base)
        k >>= 1
    ans = R[u][v]
    return -1 if ans == INF else ans
```

**Why it is correct.** By induction `(W^{⊙k})[i][j]` is the min-cost exactly-`k`-
edge walk `i → j` (Problem 1). Repeated squaring computes the *same* matrix
`W^{⊙k}` — it just orders the associative products by the bits of `k`. Seeding
with the tropical identity handles the low bits properly and returns `I` (cost 0
on the diagonal) when `k = 0`, i.e. "a 0-edge walk from `u` to `u` costs 0."

- **Time:** `O(n³ · log k)` — at most `2 log₂ k` tropical products.
- **Space:** `O(n²)`.

## Key Insights & Edge Cases

- **Associativity is the license to square.** Without it, `W^{⊙k}` would depend
  on grouping and fast exponentiation would be invalid. The tropical semiring
  provides it.
- **Correct identity matters.** The identity is `0`-diagonal / `INF`-off, NOT
  the all-`INF` matrix (that is the *zero*, i.e. additive identity) and NOT the
  all-`0` matrix. Using the wrong seed silently corrupts the answer for `k` with
  certain bit patterns.
- **Exactly vs. at most.** As posed this is *exactly* `k` edges, so leave `W`'s
  diagonal as given (INF unless a real self-loop exists). For "at most `k`", add
  a `0`-diagonal to `W` first (see Problem 2).
- **Negative edges & cycles.** Min-plus handles negative weights, but if there
  is a negative-weight cycle reachable on the walk, "min cost of exactly `k`
  edges" tends to `-∞` as `k` grows; guard for it or note the problem forbids
  it. Here weights are non-negative, so no issue.
- **Overflow.** With non-negative weights up to `10^6` and `k` up to `10^18`, a
  finite answer can reach `~10^24`, which overflows 64-bit. The stated
  constraint promises finite answers fit in 64 bits; in a language with fixed
  integers, cap sums at a sentinel to avoid wraparound. Python's big integers
  sidestep this.
- **Numerical `INF`.** Skip `INF` entries before adding so `INF + finite` never
  becomes a bogus number.
