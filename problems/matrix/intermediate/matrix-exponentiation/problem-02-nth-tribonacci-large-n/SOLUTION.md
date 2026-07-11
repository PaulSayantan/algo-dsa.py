# Solution — N-th Tribonacci for Very Large N

## Brute Force

Roll three variables forward:

```python
def tribonacci(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    a, b, c = 0, 1, 1     # T(0), T(1), T(2)
    for _ in range(3, n + 1):
        a, b, c = b, c, (a + b + c) % MOD
    return c
```

- **Time:** `O(n)`.
- **Space:** `O(1)`.

Fine for small `n`, hopeless for `n` up to `10^18`.

## Optimal Approach — Matrix Exponentiation

### Build the transition matrix

Use the state column vector `[T(n), T(n-1), T(n-2)]^T`. One step forward is:

```
[ T(n+1) ]   [ 1  1  1 ] [ T(n)   ]
[ T(n)   ] = [ 1  0  0 ] [ T(n-1) ]
[ T(n-1) ]   [ 0  1  0 ] [ T(n-2) ]
```

Reading the rows:

- Row 0: `T(n+1) = 1·T(n) + 1·T(n-1) + 1·T(n-2)` — the recurrence.
- Row 1: `T(n)   = 1·T(n) + 0 + 0` — just copies the previous top entry down.
- Row 2: `T(n-1) = 0 + 1·T(n-1) + 0` — copies the middle entry down.

Call this matrix `M = [[1,1,1],[1,0,0],[0,1,0]]`.

### Advancing n steps

The base state (largest indices we know directly) is `v_2 = [T(2), T(1), T(0)]^T = [1,1,0]^T`.
For `n >= 2`,

```
[ T(n)   ]
[ T(n-1) ] = M^(n-2) · v_2
[ T(n-2) ]
```

so `T(n)` is the top entry of `M^(n-2) · [1,1,0]^T`. Handle `n = 0, 1, 2` directly
(`0, 1, 1`).

### Why it is correct

`M` encodes exactly one application of the recurrence, and matrix multiplication is
associative, so `M^(n-2)` maps the known state `v_2` to the state at index `n`. Same argument
as Fibonacci, just with a 3-dimensional state.

### Reference implementation

```python
MOD = 10**9 + 7

def mat_mult(A, B):
    n, m, p = len(A), len(B[0]), len(B)
    C = [[0] * m for _ in range(n)]
    for i in range(n):
        for k in range(p):
            if A[i][k]:
                aik = A[i][k]
                row = C[i]
                brow = B[k]
                for j in range(m):
                    row[j] = (row[j] + aik * brow[j]) % MOD
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

def tribonacci(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    M = mat_pow([[1, 1, 1], [1, 0, 0], [0, 1, 0]], n - 2)
    # v2 = [T(2), T(1), T(0)] = [1, 1, 0]
    return (M[0][0] * 1 + M[0][1] * 1 + M[0][2] * 0) % MOD
```

- **Time:** `O(k^3 log n)` with `k = 3`, i.e. `O(27 log n) = O(log n)`.
- **Space:** `O(k^2) = O(1)`.

## Key Insights & Edge Cases

- **The matrix pattern generalizes:** for a `k`-term linear recurrence
  `f(n) = c1 f(n-1) + ... + ck f(n-k)`, the top row of `M` holds the coefficients
  `[c1, c2, ..., ck]` and the remaining `k-1` rows form a shifted identity that "slides" old
  values down. Fibonacci is the `k = 2` special case; Tribonacci is `k = 3`.
- **Base cases:** `n = 0, 1, 2` must be returned directly because the formula uses `M^(n-2)`,
  which is only meaningful for `n >= 2`. `M^0 = I` correctly handles `n = 2`, but returning it
  explicitly avoids an empty-power edge in some implementations.
- **Off-by-one in the exponent:** a common bug is powering `M^n` instead of `M^(n-2)`; anchor
  yourself to the known base index (here, index 2) and count how many steps you still need.
- **Modular arithmetic:** reduce after each add/multiply; in fixed-width languages the product
  of two `~10^9` values needs 64-bit storage.
