# Solution — Number of Walks of Length K in a Graph

## Brute Force

Do a step-by-step DP. Let `cnt[v]` be the number of walks of length `t` from `src` to `v`.
Start with `cnt[src] = 1`, and at each of the `k` steps push counts along edges:

```python
def count_walks(adj, src, dst, k):
    V = len(adj)
    cnt = [0] * V
    cnt[src] = 1
    for _ in range(k):
        nxt = [0] * V
        for u in range(V):
            if cnt[u]:
                for v in range(V):
                    if adj[u][v]:
                        nxt[v] = (nxt[v] + cnt[u]) % MOD
        cnt = nxt
    return cnt[dst]
```

- **Time:** `O(k · V^2)`.
- **Space:** `O(V)`.

For `k` up to `10^18` this is impossibly slow — we need to remove the linear dependence on `k`.

## Optimal Approach — Powers of the Adjacency Matrix

### The counting theorem

Let `A` be the adjacency matrix. Then **`(A^k)[i][j]` equals the number of walks of length
exactly `k` from `i` to `j`.**

*Why:* prove by induction on `k`. For `k = 1`, `A^1 = A` and `A[i][j]` is `1` iff there is a
single edge `i -> j` — exactly the number of length-1 walks. For the inductive step, every
length-`k` walk `i -> ... -> j` splits uniquely as a length-`(k-1)` walk `i -> ... -> m`
followed by one edge `m -> j`. Summing over the intermediate node `m`:

```
(A^k)[i][j] = sum over m of (A^(k-1))[i][m] * A[m][j]
```

which is exactly the definition of the matrix product `A^(k-1) · A = A^k`. Done.

### Algorithm

1. Compute `B = A^k` using binary (fast) exponentiation of matrices — `O(log k)` matrix
   multiplications, each `O(V^3)`.
2. Return `B[src][dst] mod (10^9 + 7)`.

### Worked check (Example 2)

`A` is the 3×3 all-ones-off-diagonal matrix (the triangle). Squaring gives
`A^2 = [[2,1,1],[1,2,1],[1,1,2]]` (from each node there are 2 length-2 walks back to itself
and 1 to each other node). Multiplying once more:
`A^3 = [[2,3,3],[3,2,3],[3,3,2]]`. Thus `A^3[0][1] = 3`, matching the three enumerated walks
`0->1->0->1`, `0->2->0->1`, `0->1->2->1`.

### Reference implementation

```python
MOD = 10**9 + 7

def mat_mult(A, B):
    n, m, p = len(A), len(B[0]), len(B)
    C = [[0] * m for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        Ci = C[i]
        for kk in range(p):
            a = Ai[kk]
            if a:
                Bk = B[kk]
                for j in range(m):
                    Ci[j] = (Ci[j] + a * Bk[j]) % MOD
    return C

def mat_pow(M, p):
    n = len(M)
    R = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    while p:
        if p & 1:
            R = mat_mult(R, M)
        M = mat_mult(M, M)
        p >>= 1
    return R

def count_walks(adj, src, dst, k):
    B = mat_pow([row[:] for row in adj], k)
    return B[src][dst] % MOD
```

- **Time:** `O(V^3 log k)`.
- **Space:** `O(V^2)`.

## Key Insights & Edge Cases

- **"Exactly k" vs "at most k":** matrix powers count walks of *exactly* length `k`. If you
  need "at most `k`", add an extra absorbing state / augment the matrix, or sum
  `A^1 + ... + A^k` (which itself can be done in `O(V^3 log k)` with a block-matrix trick).
- **Directed vs undirected:** the theorem holds for both; for undirected graphs `A` is
  symmetric, so `A^k` stays symmetric.
- **Self-loops and multigraphs:** if `adj[i][j]` can exceed 1 (parallel edges), the same
  proof still counts walks weighted by edge multiplicity — no change needed.
- **`k = 0`:** `A^0 = I`, so there is exactly one length-0 walk from a node to itself and none
  otherwise; the constraints here start at `k = 1`, but keep this in mind.
- **Modulus:** reduce after each multiply-add. With `V` up to 100, each entry sums up to 100
  products of values `< 10^9`, which fits in 64-bit before reduction.
- **Reusing the input:** copy `adj` before powering if the caller may reuse it; `mat_pow`
  above squares its argument in place conceptually but works on a fresh copy.
