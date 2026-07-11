# Count 2D Binary Pattern Matches

**Difficulty:** Medium

**Source:** Classic competitive-programming problem (2D pattern matching via FFT).

## Description

You are given a binary "text" grid `T` of size `n x m` and a smaller binary "pattern"
grid `P` of size `p x q` (with `p <= n` and `q <= m`). All entries are `0` or `1`.

A pattern **occurrence** is a top-left position `(i, j)` such that the `p x q` sub-grid
of `T` anchored at `(i, j)` equals `P` **exactly** in every cell:

```
T[i + r][j + c] == P[r][c]   for all 0 <= r < p, 0 <= c < q
```

Return the **number** of positions `(i, j)` (with `0 <= i <= n - p` and
`0 <= j <= m - q`) at which `P` occurs.

The trick: a window matches iff the number of *mismatched* cells is zero. The number
of mismatches at a shift can be written as a sum of cross-correlations, so all windows
can be scored simultaneously with 2D FFTs.

## Constraints

- `1 <= p <= n <= 2000`
- `1 <= q <= m <= 2000`
- `T[i][j]`, `P[r][c]` are each `0` or `1`.
- There are exactly `(n - p + 1) * (m - q + 1)` candidate top-left positions.

## Examples

### Example 1

```
Input:
  T = [[1,0,1,0],
       [0,1,0,1],
       [1,0,1,0]]
  P = [[1,0],
       [0,1]]

Output: 3
```

**Explanation:** `P` (the "checkerboard step" `1 0 / 0 1`) appears anchored at
`(0,0)`, `(0,2)`, and `(1,1)`. Anchor `(1,0)` gives `0 1 / 1 0`, which does not match.
So there are 3 occurrences.

### Example 2

```
Input:
  T = [[1,1,1],
       [1,1,1],
       [1,1,1]]
  P = [[1,1],
       [1,1]]

Output: 4
```

**Explanation:** The all-ones 2x2 pattern fits at the 4 anchors
`(0,0), (0,1), (1,0), (1,1)` — every 2x2 window of an all-ones 3x3 grid matches.

### Example 3

```
Input:
  T = [[1,0],
       [0,1]]
  P = [[0,0],
       [0,0]]

Output: 0
```

**Explanation:** The only candidate window is `T` itself (`1 0 / 0 1`), which is not
all zeros, so the all-zero pattern never occurs.

## Hint

Convolution / FFT on 2D data. Count mismatches per shift as
`ones(T-window) + ones(P) - 2 * (T correlated with P)` restricted to the 1-cells;
a window is an exact match exactly when its mismatch count is 0. Compute the
correlation term with 2D FFTs.
