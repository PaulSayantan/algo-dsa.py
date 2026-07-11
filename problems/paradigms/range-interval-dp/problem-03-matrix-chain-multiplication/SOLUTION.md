# Matrix Chain Multiplication — Solution

## Brute Force

Try every way to parenthesize the chain. The number of full parenthesizations of
`n` matrices is the Catalan number `C(n-1)`, so a naive recursion that picks a
top-level split and recurses on both sides — without memoization — is
exponential.

- **Time:** `O(Catalan(n)) ≈ O(4^n / n^{1.5})`.
- **Space:** `O(n)` recursion depth.

## Optimal Approach (Range / Interval DP)

This is *the* canonical interval DP. The subproblem is a **contiguous sub-chain**
of matrices.

> `dp[i][j]` = minimum scalar multiplications to compute the product
> `A[i] * A[i+1] * … * A[j]` (1-indexed matrices).

Whatever the optimal order, the **last multiplication** combines two already-
computed products: `(A[i..k]) * (A[k+1..j])` for some split `k` with
`i <= k < j`. The left product has dimensions `dims[i-1] x dims[k]`, the right
has `dims[k] x dims[j]`, so that final multiply costs
`dims[i-1] * dims[k] * dims[j]`.

**Recurrence** (split by the outermost multiplication `k`):
```
dp[i][j] = min over k in [i, j) of
           dp[i][k] + dp[k+1][j] + dims[i-1] * dims[k] * dims[j]
```

**Base case:** `dp[i][i] = 0` — a single matrix needs no multiplication.

**Why it is correct.** Any parenthesization has a unique outermost split; fixing
it makes the left and right groups independent subproblems whose costs add,
plus the fixed cost of the final multiply. Minimizing over all splits `k`
considers every possible outermost cut, hence every parenthesization.

**Iteration order.** Increasing sub-chain length, so both halves are ready.

```python
def matrix_chain_order(dims):
    n = len(dims) - 1            # number of matrices, 1..n
    if n <= 1:
        return 0
    # 1-indexed matrices; dp sized (n+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for length in range(2, n + 1):          # chain length
        for i in range(1, n - length + 2):
            j = i + length - 1
            best = float("inf")
            for k in range(i, j):
                cost = (dp[i][k] + dp[k + 1][j]
                        + dims[i - 1] * dims[k] * dims[j])
                best = min(best, cost)
            dp[i][j] = best
    return dp[1][n]
```

- **Time:** `O(n^3)` — `O(n^2)` sub-chains times `O(n)` splits.
- **Space:** `O(n^2)`. (Knuth's optimization can bring this specific DP to
  `O(n^2)` time, but `O(n^3)` is the standard expectation.)

### Trace for `dims = [10, 30, 5, 60]`

Matrices: A1(10x30), A2(30x5), A3(5x60). Only `dp[1][3]` needs a choice:
- `k = 1`: `dp[1][1] + dp[2][3] + 10*30*60 = 0 + (30*5*60) + 18000 = 9000 + 18000 = 27000`.
- `k = 2`: `dp[1][2] + dp[3][3] + 10*5*60 = (10*30*5) + 0 + 3000 = 1500 + 3000 = 4500`.

Minimum is `4500`.

## Key Insights & Edge Cases

- The split index `k` marks the **last** multiplication, not a position in the
  data — the fixed cost `dims[i-1]*dims[k]*dims[j]` is the "glue" of the merge.
- **Off-by-one with `dims`:** matrix `A[i]` is `dims[i-1] x dims[i]`. Getting this
  wrong is the most common bug. Sub-chain `A[i..j]` yields a `dims[i-1] x dims[j]`
  matrix.
- **Fewer than 2 matrices** (`len(dims) <= 2`) means at most one matrix, so the
  answer is `0`.
- The DP finds the minimum *cost*; to recover the actual parenthesization, store
  the argmin `k` for each `(i, j)` in a separate `split[i][j]` table.
- Watch for large products; use a 64-bit / arbitrary-precision integer type
  (Python's `int` is fine).
