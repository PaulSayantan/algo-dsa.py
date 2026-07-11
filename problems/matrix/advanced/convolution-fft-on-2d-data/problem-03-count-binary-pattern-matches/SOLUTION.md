# Solution — Count 2D Binary Pattern Matches

## Brute Force

For every candidate anchor `(i, j)`, compare all `p*q` cells against `P`, bailing out
on the first mismatch:

```python
def count_pattern_matches(T, P):
    n, m = len(T), len(T[0])
    p, q = len(P), len(P[0])
    count = 0
    for i in range(n - p + 1):
        for j in range(m - q + 1):
            if all(T[i + r][j + c] == P[r][c]
                   for r in range(p) for c in range(q)):
                count += 1
    return count
```

- **Time:** `O((n - p + 1) * (m - q + 1) * p * q)`, i.e. `O(n*m*p*q)` in the worst
  case (`O(n^2 m^2)` when the pattern is half the text).
- **Space:** `O(1)` extra.

## Optimal Approach (Convolution / FFT on 2D data)

### From "equality" to "zero mismatches"

For binary values `a, b in {0, 1}`, the XOR `a != b` equals `a + b - 2*a*b`. Summing
XOR over a window `(i, j)` gives the number of mismatched cells:

```
mismatch(i, j) = windowOnes(i, j) + patternOnes - 2 * corr(i, j)
```

where

- `patternOnes = sum of P` (a constant),
- `windowOnes(i, j) = sum_{r,c} T[i+r][j+c]` — the count of 1s in the T window,
- `corr(i, j) = sum_{r,c} T[i+r][j+c] * P[r][c]` — the cross-correlation of `T` and `P`.

A window is an **exact match** iff `mismatch(i, j) == 0`. So we just need the two
sum-of-products surfaces `windowOnes` and `corr` at every shift — and both are 2D
correlations computable with FFTs.

### Step by step

1. Compute `patternOnes = sum(P)`.
2. Compute `corr = correlate(T, P)` for all shifts. Correlation = convolution with `P`
   rotated 180 degrees, done with FFTs (pad both to `>= (n + p - 1) x (m + q - 1)`,
   powers of two; FFT, multiply, inverse FFT). Read the valid anchors.
3. Compute `windowOnes = correlate(T, ones(p, q))` for all shifts — either with a
   second FFT or, more cheaply, with a 2D prefix-sum (integral image) of `T`.
4. For each valid anchor `(i, j)`, form `mismatch = windowOnes + patternOnes - 2*corr`
   and count the anchors where it equals `0`.

```python
def count_pattern_matches(T, P):
    p, q = len(P), len(P[0])
    pattern_ones = sum(sum(row) for row in P)

    # corr[i][j] = sum_{r,c} T[i+r][j+c] * P[r][c]  (via FFT convolution + 180-flip)
    revP = [row[::-1] for row in P[::-1]]
    full_corr = convolve2d_full(T, revP)   # from problem 1
    # window_ones[i][j] = sum of the p x q T-window (integral image is fine here)
    window_ones = window_sums(T, p, q)

    n, m = len(T), len(T[0])
    count = 0
    for i in range(n - p + 1):
        for j in range(m - q + 1):
            # align the full-convolution index with anchor (i, j):
            c = full_corr[i + p - 1][j + q - 1]
            mism = window_ones[i][j] + pattern_ones - 2 * c
            if mism == 0:
                count += 1
    return count
```

(`convolve2d_full` is the FFT routine from problem 1; `window_sums` returns the sum of
every `p x q` window via a prefix-sum table in `O(n*m)`. The `+p-1, +q-1` offset maps
the correlation peak in the *full* convolution back to the anchor coordinate.)

### Why it is correct

`corr(i, j)` counts positions where both `T` and `P` are `1`. `windowOnes(i, j)` counts
`T`-ones in the window, `patternOnes` counts `P`-ones. Their combination
`windowOnes + patternOnes - 2*corr` counts exactly the cells where the two disagree
(the inclusion-exclusion for symmetric difference of the two 1-sets). Zero disagreements
means the window equals `P` cell-for-cell.

- **Time:** `O(N^2 log N)` with `N ~ n + p` for the FFT correlation, plus `O(n*m)`
  for the window sums — versus `O(n*m*p*q)` brute force.
- **Space:** `O(N^2)` for the FFT grids.

## Key Insights & Edge Cases

- **Reduce equality to a correlation of mismatches.** The identity
  `[a != b] = a + b - 2ab` is the whole trick; it linearizes exact matching into
  sums of products.
- **Two surfaces, not one.** You need both `corr` (with `P`) and `windowOnes` (with an
  all-ones kernel). Skipping `windowOnes` silently assumes the pattern is all ones.
- **Index alignment.** A full convolution places the correlation for anchor `(i, j)`
  at offset `(i + p - 1, j + q - 1)`; get this off-by-one wrong and every count shifts.
- **All-zero pattern.** `patternOnes = 0`, so a window matches iff it is all zeros —
  the formula handles it without special casing (see Example 3).
- **Floating-point rounding.** Round the FFT result to the nearest integer before the
  `== 0` test; comparing raw floats to zero is unsafe.
- **Prefer prefix sums for `windowOnes`.** The all-ones correlation is a plain moving
  window sum; an integral image computes it in `O(n*m)` and avoids a second FFT.
