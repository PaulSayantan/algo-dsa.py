# Solution — Sort the Matrix Diagonally (LeetCode 1329)

## Brute Force

For every possible diagonal start (each cell in the top row and each cell in the left
column), walk down-right collecting values, sort them, and walk again writing them
back. This is essentially the intended approach; the only "brute" inefficiency is
recomputing diagonal starts by hand and risking boundary bugs.

- **Time:** `O(m * n * log(min(m, n)))` — each diagonal of length `L` costs
  `O(L log L)`; the lengths sum to `m * n`.
- **Space:** `O(min(m, n))` for one diagonal's buffer.

## Optimal Approach (Diagonal / Zig-Zag Traversal via `i - j` buckets)

**Key identity:** cells on the same `\` diagonal share `i - j`. So bucket every value
by that key, sort each bucket, then write the sorted values back in row order.

A clean trick for the write-back: sort each bucket **descending** and store it as a
stack; then a single left-to-right, top-to-bottom pass over the matrix pops the
smallest remaining value for each cell. Because we scan cells in increasing `i` (and
increasing `j`), popping from the end of a descending list hands out ascending values
down each diagonal automatically.

```python
from collections import defaultdict

def diagonalSort(mat):
    m, n = len(mat), len(mat[0])
    buckets = defaultdict(list)
    for i in range(m):
        for j in range(n):
            buckets[i - j].append(mat[i][j])
    for key in buckets:
        buckets[key].sort(reverse=True)      # largest ... smallest
    for i in range(m):
        for j in range(n):
            mat[i][j] = buckets[i - j].pop()  # pop() removes the smallest
    return mat
```

**Why it is correct.** The first double loop drops each value into the bucket of its
diagonal. Sorting a bucket orders that diagonal's values. In the write-back loop we
visit cells of a given diagonal in increasing `i` (top-left to bottom-right); since
the bucket is sorted descending, `pop()` (which removes from the tail) returns the
smallest unused value first, so the diagonal ends up ascending exactly as required.
No value ever leaves its diagonal because both the collection and the write-back use
the same `i - j` key.

**Trace on the main diagonal `i - j = 0` of Example 1** — values `3, 2, 1`:

1. Bucket `0` = `[3, 2, 1]`; sorted descending -> `[3, 2, 1]`.
2. Write-back visits `(0,0)` -> pop `1`; `(1,1)` -> pop `2`; `(2,2)` -> pop `3`.
3. Diagonal becomes `1, 2, 3`. ✔

- **Time:** `O(m * n * log(min(m, n)))` — dominated by sorting; the longest diagonal
  has length `min(m, n)`.
- **Space:** `O(m * n)` for the buckets.

## Key Insights & Edge Cases

- **`i - j` is the diagonal key**, ranging over `-(n-1) .. (m-1)`. Using a dict keyed
  by `i - j` sidesteps enumerating diagonal start cells and their lengths.
- **Descending-sort + `pop()`** is a tidy way to emit ascending order in a forward
  scan; alternatively sort ascending and pop from the front with an index or a
  `deque.popleft()`.
- **Length-1 diagonals** (single cell, or corners) are already sorted; the code
  handles them with no branch.
- **In-place mutation:** the approach overwrites `mat`. If the caller needs the
  original preserved, copy first.
- **Non-square matrices** work unchanged — the `i - j` key is independent of whether
  `m == n`.
