# Solution — Minimum-Cost Cyclic Schedule of Exactly L Operations

## Brute Force

Fix a starting mode `s`, then do a layered DP over the number of operations:
`dp[e][j]` = min cost of an `e`-operation schedule that started at `s` and is now
in mode `j`, with `dp[e][j] = min_t ( dp[e-1][t] + cost[t][j] )`. The cycle cost
for start `s` is `dp[L][s]`; answer = `min_s dp[L][s]`.

- **Time:** `O(c · L · c²)` if you rerun per start, or `O(L · c²)` if you track
  all starts simultaneously via a full matrix. Either way it is **linear in
  `L`**, which is fatal for `L` up to `10^18`.
- **Space:** `O(c²)`.

Even naive enumeration of schedules is `O(c^L)` and hopeless.

## Optimal Approach (Recognizing a Hidden Tropical Product)

**The key realization.** The DP transition

```
dp[e][j] = min_t ( dp[e-1][t] + cost[t][j] )
```

is *exactly* a min-plus (tropical) matrix product: if you stack the "start = s"
DP rows into a matrix `D` where `D[s][j] = dp[e][j]`, then advancing one
operation is `D_new = D_old ⊙ C`, where `C = cost`. Starting from the tropical
identity `I` (so `D_0[s][j]` is `0` iff `s == j`), after `L` operations
`D_L = I ⊙ C^{⊙L} = C^{⊙L}`, and

```
(C^{⊙L})[s][j] = min cost of an L-operation schedule from mode s to mode j.
```

**Closed walk ⇒ diagonal.** A *cyclic* schedule starts and ends in the same
mode `s`, i.e. `s = j`. So the cost for start `s` is `(C^{⊙L})[s][s]`, and the
overall answer is the **minimum diagonal entry**:

```
answer = min over s of ( C^{⊙L} )[s][s]
```

**Handling huge `L`.** By associativity of the tropical semiring, `C^{⊙L}` is
obtained by fast exponentiation, seeding the accumulator with the tropical
identity (`0` diagonal, `INF` off-diagonal).

**Steps:**

1. Set `C = cost` (diagonal already `INF`: no-op operations are disallowed).
2. Compute `P = C^{⊙L}` by repeated squaring in the tropical semiring.
3. Return `min_i P[i][i]`, or `-1` if all diagonal entries are `INF`.

```python
INF = float("inf")

def tmul(A, B):
    n = len(A)
    R = [[INF] * n for _ in range(n)]
    for i in range(n):
        Ai, Ri = A[i], R[i]
        for t in range(n):
            a = Ai[t]
            if a == INF:
                continue
            Bt = B[t]
            for j in range(n):
                cand = a + Bt[j]
                if cand < Ri[j]:
                    Ri[j] = cand
    return R

def min_cost_cycle(c, cost, L):
    P = [[0 if i == j else INF for j in range(c)] for i in range(c)]  # tropical I
    base = [row[:] for row in cost]
    e = L
    while e > 0:
        if e & 1:
            P = tmul(P, base)
        base = tmul(base, base)
        e >>= 1
    best = min(P[i][i] for i in range(c))
    return -1 if best == INF else best
```

**Why it is correct.** The transition-as-product argument shows `C^{⊙L}` holds
all fixed-length shortest schedule costs; the diagonal restricts to schedules
that return to their start (closed walks of length `L`), which is precisely a
cyclic schedule. Fast exponentiation computes the same matrix in
`O(c³ log L)` by associativity.

- **Time:** `O(c³ · log L)` — `log₂(10^18) ≈ 60` products of `200³`.
- **Space:** `O(c²)`.

## Key Insights & Edge Cases

- **Spotting the product is the whole problem.** The DP looks like a generic
  1-D array recurrence; recognizing `min_t (dp[t] + cost[t][j])` as a tropical
  matrix–vector product (and the all-starts version as a matrix product) is what
  unlocks `log L` exponentiation.
- **Cycle ⇒ read the diagonal.** Closed walks of fixed length `L` correspond to
  diagonal entries of `C^{⊙L}`. Take the min over the diagonal because the start
  mode is free.
- **"No staying" is enforced by the matrix, not by extra logic.** Since
  `cost[i][i] = INF`, the product never uses a self-transition — every operation
  is a genuine mode change, matching the rule.
- **Exactly `L`, so no 0-diagonal on `C`.** Do not add free self-loops to `C`;
  that would let a schedule pad with no-ops and violate "exactly `L`
  operations." (The `0`-diagonal appears only in the identity seed `I`, a
  distinct matrix used to start the exponentiation.)
- **Infeasible cycles.** If some length-`L` closed walk is impossible from every
  mode, all diagonal entries are `INF`; return `-1`.
- **Overflow.** Costs up to `10^6` times `L` up to `10^18` can reach `~10^24`;
  in fixed-width languages, cap sums at a sentinel to avoid wraparound. Python's
  arbitrary-precision integers avoid the issue.
- **Sanity check with the examples.** `L = 3` gives 4 via `0 → 2 → 1 → 0`
  (`1+1+2`); `L = 6` gives 8 by repeating that best 3-cycle twice — a good
  illustration that the optimal long cycle is often a repeated short cycle.
