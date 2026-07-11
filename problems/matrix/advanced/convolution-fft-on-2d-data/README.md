# Convolution / FFT on 2D Data

**Fast 2D pattern correlation via the Fast Fourier Transform.**

## What it is

A 2D **convolution** slides a small kernel/pattern over a larger matrix and, at each
offset, sums the element-wise products. **Cross-correlation** is the same operation
without flipping the kernel — it is exactly what "how well does this pattern line up
with the image at this shift?" means. Both are *bilinear* operations, and the
**Convolution Theorem** says they become simple point-wise multiplication in the
frequency domain:

```
conv(A, B)  =  IFFT2( FFT2(A_padded) * FFT2(B_padded) )
```

So instead of the naive nested loops, you:

1. Zero-pad both matrices to a common size `R x C` where `R >= rA + rB - 1` and
   `C >= cA + cB - 1` (pick powers of two for a fast radix-2 FFT).
2. Take the 2D FFT of each (a 2D FFT = FFT along every row, then FFT along every column).
3. Multiply the two spectra element-wise.
4. Take the inverse 2D FFT and read off the real parts (round for integer data).

For **cross-correlation** you either conjugate one spectrum (`FFT2(A) * conj(FFT2(B))`)
or flip the kernel by 180 degrees before convolving.

## When to reach for it

- You need the convolution/correlation for **every** shift at once (pattern search,
  template matching, image filtering, overlap counting, string/2D matching with
  wildcards).
- The pattern is not tiny relative to the image, so the naive `O(n^2 m^2)` cost hurts.
- Scores are (or can be rewritten as) sums of products of two arrays indexed by a shift.

If the pattern is very small (say `3 x 3`) or you only need one alignment, the direct
loop is simpler and often faster in practice — reach for FFT when the total work
`n^2 * m^2` is large.

## Typical complexity

| Approach | Time | Space |
|---|---|---|
| Naive 2D convolution (`n x n` image, `m x m` kernel) | `O(n^2 * m^2)` | `O(n^2)` |
| FFT-based (pad to `N x N`, `N ~ n + m`) | `O(N^2 log N)` | `O(N^2)` |

The FFT itself is `O(K log K)` for a length-`K` transform; a 2D FFT on an `R x C` grid
costs `O(R*C * log(R*C))`.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Full 2D Linear Convolution](problem-01-full-2d-convolution/PROBLEM.md) | Compute the full 2D convolution of two matrices — the core primitive itself. | Easy |
| 2 | [Largest Image Overlap](problem-02-largest-image-overlap/PROBLEM.md) | Max overlapping 1s over all translations of two binary images (LeetCode 835). | Medium |
| 3 | [Count 2D Binary Pattern Matches](problem-03-count-binary-pattern-matches/PROBLEM.md) | Count exact occurrences of a binary sub-grid inside a binary grid via correlation. | Medium |
| 4 | [2D Template Matching (SSD)](problem-04-template-matching-ssd/PROBLEM.md) | Find the window minimizing sum-of-squared-differences to a template. | Hard |
| 5 | [2D Pattern Matching with Wildcards](problem-05-wildcard-pattern-matching/PROBLEM.md) | Locate a pattern containing `?` wildcards using the masked-correlation trick. | Hard |
