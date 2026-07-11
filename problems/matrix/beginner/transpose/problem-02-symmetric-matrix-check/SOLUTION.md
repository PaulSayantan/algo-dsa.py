# Symmetric Matrix Check — Solution

## Brute Force

Materialize the full transpose into a new matrix, then compare it element by
element against the original.

```python
def isSymmetric(matrix):
    n = len(matrix)
    transposed = [[matrix[j][i] for j in range(n)] for i in range(n)]
    return transposed == matrix
```

- **Time:** `O(n^2)` — build the transpose and compare.
- **Space:** `O(n^2)` for the explicit transpose copy.

## Optimal Approach (Transpose)

We do not actually need to build the transpose. By definition, the matrix
equals its transpose iff `M[i][j] == M[j][i]` for every pair. We only need to
check each off-diagonal pair **once**, so iterate over the strict upper
triangle (`j > i`). Diagonal entries (`i == j`) are compared with themselves and
are always equal, so they can be skipped.

```python
def isSymmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):   # upper triangle only
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
```

**Why it is correct:** Symmetry is precisely the statement "M equals its
transpose." Comparing `M[i][j]` with `M[j][i]` for all `i < j` covers every
mirrored pair; the `i == j` case is trivially satisfied. If any pair disagrees,
the matrix cannot equal its transpose, so we return `False` immediately.

**Step by step** on `[[1,2,3],[2,4,5],[3,5,6]]`:

1. `(0,1)`: `M[0][1]=2` vs `M[1][0]=2` — equal.
2. `(0,2)`: `M[0][2]=3` vs `M[2][0]=3` — equal.
3. `(1,2)`: `M[1][2]=5` vs `M[2][1]=5` — equal.
4. No mismatch found — return `True`.

- **Time:** `O(n^2)` worst case, but early-exits on the first mismatch.
- **Space:** `O(1)` — no extra matrix is built.

## Key Insights & Edge Cases

- **Only the upper triangle matters.** Iterating `j` from `i + 1` avoids
  redundant comparisons and skips the always-equal diagonal.
- **Symmetry requires squareness.** If the problem allowed rectangular input,
  a non-square matrix could never be symmetric — check dimensions first.
- **1x1 matrix** is always symmetric (no off-diagonal pairs to violate).
- **Early termination** makes the average case much faster than always building
  the whole transpose.
- Symmetry is unrelated to the values on the diagonal — those are free to be
  anything.
