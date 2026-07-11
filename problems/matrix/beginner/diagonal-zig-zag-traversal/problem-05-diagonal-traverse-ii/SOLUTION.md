# Solution — Diagonal Traverse II (LeetCode 1424)

## Brute Force

Find the maximum possible diagonal id (`max(i + j)`), then for each `d` from `0`
upward scan the entire jagged array collecting cells with `i + j == d` in the right
order.

- **Time:** `O(D * N)` where `D` is the number of diagonals and `N` the total number
  of elements — repeated full scans.
- **Space:** `O(N)` for the output.

Because rows are ragged, `D` can be as large as `O(N)`, so this can degrade toward
`O(N^2)`. We can do a single pass instead.

## Optimal Approach (Diagonal / Zig-Zag Traversal on a jagged array)

**Key identity holds even when ragged:** a cell `(i, j)` still belongs to
anti-diagonal `i + j`, regardless of how long each row is. So bucket cells by `i + j`
in one pass, then emit buckets in increasing key order.

**Required within-diagonal order is bottom-to-top** (largest `i` first). If we append
cells while iterating rows top-to-bottom, each bucket ends up top-to-bottom; simply
reverse it on output. (Equivalently, iterate rows bottom-to-top, or prepend.)

```python
from collections import defaultdict

def findDiagonalOrder(nums):
    buckets = defaultdict(list)
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            buckets[i + j].append(nums[i][j])   # appended top-to-bottom
    res = []
    for key in sorted(buckets):                 # increasing i + j
        res.extend(reversed(buckets[key]))      # -> bottom-to-top
    return res
```

**Why it is correct.** During the scan, for a fixed diagonal key `d = i + j`, cells
are appended in increasing `i` (rows processed top-to-bottom), so `buckets[d]` is in
top-to-bottom order. Reversing yields bottom-to-top, the order the figure requires.
Emitting keys in ascending order visits diagonals from the top-left corner outward.
Ragged rows never break the invariant because membership depends only on `i + j`.

**Avoiding the sort.** Diagonal keys are `0, 1, 2, ...` contiguously up to
`max(i + j)`, so you can index buckets by an array/list instead of a dict and skip
the `sorted(...)`, giving strict `O(N)`:

```python
def findDiagonalOrder(nums):
    max_key = max(i + len(row) - 1 for i, row in enumerate(nums))
    buckets = [[] for _ in range(max_key + 1)]
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            buckets[i + j].append(nums[i][j])
    res = []
    for b in buckets:
        res.extend(reversed(b))
    return res
```

**Trace on Example 1** (`[[1,2,3],[4,5,6],[7,8,9]]`):

| `d` | bucket (top-to-bottom) | reversed (emitted) |
|-----|------------------------|--------------------|
| 0   | [1]                    | 1                  |
| 1   | [2, 4]                 | 4, 2               |
| 2   | [3, 5, 7]              | 7, 5, 3            |
| 3   | [6, 8]                 | 8, 6               |
| 4   | [9]                    | 9                  |

Result: `[1, 4, 2, 7, 5, 3, 8, 6, 9]`. ✔

- **Time:** `O(N)` with the array-indexed buckets (`O(N + D log D)` with the dict +
  sort), where `N` is the total element count.
- **Space:** `O(N)` for buckets and output.

## Key Insights & Edge Cases

- **Ragged is fine:** the `i + j` grouping never assumed a rectangle. Only iterate
  `j` up to `len(nums[i])`, which varies per row.
- **Direction differs from LeetCode 498:** here *every* diagonal is read
  bottom-to-top (no alternation), unlike the zig-zag of Problem 2. Do not add the
  parity flip.
- **Do not build an `m x n` grid** — a short row followed by a long row would make a
  dense matrix huge; bucketing by key uses only `O(N)`.
- **Contiguous keys** enable the sort-free variant; the largest key is
  `max(i + len(nums[i]) - 1)`.
- **Single row / single column / single element** all fall out correctly: each bucket
  has the trivial order and reversing a length-1 (or length-`n` single-diagonal) list
  behaves as expected.
