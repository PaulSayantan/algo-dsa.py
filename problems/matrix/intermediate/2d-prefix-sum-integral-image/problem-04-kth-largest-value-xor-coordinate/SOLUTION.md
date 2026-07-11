# Solution — Find Kth Largest XOR Coordinate Value

## Brute Force

For each coordinate `(a, b)`, XOR together every `matrix[i][j]` with `i <= a`
and `j <= b`, collect all `m * n` values, sort, and pick the k-th largest.

```python
values = []
for a in range(m):
    for b in range(n):
        v = 0
        for i in range(a + 1):
            for j in range(b + 1):
                v ^= matrix[i][j]
        values.append(v)
values.sort(reverse=True)
return values[k - 1]
```

- **Time:** O((m * n)^2) to recompute every prefix XOR, plus O(m*n log(m*n))
  to sort. For `1000 x 1000` the recomputation is `10^12` — hopeless.
- **Space:** O(m * n) for the value list.

## Optimal Approach — 2D Prefix Sum (Integral Image) with XOR

The coordinate value is literally a 2D prefix, except the associative operation
is **XOR** rather than addition. XOR is its own inverse (`x ^ x = 0`), so it
plays the role of both `+` and `-` in the standard recurrence — the "subtract
the overlap" step becomes "XOR the overlap back out."

### Build recurrence (padded table `P`, size `(m+1) x (n+1)`, all zeros border)

```
P[i][j] = matrix[i-1][j-1] ^ P[i-1][j] ^ P[i][j-1] ^ P[i-1][j-1]
```

`P[i][j]` is exactly `value(i-1, j-1)` — the XOR over the top-left block. The
top-left overlap `P[i-1][j-1]` was included in *both* `P[i-1][j]` and
`P[i][j-1]`, so it appears twice and cancels itself; XOR-ing it a third time
restores the correct single contribution. (Equivalently: it was double-counted,
and one more XOR removes the duplicate.)

### Selecting the k-th largest

Collect all `P[i][j]` for `i, j >= 1` into a list and either:

- sort descending and index `k-1` — O(m*n log(m*n)); or
- use a size-`k` min-heap / `heapq.nlargest` — O(m*n log k); or
- use quickselect — O(m*n) average.

### Step by step

1. Allocate padded `P`.
2. Fill `P` with the XOR recurrence; append each real value to `results`.
3. Return the k-th largest of `results`.

### Why it is correct

Because XOR is associative, commutative, and self-inverse, the same
inclusion-exclusion identity that proves the additive integral image proves the
XOR version — every original cell inside the block is XOR-ed an odd number of
times (exactly once) and every cell outside is XOR-ed an even number of times
(net zero).

### Reference implementation

```python
import heapq

class Solution:
    def kthLargestValue(self, matrix, k):
        m, n = len(matrix), len(matrix[0])
        P = [[0] * (n + 1) for _ in range(m + 1)]
        results = []
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = (matrix[i - 1][j - 1] ^ P[i - 1][j]
                           ^ P[i][j - 1] ^ P[i - 1][j - 1])
                results.append(P[i][j])
        return heapq.nlargest(k, results)[-1]
```

- **Time:** O(m * n) to build + O(m*n log k) to select. **Space:** O(m * n).

## Key Insights & Edge Cases

- The whole point is recognizing that "prefix" does not require addition — **any
  associative, invertible operator** admits an integral-image table. XOR is the
  classic example because it is its own inverse, so the build formula uses XOR
  four times with no minus sign.
- **k-th largest**, not smallest, and it is **1-indexed** — index `k-1` after
  sorting descending, or take the last element of `nlargest(k, ...)`.
- Duplicate coordinate values are counted independently; do **not** deduplicate.
- A `1 x 1` matrix has a single value; `k` must be 1 and the answer is that
  cell. The formula returns it directly.
- Prefer a heap or quickselect over a full sort when `k` is small and the grid
  is large (up to `10^6` values).
