# Full 2D Linear Convolution

**Difficulty:** Easy

**Source:** Classic signal/image-processing primitive (equivalent to `scipy.signal.convolve2d(A, B, mode="full")`).

## Description

You are given two integer matrices `A` (size `rA x cA`) and `B` (size `rB x cB`).
Compute their **full 2D linear convolution** `C = A * B`, defined by

```
C[i][j] = sum over all k, l of  A[k][l] * B[i-k][j-l]
```

where the sum runs over every pair `(k, l)` for which both `A[k][l]` and
`B[i-k][j-l]` are inside their matrices.

The result `C` has shape `(rA + rB - 1) x (cA + cB - 1)`. Entry `C[i][j]` collects
every product of an element of `A` and an element of `B` whose index sums equal
`(i, j)`. Convolution is the building block behind image blurring/sharpening,
polynomial multiplication in two variables, and cross-correlation-based pattern
search (correlation is convolution with one operand flipped 180 degrees).

Return the full convolution matrix `C`.

## Constraints

- `1 <= rA, cA, rB, cB <= 1000`
- `-10^4 <= A[k][l], B[k][l] <= 10^4`
- The output has dimensions `(rA + rB - 1) x (cA + cB - 1)`.
- Products and sums fit comfortably in 64-bit integers.

## Examples

### Example 1

```
Input:
  A = [[1, 2],
       [3, 4]]
  B = [[1, 0],
       [0, 1]]

Output:
  [[1, 2, 0],
   [3, 5, 2],
   [0, 3, 4]]
```

**Explanation:** `B` is the 2x2 identity kernel. Convolving with it places a copy of
`A` at the top-left and another copy shifted down-and-right by one, then adds the
overlap. The overlapping center cell is `A[1][1] + A[0][0] = 4 + 1 = 5`.

### Example 2

```
Input:
  A = [[1, 2, 3]]
  B = [[1, 1]]

Output:
  [[1, 3, 5, 3]]
```

**Explanation:** This is 1D convolution of `[1,2,3]` with `[1,1]` (a moving sum of
width 2 with zero padding): `1`, `1+2=3`, `2+3=5`, `3`.

### Example 3

```
Input:
  A = [[1, 2],
       [3, 4]]
  B = [[1, 1],
       [1, 1]]

Output:
  [[1, 3, 2],
   [4, 10, 6],
   [3, 7, 4]]
```

**Explanation:** `B` is the 2x2 box (blur) kernel, so each output cell is the sum of
the (zero-padded) 2x2 neighborhood of `A`. The center `10 = 1+2+3+4` is the sum of
all four entries.

## Hint

Convolution / FFT on 2D data. The naive quadruple loop is `O(rA*cA*rB*cB)`. By the
Convolution Theorem, zero-pad both matrices to `(rA+rB-1) x (cA+cB-1)`, take their
2D FFTs, multiply the spectra element-wise, and invert.
