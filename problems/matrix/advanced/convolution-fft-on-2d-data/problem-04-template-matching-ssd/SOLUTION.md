# Solution — 2D Template Matching (Minimum SSD)

## Brute Force

Score every anchor by directly summing squared differences:

```python
def best_match(I, Tpl):
    n, m = len(I), len(I[0])
    p, q = len(Tpl), len(Tpl[0])
    best_ssd = None
    best_pos = None
    for i in range(n - p + 1):
        for j in range(m - q + 1):
            s = 0
            for r in range(p):
                for c in range(q):
                    d = I[i + r][j + c] - Tpl[r][c]
                    s += d * d
            if best_ssd is None or s < best_ssd:
                best_ssd, best_pos = s, (i, j)
    return best_pos
```

- **Time:** `O((n - p + 1)(m - q + 1) * p * q)`, i.e. `O(n*m*p*q)` (up to `O(n^2 m^2)`).
- **Space:** `O(1)` extra.

## Optimal Approach (Convolution / FFT on 2D data)

### Expand the square

```
SSD(i, j) = sum_{r,c} (I[i+r][j+c] - Tpl[r][c])^2
          = sum_{r,c} I[i+r][j+c]^2            (windowSqSum(i, j))
          - 2 * sum_{r,c} I[i+r][j+c]*Tpl[r][c] (2 * corr(i, j))
          + sum_{r,c} Tpl[r][c]^2               (templateSqSum, a constant)
```

Three pieces:

- `templateSqSum` — a single constant, computed once in `O(p*q)`.
- `windowSqSum(i, j)` — the sum of squared image intensities inside the window. Square
  the image once, then use a **2D prefix-sum (integral image)** to get every window
  sum in `O(1)`; total `O(n*m)`.
- `corr(i, j) = sum I[i+r][j+c] * Tpl[r][c]` — the **cross-correlation** of image and
  template. This is the only term coupling both operands over all shifts, and it is
  exactly what FFT computes cheaply.

Because `templateSqSum` is constant, minimizing SSD means minimizing
`windowSqSum - 2*corr`. (If additionally the window energy were constant — e.g. a
normalized image — minimizing SSD would reduce to *maximizing the correlation*.)

### Step by step

1. `templateSqSum = sum(Tpl[r][c]^2)`.
2. Build the integral image of `I .* I` to get `windowSqSum(i, j)` in `O(1)` each.
3. Compute `corr` for all valid anchors with an FFT correlation: flip `Tpl` 180
   degrees, convolve with `I` (pad to `>= (n+p-1) x (m+q-1)`, powers of two; 2D FFT,
   element-wise multiply, inverse 2D FFT), and round to integers.
4. For each anchor combine `SSD = windowSqSum - 2*corr + templateSqSum` and track the
   minimum, breaking ties by row-major order.

```python
def best_match(I, Tpl):
    n, m = len(I), len(I[0])
    p, q = len(Tpl), len(Tpl[0])
    tpl_sq = sum(v * v for row in Tpl for v in row)

    # corr via FFT: convolve I with the 180-degree-rotated template
    revT = [row[::-1] for row in Tpl[::-1]]
    full = convolve2d_full(I, revT)                 # from problem 1
    win_sq = window_sums([[v * v for v in row] for row in I], p, q)  # integral image

    best = None
    best_pos = None
    for i in range(n - p + 1):
        for j in range(m - q + 1):
            corr = full[i + p - 1][j + q - 1]       # align to anchor (i, j)
            ssd = win_sq[i][j] - 2 * corr + tpl_sq
            if best is None or ssd < best:          # strict < keeps first on ties
                best, best_pos = ssd, (i, j)
    return best_pos
```

### Why it is correct

The expansion of `(I - Tpl)^2` is an exact algebraic identity, so the reconstructed
`SSD(i, j)` equals the brute-force value at every anchor; the argmin is therefore the
same. The FFT correlation is exact up to floating-point error (rounded away for integer
data), and the integral image reproduces `windowSqSum` exactly. Using strict `<` when
updating the best keeps the earliest anchor on ties, satisfying the tie-break rule.

- **Time:** `O(N^2 log N)` for the FFT (`N ~ n + p`) plus `O(n*m)` for the integral
  image — a big win over `O(n*m*p*q)` when the template is large.
- **Space:** `O(N^2)` for the FFT grids and `O(n*m)` for the prefix-sum table.

## Key Insights & Edge Cases

- **SSD splits into constant + window energy + correlation.** Only the correlation
  needs the FFT; the rest are constants or prefix sums.
- **Argmin of SSD = argmax of correlation only after correcting for window energy.**
  If image regions differ in brightness, dropping `windowSqSum` picks bright regions,
  not similar ones — a classic template-matching pitfall (hence *normalized* matching).
- **Index alignment.** As in problem 3, the full convolution places anchor `(i, j)`'s
  correlation at offset `(i + p - 1, j + q - 1)`.
- **Tie-breaking.** Iterate anchors in row-major order and update only on strictly
  smaller SSD to return the first minimizer.
- **Integer rounding.** Round the inverse-FFT correlation to the nearest integer before
  combining; otherwise floating-point noise can flip a `0`-SSD exact match.
- **Overflow.** With intensities up to 255 and large windows, `windowSqSum` can be
  large; use 64-bit integers (Python ints are unbounded, so this is a note for ported
  code).
- **Degenerate template.** A `1 x 1` template reduces SSD to `(I[i][j] - Tpl)^2`; the
  formula and FFT path still work (the FFT is overkill here but not wrong).
