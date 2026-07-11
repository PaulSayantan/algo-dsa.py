# Largest Image Overlap

**Difficulty:** Medium

**Source:** LeetCode 835 — Image Overlap.

## Description

You are given two `n x n` binary matrices `img1` and `img2`.

We translate one image over the other (slide it left/right and up/down, **without
rotating**). After a translation, the **overlap** is the number of positions where
both images have a `1`. Any part of an image that slides off the grid is discarded.

Return the **largest possible overlap** over all translations.

Equivalently, for every shift `(dr, dc)` count how many cells satisfy
`img1[i][j] == 1` **and** `img2[i + dr][j + dc] == 1` (with `(i+dr, j+dc)` in bounds),
and return the maximum count. This is exactly the **cross-correlation** of the two
binary images evaluated at its peak.

## Constraints

- `n == img1.length == img1[i].length == img2.length == img2[i].length`
- `1 <= n <= 30`
- `img1[i][j]` and `img2[i][j]` are each `0` or `1`.

## Examples

### Example 1

```
Input:
  img1 = [[1,1,0],
          [0,1,0],
          [0,1,0]]
  img2 = [[0,0,0],
          [0,1,1],
          [0,0,1]]

Output: 3
```

**Explanation:** Translate `img1` one unit to the right and one unit down. Then the
three 1s at `img1` positions `(0,1)`, `(1,1)`, `(2,1)` line up with the 1s of `img2`
at `(1,2)`, `(2,2)`... i.e. exactly three 1s coincide, which is the maximum.

### Example 2

```
Input:
  img1 = [[1]]
  img2 = [[1]]

Output: 1
```

**Explanation:** A single 1 in each image; with zero shift they overlap, giving 1.

### Example 3

```
Input:
  img1 = [[0]]
  img2 = [[0]]

Output: 0
```

**Explanation:** Neither image contains a 1, so no translation can produce any
overlap.

## Hint

Convolution / FFT on 2D data. The overlap count as a function of shift `(dr, dc)`
is the cross-correlation of `img1` and `img2`. For `n <= 30` a direct
shift-and-count is enough, but the same answer equals the peak of
`IFFT2(FFT2(img1) * conj(FFT2(img2)))`.
