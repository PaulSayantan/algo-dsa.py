# 2D Template Matching (Minimum Sum of Squared Differences)

**Difficulty:** Hard

**Source:** Classic image-processing / computer-vision primitive (normalized template matching, e.g. OpenCV `matchTemplate` with `TM_SQDIFF`).

## Description

You are given a grayscale "image" matrix `I` of size `n x m` and a smaller "template"
matrix `Tpl` of size `p x q` (with `p <= n`, `q <= m`), both containing integer
intensities. For every valid top-left anchor `(i, j)` we slide the template over the
image and measure the **sum of squared differences (SSD)**:

```
SSD(i, j) = sum over r, c of ( I[i + r][j + c] - Tpl[r][c] )^2
```

Return the anchor `(i, j)` with the **smallest** SSD (the best-matching location). If
several anchors tie for the minimum, return the one that comes first in row-major order
(smallest `i`, then smallest `j`).

The key algebraic fact: expanding the square gives

```
SSD(i, j) = windowSqSum(i, j)  -  2 * corr(i, j)  +  templateSqSum
```

where `windowSqSum` and `corr` are both sums over a sliding window — the second term
`corr(i, j) = sum I[i+r][j+c] * Tpl[r][c]` is a 2D cross-correlation and is the only
part that mixes both operands, so it can be computed for all shifts at once with FFTs.

## Constraints

- `1 <= p <= n <= 1500`
- `1 <= q <= m <= 1500`
- `0 <= I[i][j], Tpl[r][c] <= 255`
- There are `(n - p + 1) * (m - q + 1)` candidate anchors; at least one exists.

## Examples

### Example 1

```
Input:
  I = [[1, 2, 3, 0],
       [4, 5, 6, 1],
       [7, 8, 9, 2]]
  Tpl = [[5, 6],
         [8, 9]]

Output: (1, 1)
```

**Explanation:** The 2x2 window anchored at `(1, 1)` is exactly `5 6 / 8 9`, identical
to the template, so `SSD(1,1) = 0` — the global minimum. No other window matches
perfectly.

### Example 2

```
Input:
  I = [[0, 0, 0],
       [0, 9, 0],
       [0, 0, 0]]
  Tpl = [[9]]

Output: (1, 1)
```

**Explanation:** With a 1x1 template, `SSD(i,j) = (I[i][j] - 9)^2`. The single `9` sits
at `(1, 1)` where the difference is `0`; every other cell gives `81`.

### Example 3

```
Input:
  I = [[1, 1, 1],
       [1, 1, 1]]
  Tpl = [[2, 2]]

Output: (0, 0)
```

**Explanation:** Every 1x2 window is `[1, 1]`, so `SSD = (1-2)^2 + (1-2)^2 = 2`
everywhere — a tie. The row-major-first anchor `(0, 0)` is returned.

## Hint

Convolution / FFT on 2D data. Expand `(I - Tpl)^2`; `templateSqSum` is constant and
`windowSqSum` is a moving-window sum (prefix sums), so minimizing SSD is the same as
**maximizing the cross-correlation** term `corr(i, j)` after correcting for the window
energy. Compute `corr` for all shifts with 2D FFTs.
