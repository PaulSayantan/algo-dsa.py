# Transpose Matrix — Solution

## Brute Force

There isn't really a "slow" way to transpose — you must touch every cell at
least once. The most direct approach is to allocate a fresh `n x m` result and
copy each element into its mirrored position.

```python
def transpose(matrix):
    m, n = len(matrix), len(matrix[0])
    result = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            result[j][i] = matrix[i][j]
    return result
```

- **Time:** `O(m * n)` — one pass over every element.
- **Space:** `O(m * n)` for the new matrix (unavoidable for a rectangular
  input, since the shape changes).

## Optimal Approach (Transpose)

The approach above is already optimal in asymptotic terms. Because the input
may be rectangular (`m != n`), an in-place swap is not possible: the output has
a different shape than the input. So we build a new matrix with swapped
dimensions.

Two equivalent, idiomatic ways to write it in Python:

```python
# Explicit index mapping: result[j][i] = matrix[i][j]
def transpose(matrix):
    n_rows, n_cols = len(matrix), len(matrix[0])
    return [[matrix[i][j] for i in range(n_rows)] for j in range(n_cols)]

# Or the one-liner using zip, which pairs up the i-th element of every row.
def transpose(matrix):
    return [list(col) for col in zip(*matrix)]
```

**Why it is correct:** By definition the transpose entry at `(i, j)` is the
original entry at `(j, i)`. The comprehension iterates `j` over the original
columns (the new rows) and `i` over the original rows (the new columns),
placing `matrix[i][j]` exactly at output position `(j, i)`. `zip(*matrix)`
groups the elements that share a column index into tuples, which is precisely
the set of rows of the transpose.

**Step by step** on `[[1,2,3],[4,5,6]]`:

1. Original is `2x3`, so the result is `3x2`.
2. New row 0 = original column 0 = `[1, 4]`.
3. New row 1 = original column 1 = `[2, 5]`.
4. New row 2 = original column 2 = `[3, 6]`.
5. Result: `[[1,4],[2,5],[3,6]]`.

- **Time:** `O(m * n)`.
- **Space:** `O(m * n)` for the output (`O(1)` auxiliary beyond the output).

## Key Insights & Edge Cases

- **Rectangular vs. square:** In-place transpose only works for square
  matrices. Here the input can be rectangular, so allocate a new matrix.
- **Single row / single column:** `[[1,2,3]]` (1x3) transposes to
  `[[1],[2],[3]]` (3x1). The `zip` form handles this cleanly.
- **Single element:** `[[7]]` returns `[[7]]`.
- **`zip(*matrix)` returns tuples**, so wrap each in `list(...)` if the caller
  expects lists.
- **Don't alias rows:** build fresh inner lists; reusing references could cause
  aliasing bugs if the result is later mutated.
