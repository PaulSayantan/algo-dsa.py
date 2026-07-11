# Solution — The K Weakest Rows in a Matrix

## Brute Force

Build a `(soldier_count, index)` key for each row, sort all keys, and take the first `k` indices:

```python
def kWeakestRows(self, mat, k):
    keys = sorted((sum(row), i) for i, row in enumerate(mat))
    return [i for _, i in keys[:k]]
```

- **Time:** `O(m·n)` to count soldiers + `O(m log m)` to sort the keys.
- **Space:** `O(m)` for the key list.

Tuple comparison `(count, index)` gives the required "fewer soldiers, then smaller index" ordering
for free. This is the clean idiomatic solution; below we swap the library sort for a partial
Selection Sort since we only need the `k` smallest keys.

## Optimal Approach (Partial Selection Sort on a composite key)

1. Reduce each row to a `(soldier_count, row_index)` pair. Because every row has its `1`s before its
   `0`s, `soldier_count = sum(row)` (or a binary search for the first `0`, which is `O(log n)` per
   row).
2. **Selection-Sort** the list of pairs for just `k` passes, each pass selecting the pair that is
   smallest under the natural tuple order `(count, index)`.
3. Emit the `row_index` component of the first `k` selected pairs.

```python
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        pairs = [(sum(row), i) for i, row in enumerate(mat)]
        m = len(pairs)
        for i in range(k):                     # only k passes
            min_idx = i
            for j in range(i + 1, m):
                if pairs[j] < pairs[min_idx]:  # tuple compare: count, then index
                    min_idx = j
            if min_idx != i:
                pairs[i], pairs[min_idx] = pairs[min_idx], pairs[i]
        return [pairs[i][1] for i in range(k)]
```

### Why it is correct

The comparison key is the tuple `(count, index)`. Python compares tuples lexicographically, so
`(c1, i1) < (c2, i2)` is true exactly when `c1 < c2`, or `c1 == c2 and i1 < i2` — which is precisely
the problem's definition of "weaker." Selection Sort's invariant then guarantees that after `k`
passes, `pairs[0 .. k-1]` are the `k` smallest keys in ascending order, i.e. the `k` weakest rows
from weakest to strongest. Projecting out the index component yields the answer.

### Step-by-step on Example 1 (`k = 3`)

Keys: `row0=(2,0), row1=(4,1), row2=(1,2), row3=(2,3)` → `pairs = [(2,0),(4,1),(1,2),(2,3)]`.

| pass i | min key in suffix | swap indices | pairs                              |
|--------|-------------------|--------------|------------------------------------|
| 0      | `(1,2)` @2        | swap 0,2     | `[(1,2),(4,1),(2,0),(2,3)]`        |
| 1      | `(2,0)` @2        | swap 1,2     | `[(1,2),(2,0),(4,1),(2,3)]`        |
| 2      | `(2,3)` @3        | swap 2,3     | `[(1,2),(2,0),(2,3),(4,1)]`        |

Take indices of the first 3 pairs: `[2, 0, 3]`. ✔

### Complexity

- **Time:** `O(m·n)` to compute the counts (or `O(m log n)` with binary search) + `O(m·k)` for the
  `k` selection passes. Overall `O(m·n + m·k)`.
- **Space:** `O(m)` for the pair list; the selection itself is in place over that list.

## Key Insights & Edge Cases

- **Composite key = built-in tiebreak:** encoding the tiebreaker directly into the sort key
  `(count, index)` means a single tuple comparison enforces both rules. No custom stability handling
  is needed — the index is part of the key, so equal-count rows are already ordered by index.
- **Partial sort:** as in the k-th-largest problem, only `k` passes are required; do not sort all
  `m` rows. This keeps the work at `O(m·k)` for the sorting phase.
- **Sorted rows ⇒ fast count:** the guarantee that `1`s precede `0`s lets you count soldiers with a
  binary search for the first `0` (`O(log n)`), though `sum(row)` (`O(n)`) is simpler and fine for
  `n <= 100`.
- **All rows equal strength:** ties resolve purely by index, so the answer is `[0, 1, ..., k-1]`.
- **k == m:** every row is returned, fully ordered by `(count, index)`; the loop runs `m` passes.
- **Return indices, not counts:** the output must be the original **row indices**, which is why the
  index is carried inside each pair throughout the sort.
