# Transpose Matrix — Solution

## Brute Force

There is really only one natural approach, but the most literal version is to
allocate a result of the correct shape and copy element by element.

- Read `m` and `n` from the input.
- Create `result` as an `n × m` grid of zeros.
- For each `(i, j)`, set `result[j][i] = matrix[i][j]`.

**Time:** `O(m · n)` — every element is copied once.
**Space:** `O(m · n)` for the output (unavoidable when the matrix is not square).

## Optimal Approach (Transpose half of Rotate 90°)

Transpose *is* the operation, so the "optimal" version is the same nested loop
written cleanly. This is exactly the first pass of the Rotate 90° recipe.

```python
def transpose(matrix):
    m, n = len(matrix), len(matrix[0])
    result = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            result[j][i] = matrix[i][j]
    return result
```

**Why it is correct:** By definition the transpose satisfies
`result[j][i] == matrix[i][j]`. The double loop assigns exactly that for every
cell, and since `(i, j) → (j, i)` is a bijection between an `m × n` grid and an
`n × m` grid, every output cell is written exactly once.

**Step by step** on `[[1,2,3],[4,5,6]]` (`m = 2`, `n = 3`):

1. `(0,0)=1 → result[0][0]`
2. `(0,1)=2 → result[1][0]`
3. `(0,2)=3 → result[2][0]`
4. `(1,0)=4 → result[0][1]`, `(1,1)=5 → result[1][1]`, `(1,2)=6 → result[2][1]`

Result: `[[1,4],[2,5],[3,6]]`.

**Time:** `O(m · n)`. **Space:** `O(m · n)` for the returned matrix
(`O(1)` auxiliary beyond the output).

### Note on in-place transpose

If — and only if — the matrix is **square** (`m == n`), you can transpose in
place by swapping the upper triangle with the lower triangle:

```python
for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

Starting `j` at `i + 1` is essential: it skips the diagonal and prevents
swapping every pair twice (which would undo the transpose).

## Key Insights & Edge Cases

- **Non-square input:** the output shape is `n × m`, not `m × n`. You must
  allocate a fresh matrix; you cannot swap in place.
- **Single row / single column:** `[[1,2,3]]` transposes to `[[1],[2],[3]]`.
- **Do not iterate the upper triangle only** unless the matrix is square — that
  optimization is exclusive to the in-place square case.
- Transpose composed with a row reversal is a full 90° rotation; mastering this
  pass makes the harder problems in this folder straightforward.
