# 2D Pattern Matching with Wildcards

**Difficulty:** Hard

**Source:** Classic FFT string-matching-with-wildcards result (Clifford & Clifford, 2007), lifted to two dimensions.

## Description

You are given a "text" grid `T` of size `n x m` and a "pattern" grid `P` of size
`p x q` (`p <= n`, `q <= m`). Both grids contain single characters. In addition, the
pattern may contain the **wildcard** character `'?'`, which matches **any** text
character.

A pattern **occurrence** at top-left anchor `(i, j)` means that for every pattern cell,
either the pattern cell is `'?'` or it equals the aligned text cell:

```
for all r, c:  P[r][c] == '?'  OR  P[r][c] == T[i + r][j + c]
```

Return the list of all matching anchors `(i, j)` (with `0 <= i <= n - p`,
`0 <= j <= m - q`) in row-major order.

The classic reduction: map each character to a number, and encode a wildcard cell as
`0` in a *pattern mask*. Then the quantity

```
mismatch(i, j) = sum over r, c of  mask[r][c] * ( T[i+r][j+c] - P[r][c] )^2
```

is zero **exactly** when the window matches (every non-wildcard cell agrees, and
wildcard cells are ignored because their mask is `0`). Expanding the square turns
`mismatch` into a handful of 2D cross-correlations, all computable with FFTs.

## Constraints

- `1 <= p <= n <= 1500`
- `1 <= q <= m <= 1500`
- Text characters come from a fixed alphabet; the pattern uses the same alphabet plus
  the wildcard `'?'`.
- Map characters to positive integers (so wildcards, encoded as `0`, are distinct from
  real characters).

## Examples

### Example 1

```
Input:
  T = [['a','b','a','b'],
       ['b','a','b','a'],
       ['a','b','a','b']]
  P = [['a','?'],
       ['?','a']]

Output: [(0, 0), (0, 2), (1, 1)]
```

**Explanation:** The pattern requires `a` at its top-left and bottom-right corners and
allows anything on the anti-diagonal. Windows anchored at `(0,0)`, `(0,2)`, and `(1,1)`
have `a` at both required corners; `(1,0)` has `b` there and fails. So 3 matches.

### Example 2

```
Input:
  T = [['1','0','1'],
       ['0','1','0']]
  P = [['?','0'],
       ['0','?']]

Output: [(0, 0)]
```

**Explanation:** The pattern needs `0` at positions `(0,1)` and `(1,0)` of the window
and allows anything on the main diagonal. Anchored at `(0,0)` the window is
`1 0 / 0 1`: cell `(0,1)=0` and `(1,0)=0` both satisfy the required `0`s, so it matches.
Anchored at `(0,1)` the window is `0 1 / 1 0`: the required `0` cells see `1`, so it
fails. Only `(0, 0)` matches.

### Example 3

```
Input:
  T = [['x','y'],
       ['y','x']]
  P = [['?','?'],
       ['?','?']]

Output: [(0, 0)]
```

**Explanation:** An all-wildcard pattern matches everywhere it fits. The only anchor is
`(0, 0)`, so the single match is `(0, 0)`.

## Hint

Convolution / FFT on 2D data. Encode wildcards as a `0` mask and expand
`sum mask * (T - P)^2 = sum mask*T^2 - 2*sum (mask*P)*T + sum mask*P^2`. Each term is a
2D cross-correlation of two grids; compute them with 2D FFTs, and a window matches iff
the total is `0`.
