# Range Count of Elements Not Exceeding K — Solution

## Brute Force

Store the array. `update` overwrites a cell in `O(1)`. `query(left, right, k)`
scans the range and counts values `<= k` in `O(n)`.

```python
def query(self, left, right, k):
    return sum(1 for i in range(left, right + 1) if self.nums[i] <= k)
```

With `5 * 10^4` queries over `5 * 10^4` elements this is `O(q * n) = 2.5 * 10^9`
in the worst case — too slow. The difficulty is that "count `<= k`" is an
**order statistic**: a plain running count cannot be maintained incrementally
across arbitrary ranges the way a sum can.

## Optimal Approach (Sqrt Decomposition with Sorted Blocks)

Split the array into blocks of size `b ≈ sqrt(n)`. In addition to the raw array,
each block `k` keeps `sorted_block[k]`, a **sorted copy** of that block's
current values.

**Build** — copy each block's elements and sort them: `O(n log b)` overall
(`≈ O(n log n)`).

**query(left, right, k)** — the usual three-part split:

1. **Partial left block:** scan the in-range elements directly, incrementing the
   count when `nums[i] <= k`.
2. **Whole interior blocks:** for each fully contained block `k`, the count of
   values `<= k` equals the number of sorted elements not exceeding `k`, found
   with one binary search: `bisect_right(sorted_block[k], k)`.
3. **Partial right block:** scan directly like the left.

```python
from bisect import bisect_right, bisect_left, insort

def query(self, left, right, k):
    b = self.b
    lb, rb = left // b, right // b
    count = 0
    if lb == rb:
        return sum(1 for i in range(left, right + 1) if self.nums[i] <= k)
    for i in range(left, (lb + 1) * b):            # partial left block
        if self.nums[i] <= k:
            count += 1
    for blk in range(lb + 1, rb):                  # whole interior blocks
        count += bisect_right(self.sorted_block[blk], k)
    for i in range(rb * b, right + 1):             # partial right block
        if self.nums[i] <= k:
            count += 1
    return count
```

**update(index, val)** — the value at `index` changes, so the sorted copy of its
block must be repaired: delete the old value and insert the new one.

```python
def update(self, index, val):
    k = index // self.b
    old = self.nums[index]
    if old == val:
        return
    arr = self.sorted_block[k]
    arr.pop(bisect_left(arr, old))   # remove one copy of the old value
    insort(arr, val)                 # insert the new value in order
    self.nums[index] = val
```

Both the delete and the insert are `O(b)` because shifting inside a
`b`-length list dominates the `O(log b)` search.

**Why it is correct.** For a fully contained block, every element is inside the
query range, so the count of block values `<= k` is exactly
`bisect_right(sorted_block[k], k)` — the position where `k` would be inserted to
keep the list sorted, i.e. the number of entries `<= k`. Boundary blocks are only
partially inside the range, so they are counted element-by-element to avoid
including out-of-range indices. Every in-range index is thus counted once.
`update` keeps `sorted_block[k]` a faithful sorted multiset of block `k`
(remove old, add new), so the binary searches always reflect the current data.

**Complexity.** A query does `< 2b` scalar comparisons on the boundaries plus
`< n / b` binary searches of `O(log b)` each: `O(b + (n / b) log b)`. With
`b ≈ sqrt(n)` this is `O(sqrt(n) log n)`. Each `update` is `O(b) = O(sqrt(n))`.
Space is `O(n)` for the sorted copies. Total: `O(n log n + q * sqrt(n) log n)`.

## Key Insights & Edge Cases

- **`bisect_right(list, k)` counts values `<= k`** (it returns the insertion
  point to the right of equal keys). Use `bisect_left` if you instead want
  strictly-less-than.
- **The sorted block is a multiset.** Remove exactly one copy of the old value
  with `pop(bisect_left(arr, old))`; do not remove all equal values.
- **Duplicates and negatives** are handled naturally by binary search on the
  sorted copy.
- **Single-block ranges** (`lb == rb`) must scan directly, since there are no
  fully contained interior blocks.
- **No-op updates** (`old == val`) can return early to skip list surgery.
- This "sorted blocks" trick generalizes to range-`k`-th-smallest and
  range-count-in-`[lo, hi]`. A merge sort tree or a wavelet tree answers static
  versions faster, but sqrt decomposition is the simplest structure that also
  supports **point updates**.
