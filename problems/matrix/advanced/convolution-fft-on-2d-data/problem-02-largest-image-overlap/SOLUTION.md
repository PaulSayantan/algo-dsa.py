# Solution — Largest Image Overlap

## Brute Force

Try every translation `(dr, dc)` with `dr, dc` in `[-(n-1), n-1]`, and for each count
coinciding 1s:

```python
class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)
        best = 0
        for dr in range(-(n - 1), n):
            for dc in range(-(n - 1), n):
                cnt = 0
                for i in range(n):
                    for j in range(n):
                        ni, nj = i + dr, j + dc
                        if (img1[i][j] == 1 and 0 <= ni < n and 0 <= nj < n
                                and img2[ni][nj] == 1):
                            cnt += 1
                best = max(best, cnt)
        return best
```

- **Time:** `O(n^4)` — `O(n^2)` shifts times `O(n^2)` per count.
- **Space:** `O(1)` beyond the inputs.

A common interview-grade optimization: collect the coordinates of the 1s in each
image, then for every pair `(a in img1, b in img2)` increment a hashmap keyed by the
shift `b - a`; the busiest bucket is the answer. That is `O(k1 * k2)` where `k1, k2`
are the counts of 1s — still quadratic in the worst case (`k ~ n^2`).

## Optimal Approach (Convolution / FFT on 2D data)

### Key reduction

The overlap as a function of shift is precisely the **cross-correlation** of the two
binary images:

```
overlap(dr, dc) = sum over i, j of  img1[i][j] * img2[i + dr][j + dc]
```

Cross-correlation equals convolution with one operand rotated 180 degrees. So:

1. Build `rev2 = img2` rotated 180 degrees (reverse rows and columns).
2. Compute the **full 2D convolution** `img1 * rev2` (see problem 1) via FFT: pad both
   to `P x Q` with `P, Q >= 2n - 1` (powers of two), take 2D FFTs, multiply, invert.
3. Every entry of the resulting `(2n-1) x (2n-1)` correlation surface is the overlap
   count for one shift. The **maximum** entry is the answer.

Equivalently, skip the manual flip and multiply by the conjugate spectrum:
`corr = IFFT2( FFT2(img1) * conj(FFT2(img2)) )`.

```python
# Using the flip-then-convolve view with the FFT convolution from problem 1:
def largestOverlap(img1, img2):
    rev2 = [row[::-1] for row in img2[::-1]]   # rotate img2 by 180 degrees
    corr = convolve2d_full(img1, rev2)         # full 2D convolution via FFT
    return max(max(row) for row in corr) if corr else 0
```

### Why it is correct

Rotating `img2` by 180 degrees turns the flip inside the convolution sum back into a
plain shift, so `(img1 * rev2)[i][j]` equals `sum img1[k][l] * img2[k - i + off, ...]`
— i.e. the overlap for one specific translation. The full convolution enumerates
every valid overlap (each shift maps to a distinct output index), and out-of-bounds
cells contribute `0` because they were zero-padded. Taking the max over the surface
therefore returns the best achievable overlap.

- **Time:** `O(N^2 log N)` with `N ~ 2n`, dominated by the three 2D FFTs.
- **Space:** `O(N^2)` for the padded complex grids.

## Key Insights & Edge Cases

- **Correlation, not convolution:** the overlap has *no* flip, so you must flip one
  image before a convolution routine, or use the conjugate-spectrum form.
- **Pad to `2n - 1` per axis** (round up to a power of two) so the correlation for the
  extreme shifts does not wrap around.
- **Practicality:** with `n <= 30` the brute force / coordinate-pair method is
  perfectly fast and simpler; FFT shines when `n` grows into the hundreds or the same
  correlation is needed repeatedly. This problem is the canonical illustration that
  "count matches over all shifts" *is* a correlation.
- **All-zero images:** the correlation surface is all zeros, so the max is `0` — no
  special casing needed.
- **Integer rounding:** binary inputs give integer correlations; round the real part
  of the inverse FFT to kill floating-point noise.
- **Off-by-one on the max:** remember to take the maximum over the *entire*
  `(2n-1) x (2n-1)` surface, including the borders, not just the central `n x n` block.
