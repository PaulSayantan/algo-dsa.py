# Sparse Matrix Transpose — Solution

## Brute Force

Two easy but wasteful ideas:

1. **Densify.** Expand the triplets into a full `num_rows x num_cols` grid,
   transpose the grid, then re-extract the non-zeros. This defeats the purpose
   of the sparse representation and costs `O(num_rows * num_cols)` time and
   space even when there are only a handful of non-zero entries.

2. **Swap then sort.** Map each triplet `[r, c, v] -> [c, r, v]`, then run a
   general comparison sort on the swapped list to restore row-major order.

```python
def transpose_sparse(num_rows, num_cols, triplets):
    swapped = [[c, r, v] for r, c, v in triplets]
    swapped.sort(key=lambda t: (t[0], t[1]))
    return swapped
```

- Densify — **Time:** `O(num_rows * num_cols)`, **Space:** `O(num_rows * num_cols)`.
- Swap + sort — **Time:** `O(k log k)` where `k = len(triplets)`,
  **Space:** `O(k)`.

The swap-and-sort version is perfectly acceptable and is the cleanest correct
answer. The optimal version below removes the `log k` factor.

## Optimal Approach (Transpose via Counting Sort)

The core transpose step is trivial: a non-zero at `(r, c)` moves to `(c, r)`
with the same value. The only real work is emitting the results already sorted
in **row-major order of the transpose** — that is, ordered by the original
**column** index, and within a column by the original row index.

Because the input is already in row-major order (rows ascending, columns
ascending within a row), the entries that share a given original column already
appear in ascending original-row order. So a single **counting sort by column**
produces the correct final order without any comparisons.

```python
def transpose_sparse(num_rows, num_cols, triplets):
    k = len(triplets)
    if k == 0:
        return []

    # count[c] = number of non-zeros in original column c
    count = [0] * num_cols
    for _, c, _ in triplets:
        count[c] += 1

    # start[c] = index in the output where column c's block begins
    start = [0] * num_cols
    running = 0
    for c in range(num_cols):
        start[c] = running
        running += count[c]

    result = [None] * k
    for r, c, v in triplets:      # input is in row-major (ascending r) order
        pos = start[c]
        result[pos] = [c, r, v]   # transpose: (r, c) -> (c, r)
        start[c] += 1
    return result
```

**Why it is correct.** After transposing, an output row equals an original
column. `count[c]` tells us how many entries land in output row `c`, and the
prefix sums in `start` reserve a contiguous block for each output row in
ascending order. Since we scan the input in ascending-row order and the input's
per-column entries are already row-sorted, each entry is dropped into the next
free slot of its column's block, so within every output row the columns (the
original rows) come out ascending. The result is fully row-major.

**Step by step** on `num_rows=3, num_cols=4,
triplets=[[0,2,5],[1,0,3],[2,1,2],[2,3,1]]`:

1. Column counts: col0=1, col1=1, col2=1, col3=1 -> `count=[1,1,1,1]`.
2. Prefix starts: `start=[0,1,2,3]`.
3. Place `[0,2,5]` -> output row 2, slot 2 -> `[2,0,5]`.
4. Place `[1,0,3]` -> output row 0, slot 0 -> `[0,1,3]`.
5. Place `[2,1,2]` -> output row 1, slot 1 -> `[1,2,2]`.
6. Place `[2,3,1]` -> output row 3, slot 3 -> `[3,2,1]`.
7. Result: `[[0,1,3],[1,2,2],[2,0,5],[3,2,1]]`.

- **Time:** `O(num_cols + k)` — one pass to count, one pass to place.
- **Space:** `O(num_cols + k)` for the counting arrays and the output.

## Key Insights & Edge Cases

- **The transpose itself is just index swapping**: `(r, c, v) -> (c, r, v)`. All
  the effort is in producing sorted output cheaply.
- **Counting sort beats comparison sort** here (`O(num_cols + k)` vs.
  `O(k log k)`) because column indices are small bounded integers.
- **Empty matrix** (`triplets == []`) returns `[]` — handle it before building
  count arrays (or the code naturally returns an empty list).
- **Shape flips**: the transpose has `num_cols` rows and `num_rows` columns; a
  valid output row index ranges over `0 .. num_cols - 1`.
- **Relies on sorted input.** If the input triplets were not in row-major order,
  the counting-sort pass would still group by column correctly but the order
  *within* each output row would not be guaranteed — you would need to sort the
  input first (or fall back to swap-and-sort).
- **No zero values** are stored, so the output never contains a triplet with
  `value == 0`.
