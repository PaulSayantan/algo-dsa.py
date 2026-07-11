# Doolittle LU Decomposition

**Difficulty:** Easy

**Source:** Classic numerical-methods exercise (CLRS §28.1, "LUP Decomposition")

## Description

Given a square `n × n` matrix `A`, factor it into a **lower** triangular matrix
`L` and an **upper** triangular matrix `U` such that:

```
A = L · U
```

Use the **Doolittle** convention, in which every diagonal entry of `L` is exactly
`1`. Under this convention the factorization is unique whenever it exists.

Concretely, you must produce:

- `L`: an `n × n` matrix that is `0` above the diagonal and `1` on the diagonal.
- `U`: an `n × n` matrix that is `0` below the diagonal.

You may assume the matrix admits a factorization **without row swaps** — i.e.
every pivot encountered during elimination is non-zero (no pivoting required for
this problem). Return `L` and `U` as a tuple `(L, U)`.

The factorization is exactly Gaussian elimination: `U` is what `A` reduces to,
and each below-diagonal entry `L[i][k]` is the multiplier `A[i][k] / U[k][k]`
used to eliminate column `k` from row `i`.

## Constraints

- `1 <= n <= 100`
- `A` is a square matrix of real numbers given as a list of `n` lists of `n` floats.
- Every leading principal minor of `A` is non-zero (so no pivoting is needed and
  every pivot `U[k][k]` is non-zero).
- Entries fit in double-precision floating point; comparisons may allow a small
  tolerance such as `1e-9`.

## Examples

### Example 1

```
Input:  A = [[4, 3],
             [6, 3]]

Output: L = [[1.0, 0.0],
             [1.5, 1.0]]
        U = [[4.0, 3.0],
             [0.0, -1.5]]
```

**Explanation:** The multiplier to eliminate the `6` under the pivot `4` is
`6 / 4 = 1.5`, so `L[1][0] = 1.5`. Subtracting `1.5 ×` row 0 from row 1 turns the
`3` into `3 - 1.5·3 = -1.5`. Multiplying `L · U` reproduces `A` exactly.

### Example 2

```
Input:  A = [[ 2, -1, -2],
             [-4,  6,  3],
             [-4, -2,  8]]

Output: L = [[ 1.0,  0.0, 0.0],
             [-2.0,  1.0, 0.0],
             [-2.0, -1.0, 1.0]]
        U = [[ 2.0, -1.0, -2.0],
             [ 0.0,  4.0, -1.0],
             [ 0.0,  0.0,  3.0]]
```

**Explanation:** Column 0 multipliers are `-4/2 = -2` and `-4/2 = -2`. After
eliminating column 0 the matrix becomes `[[2,-1,-2],[0,4,-1],[0,-4,4]]`; the
column-1 multiplier is `-4/4 = -1`, giving `L[2][1] = -1` and turning the last
row into `[0, 0, 3]`. You can confirm `L · U = A`.

## Hint

Run Gaussian elimination but *remember* the multiplier you use for each row
instead of throwing it away — that is exactly **LU Decomposition**.
