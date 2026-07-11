# Solution — N-th Fibonacci for Very Large N

## Brute Force

Iterate from the bottom up, keeping the last two terms:

```python
def fibonacci(n):
    a, b = 0, 1            # F(0), F(1)
    for _ in range(n):
        a, b = b, (a + b) % MOD
    return a
```

- **Time:** `O(n)`.
- **Space:** `O(1)`.

This is perfectly fine for `n` up to ~`10^7`, but with `n` up to `10^18` it would take
longer than the age of the universe. We need something sublinear in `n`.

## Optimal Approach — Matrix Exponentiation

### The key identity

Write the state as the column vector `[F(n+1), F(n)]^T`. Then

```
[ F(n+1) ]   [ 1  1 ] [ F(n)   ]
[ F(n)   ] = [ 1  0 ] [ F(n-1) ]
```

because `F(n+1) = 1·F(n) + 1·F(n-1)` and `F(n) = 1·F(n) + 0·F(n-1)`. Call the 2×2 matrix
`M = [[1, 1], [1, 0]]`. Applying `M` once advances the sequence by one step, so applying it
`n` times gives

```
[ F(n+1) ]        [ F(1) ]        [ 1 ]
[ F(n)   ] = M^n  [ F(0) ] = M^n  [ 0 ]
```

A well-known consequence is that

```
M^n = [ F(n+1)  F(n)   ]
      [ F(n)    F(n-1) ]
```

so `F(n)` is simply the top-right (equivalently bottom-left) entry of `M^n`.

### Why it is correct

Matrix multiplication is associative, and `M` exactly encodes one step of the recurrence.
By induction, `M^n` maps the initial state to the state after `n` steps. This is exact
integer arithmetic (we only reduce modulo `10^9 + 7` at the end of each multiply, which is
valid because `+` and `×` commute with taking remainders).

### Fast exponentiation

We never multiply `M` by itself `n` times. Instead we use binary exponentiation
("square and multiply"): repeatedly square the base and multiply the accumulated result in
only when the corresponding bit of `n` is set. That is `O(log n)` matrix multiplications.

### Step by step

1. If `n == 0`, return `0` directly (base case).
2. Start with `result = I` (2×2 identity) and `base = [[1,1],[1,0]]`.
3. While `n > 0`: if the lowest bit of `n` is set, `result = result · base`; then
   `base = base · base` and `n >>= 1`. Reduce every entry mod `10^9 + 7`.
4. Return `result[0][1]` (which equals `F(n)`).

### Reference implementation

```python
MOD = 10**9 + 7

def mat_mult(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) % MOD
             for j in range(2)] for i in range(2)]

def mat_pow(M, p):
    R = [[1, 0], [0, 1]]          # identity
    while p:
        if p & 1:
            R = mat_mult(R, M)
        M = mat_mult(M, M)
        p >>= 1
    return R

def fibonacci(n):
    if n == 0:
        return 0
    M = mat_pow([[1, 1], [1, 0]], n)
    return M[0][1]                # == F(n)
```

- **Time:** `O(k^3 log n)` with `k = 2`, i.e. `O(log n)`.
- **Space:** `O(k^2) = O(1)`.

## Key Insights & Edge Cases

- **The identity `M^n[0][1] = F(n)`** lets you skip building an explicit state vector — you
  can just power the matrix and read one cell.
- **Base case `n = 0`:** `M^0 = I`, whose `[0][1]` entry is `0`, which happens to equal
  `F(0)`, so the code is even correct without a special case; still, handling it explicitly
  is clean.
- **Modular reduction:** apply `% MOD` after every multiply/add so intermediate values stay
  bounded. Because Python has big integers this only affects performance, but in C++/Java it
  is essential to avoid overflow (products of two values near `10^9` need 64-bit arithmetic).
- **`n = 1`** should return `1`; verify your loop's bit handling doesn't accidentally skip
  the last bit.
- **Fibonacci-specific shortcuts** (fast-doubling) exist and are also `O(log n)`; matrix
  exponentiation is the general pattern that extends to *any* linear recurrence, which is why
  we practice it here.
