# Solution — Reshape the Matrix

## Brute Force

Conceptually the simplest approach is two explicit passes. First, flatten the source
matrix into a 1D list by walking it row by row. Then, chop that list into `r` chunks of
length `c`.

```python
def matrixReshape(self, mat, r, c):
    m, n = len(mat), len(mat[0])
    if m * n != r * c:
        return mat
    flat = []
    for row in mat:                 # row-major flatten
        for val in row:
            flat.append(val)
    return [flat[i * c:(i + 1) * c] for i in range(r)]
```

- **Time:** O(m * n).
- **Space:** O(m * n) for the flattened list plus the output.

## Optimal Approach (Row/Column Traversal)

We can skip the intermediate flat list by mapping a single running counter `k` directly
onto both grids. The `k`-th element in row-major order lives at `(k // n, k % n)` in the
source and belongs at `(k // c, k % c)` in the destination.

```python
def matrixReshape(self, mat, r, c):
    m, n = len(mat), len(mat[0])
    if m * n != r * c:
        return mat
    out = [[0] * c for _ in range(r)]
    k = 0
    for i in range(m):              # outer: source rows
        for j in range(n):          # inner: source columns
            out[k // c][k % c] = mat[i][j]
            k += 1
    return out
```

**Why it is correct:** Both matrices contain the same `m * n = r * c` elements. Reading
the source in row-major order yields the elements in the exact sequence the problem
requires, and writing them with the `(k // c, k % c)` mapping fills the destination in
that same row-major order. The legality check `m * n == r * c` guarantees the counter
`k` ends precisely when `out` is full.

**Step by step** on `mat = [[1,2,3],[4,5,6]], r = 3, c = 2`:

1. `6 == 6`, so reshape is legal; allocate a `3 x 2` grid.
2. `k=0 -> out[0][0]=1`, `k=1 -> out[0][1]=2`, `k=2 -> out[1][0]=3`,
   `k=3 -> out[1][1]=4`, `k=4 -> out[2][0]=5`, `k=5 -> out[2][1]=6`.
3. Return `[[1,2],[3,4],[5,6]]`.

- **Time:** O(m * n) — each element is read once and written once.
- **Space:** O(r * c) for the output (unavoidable, since we must return it); O(1) extra
  beyond that.

## Key Insights & Edge Cases

- **Guard first.** If `m * n != r * c` the reshape is illegal and you must return the
  original matrix unchanged. Forgetting this is the most common bug.
- The integer-division/modulo trick (`k // c`, `k % c`) is the clean way to convert a
  flat position into 2D coordinates; internalize it, as it recurs across matrix
  problems.
- A "reshape" to the same dimensions (`r == m and c == n`) is legal and simply copies
  the matrix.
- Do not mutate `mat` in place when building `out`; allocate a fresh grid so the illegal
  case can still return the original safely.
