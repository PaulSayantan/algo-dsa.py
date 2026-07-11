# Solution — 2D Pattern Matching with Wildcards

## Brute Force

For each anchor, compare every pattern cell, treating `'?'` as an automatic pass:

```python
def find_matches(T, P):
    n, m = len(T), len(T[0])
    p, q = len(P), len(P[0])
    res = []
    for i in range(n - p + 1):
        for j in range(m - q + 1):
            ok = True
            for r in range(p):
                for c in range(q):
                    pc = P[r][c]
                    if pc != '?' and pc != T[i + r][j + c]:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                res.append((i, j))
    return res
```

- **Time:** `O((n - p + 1)(m - q + 1) * p * q)`, i.e. `O(n*m*p*q)`.
- **Space:** `O(1)` beyond the output.

## Optimal Approach (Convolution / FFT on 2D data)

### The masked-mismatch identity

Map each real character to a **positive** integer (so no real char is `0`). Build a
numeric pattern grid `p[r][c]` and a **mask** grid:

```
mask[r][c] = 0 if P[r][c] == '?'   else 1
```

Define the wildcard-aware mismatch score at anchor `(i, j)`:

```
mismatch(i, j) = sum_{r,c} mask[r][c] * ( T[i+r][j+c] - p[r][c] )^2
```

- Where `P` has a real character, `mask = 1`, so the term is `(t - p)^2`, which is `0`
  iff the characters are equal (they are distinct positive integers) and positive
  otherwise.
- Where `P` has `'?'`, `mask = 0`, so that cell contributes nothing — exactly the
  "matches anything" semantics.

Therefore `mismatch(i, j) == 0` **iff** the window matches the pattern.

### Expand into correlations

Expand the square and distribute the mask:

```
mismatch(i, j) = sum mask*T^2            (A)
               - 2 * sum (mask*p) * T    (B)
               + sum mask*p^2            (C, a constant)
```

Term by term, treating each as a correlation of the text (or `T^2`) with a
pattern-derived kernel:

- **(A)** `sum_{r,c} mask[r][c] * T[i+r][j+c]^2` = correlation of `T .* T` (element-wise
  square of the text) with the kernel `mask`.
- **(B)** `sum_{r,c} (mask[r][c]*p[r][c]) * T[i+r][j+c]` = correlation of `T` with the
  kernel `mask .* p`.
- **(C)** `sum_{r,c} mask[r][c] * p[r][c]^2` — a single constant, precomputed in
  `O(p*q)`.

Each correlation is one FFT convolution (flip the kernel 180 degrees, pad, 2D FFT,
multiply, inverse 2D FFT). So the whole thing is **two** 2D FFT correlations plus a
constant.

### Step by step

1. Encode characters as positive integers; build numeric `T`, numeric `p`, and `mask`.
2. Precompute `constC = sum mask[r][c] * p[r][c]^2`.
3. `A = correlate(T .* T, mask)` via FFT.
4. `B = correlate(T, mask .* p)` via FFT.
5. For each valid anchor, `mismatch = A - 2*B + constC`; collect anchors where it is
   `0` (after rounding), in row-major order.

```python
def find_matches(T, P):
    n, m = len(T), len(T[0])
    p, q = len(P), len(P[0])
    code = {}                                  # map chars -> 1, 2, 3, ...
    def enc(ch):
        return code.setdefault(ch, len(code) + 1)

    Tn  = [[enc(ch) for ch in row] for row in T]
    Pn  = [[0 if ch == '?' else enc(ch) for ch in row] for row in P]
    msk = [[0 if ch == '?' else 1 for ch in row] for row in P]

    const_c = sum(msk[r][c] * Pn[r][c] ** 2 for r in range(p) for c in range(q))
    T_sq    = [[v * v for v in row] for row in Tn]
    mask_p  = [[msk[r][c] * Pn[r][c] for c in range(q)] for r in range(p)]

    A = correlate_fft(T_sq, msk)      # full 2D convolution with 180-rotated kernel
    B = correlate_fft(Tn,   mask_p)   #   (each returns a full-convolution grid)

    res = []
    for i in range(n - p + 1):
        for j in range(m - q + 1):
            a = A[i + p - 1][j + q - 1]   # align full-convolution index to anchor
            b = B[i + p - 1][j + q - 1]
            if a - 2 * b + const_c == 0:
                res.append((i, j))
    return res
```

(`correlate_fft(X, K)` = full 2D convolution of `X` with `K` rotated 180 degrees, using
the FFT routine from problem 1, rounded to integers.)

### Why it is correct

The identity `mismatch = A - 2B + C` is an exact expansion of
`sum mask*(T - p)^2`. Every summand is non-negative, and a summand is `0` iff its cell
is a wildcard (mask `0`) or the characters agree (`(t-p)^2 = 0`, using distinct positive
codes so different characters always differ). Hence the total is `0` precisely at true
matches. FFT computes each correlation exactly up to floating-point error, removed by
rounding integer results.

- **Time:** `O(N^2 log N)` with `N ~ n + p`, dominated by two FFT correlations —
  versus `O(n*m*p*q)` brute force.
- **Space:** `O(N^2)` for the FFT grids.

## Key Insights & Edge Cases

- **Wildcards become a `0` mask.** Multiplying every squared-difference term by the mask
  is the whole idea: masked cells vanish, so `'?'` truly matches anything.
- **Use distinct positive codes.** If a real character were coded `0`, it would collide
  with the wildcard encoding and the `(t - p)^2` test could misfire. Start codes at `1`.
- **Two correlations suffice in 2D.** The general (both sides wildcarded) formula needs
  three; here only the pattern has wildcards, so the mask-on-text terms collapse and you
  need `A` (mask vs `T^2`) and `B` (mask*p vs `T`) plus the constant `C`.
- **Index alignment.** As in problems 3 and 4, a full convolution stores anchor
  `(i, j)`'s correlation at offset `(i + p - 1, j + q - 1)`.
- **All-wildcard pattern.** Then `mask` is all zeros, so `A`, `B`, and `C` are all `0`
  and every fitting anchor matches (see Example 3).
- **Floating-point rounding.** Round each correlation to the nearest integer before the
  `== 0` test; never compare raw FFT floats to zero.
- **1D specialization.** With a single row this is exactly Clifford & Clifford's
  FFT string matching with wildcards — the 2D version just runs the FFT over both axes.
