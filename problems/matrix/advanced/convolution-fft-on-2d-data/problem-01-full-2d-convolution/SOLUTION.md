# Solution — Full 2D Linear Convolution

## Brute Force

Directly evaluate the definition. For every output cell `(i, j)`, sum the products
of aligned entries:

```python
def convolve2d_full(A, B):
    rA, cA = len(A), len(A[0])
    rB, cB = len(B), len(B[0])
    R, C = rA + rB - 1, cA + cB - 1
    out = [[0] * C for _ in range(R)]
    for i in range(rA):
        for j in range(cA):
            a = A[i][j]
            if a == 0:
                continue
            for k in range(rB):
                for l in range(cB):
                    out[i + k][j + l] += a * B[k][l]
    return out
```

(The loop is written "scatter" style — for each `A` entry, add its contribution to
every output cell it touches. That is algebraically identical to the definition.)

- **Time:** `O(rA * cA * rB * cB)`. For two `n x n` matrices this is `O(n^4)`.
- **Space:** `O((rA + rB) * (cA + cB))` for the output.

This is fine for small kernels but blows up when both operands are large.

## Optimal Approach (Convolution / FFT on 2D data)

### Why FFT helps

Convolution in the spatial domain equals point-wise multiplication in the frequency
domain — the **Convolution Theorem**. Concretely, if `F` denotes the 2D discrete
Fourier transform then

```
A * B = F^{-1}( F(A) . F(B) )      ( . = element-wise product )
```

as long as both `A` and `B` are zero-padded to a common size that is at least the
size of the output, `(rA + rB - 1) x (cA + cB - 1)`. Padding to that size prevents
the circular ("wrap-around") convolution that a bare DFT would otherwise compute.

### Step by step

1. Compute output dimensions `R = rA + rB - 1`, `C = cA + cB - 1`.
2. Choose FFT dimensions `P >= R`, `Q >= C`. Using powers of two lets you use a
   simple recursive radix-2 FFT.
3. Zero-pad `A` and `B` into `P x Q` complex grids (top-left aligned).
4. Take the 2D FFT of each grid: FFT every row, then FFT every column of the result.
5. Multiply the two spectra element-wise.
6. Take the inverse 2D FFT.
7. The top-left `R x C` block holds the answer; take the real part and round to the
   nearest integer (imaginary parts and fractional noise come only from
   floating-point error).

### Reference implementation

```python
import cmath

def _fft(a, invert):
    n = len(a)
    if n == 1:
        return
    even = a[0::2]
    odd = a[1::2]
    _fft(even, invert)
    _fft(odd, invert)
    ang = (2 * cmath.pi / n) * (1 if invert else -1)
    w, wn = 1 + 0j, cmath.exp(1j * ang)
    for k in range(n // 2):
        t = w * odd[k]
        a[k] = even[k] + t
        a[k + n // 2] = even[k] - t
        if invert:
            a[k] /= 2
            a[k + n // 2] /= 2
        w *= wn

def _fft2(grid, invert):
    for row in grid:                    # transform each row
        _fft(row, invert)
    cols = list(map(list, zip(*grid)))  # transpose
    for col in cols:                    # transform each column
        _fft(col, invert)
    return [list(c) for c in zip(*cols)]  # transpose back

def convolve2d_full(A, B):
    rA, cA = len(A), len(A[0])
    rB, cB = len(B), len(B[0])
    R, C = rA + rB - 1, cA + cB - 1
    P = 1
    while P < R:
        P <<= 1
    Q = 1
    while Q < C:
        Q <<= 1

    fa = [[0j] * Q for _ in range(P)]
    fb = [[0j] * Q for _ in range(P)]
    for i in range(rA):
        for j in range(cA):
            fa[i][j] = complex(A[i][j])
    for i in range(rB):
        for j in range(cB):
            fb[i][j] = complex(B[i][j])

    fa = _fft2(fa, invert=False)
    fb = _fft2(fb, invert=False)
    prod = [[fa[i][j] * fb[i][j] for j in range(Q)] for i in range(P)]
    prod = _fft2(prod, invert=True)

    return [[int(round(prod[i][j].real)) for j in range(C)] for i in range(R)]
```

- **Time:** `O(P*Q * log(P*Q))` where `P, Q` are the padded (power-of-two) sizes,
  roughly `O(N^2 log N)` for `N ~ n + m`. This beats `O(n^4)` when the matrices are
  large.
- **Space:** `O(P*Q)` for the complex work grids.

### Why it is correct

The DFT diagonalizes circular convolution: multiplying transforms and inverting
yields the *cyclic* convolution modulo `P x Q`. By zero-padding so that `P >= R` and
`Q >= C`, no two contributing terms wrap onto the same output index, so the cyclic
convolution equals the desired *linear* convolution on the first `R x C` block.

## Key Insights & Edge Cases

- **Pad to at least the output size**, not just to the input size. Padding only to
  `max(rA, rB)` produces wrap-around (circular) convolution — a classic bug.
- **Correlation vs. convolution:** cross-correlation is convolution with one operand
  rotated 180 degrees, or equivalently `F^{-1}(F(A) . conj(F(B)))`. Every later
  problem in this folder is really correlation dressed up as a matching score.
- **Integer rounding:** with integer inputs the true answer is an integer; round the
  real part and discard the tiny imaginary residue from floating-point error.
- **Small kernels:** if `B` is `3 x 3` or smaller, the naive loop is simpler and
  usually faster — the FFT's constant factors and padding overhead dominate.
- **Degenerate sizes:** a `1 x n` by `1 x m` convolution is ordinary 1D convolution;
  a `1 x 1` operand just scales the other matrix. The formulas still hold.
- **Empty / all-zero inputs:** an all-zero operand yields an all-zero result of the
  correct `(rA+rB-1) x (cA+cB-1)` shape; do not special-case it away silently.
