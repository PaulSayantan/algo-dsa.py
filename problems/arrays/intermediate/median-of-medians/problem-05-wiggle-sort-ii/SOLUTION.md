# Solution — Wiggle Sort II

## Brute Force

Sort, split into a smaller half and a larger half, and interleave from the
**ends inward** so that duplicates near the median get pushed apart.

```python
def wiggle_sort(nums):
    s = sorted(nums)
    n = len(nums)
    mid = (n + 1) // 2            # size of the smaller half
    small = s[:mid][::-1]         # smaller half, largest-first
    large = s[mid:][::-1]         # larger half, largest-first
    nums[0::2] = small            # even indices get the smaller half
    nums[1::2] = large            # odd indices get the larger half
```

- **Time:** O(n log n) for the sort.
- **Space:** O(n).

Reversing each half before interleaving is what keeps equal values around the
median from becoming adjacent (e.g. `[1,1,1,1,2,2]`). But the sort is
superlinear.

## Optimal Approach — Median of Medians + Virtual Indexing

Two ideas combine:

1. **Find the median in O(n)** with Median of Medians instead of sorting.
2. **Three-way partition on virtual indices** so that, in a single pass, all
   values greater than the median land on the "peak" (odd) slots, all values
   less than the median land on the "valley" (even) slots, and the medians fill
   the boundary — never adjacent.

### The virtual index map

Map a logical position `i` to a real array index:

```
idx(i) = (1 + 2*i) % (n | 1)
```

As `i` runs `0, 1, 2, ...`, `idx(i)` visits the **odd** indices first
(`1, 3, 5, ...`) and then wraps to the **even** indices (`0, 2, 4, ...`).
`n | 1` is `n` rounded up to the next odd number, which makes the mapping a
bijection over `[0, n)`. So writing "larger values to the front of the virtual
order, smaller values to the back" automatically places larger values on peaks
and smaller values on valleys.

### Step by step

1. **Median.** `m = select(nums, (n + 1) // 2)` via Median of Medians (the
   lower-median rank works for both parities).
2. **Dutch-national-flag partition over `idx`.** Maintain `i` (next slot for a
   `> m` value), `j` (scanner), `k` (next slot for a `< m` value). Compare
   `nums[idx(j)]` to `m`:
   - `> m`: swap into `idx(i)`, advance `i` and `j`;
   - `< m`: swap into `idx(k)`, retreat `k`;
   - `== m`: advance `j` only.
3. Done — `nums` is a valid wiggle, in place, in linear time.

### Reference implementation

```python
def wiggle_sort(nums):
    n = len(nums)

    def select(arr, k):                       # k-th smallest, 1-indexed
        if len(arr) <= 5:
            return sorted(arr)[k - 1]
        med = [sorted(arr[i:i + 5])[len(arr[i:i + 5]) // 2]
               for i in range(0, len(arr), 5)]
        pivot = select(med, (len(med) + 1) // 2)
        lows   = [x for x in arr if x < pivot]
        equals = [x for x in arr if x == pivot]
        highs  = [x for x in arr if x > pivot]
        if k <= len(lows):
            return select(lows, k)
        elif k <= len(lows) + len(equals):
            return pivot
        return select(highs, k - len(lows) - len(equals))

    m = select(nums[:], (n + 1) // 2)         # median (copy: select rearranges)

    def idx(i):
        return (1 + 2 * i) % (n | 1)

    i = j = 0
    k = n - 1
    while j <= k:
        v = nums[idx(j)]
        if v > m:
            nums[idx(i)], nums[idx(j)] = nums[idx(j)], nums[idx(i)]
            i += 1
            j += 1
        elif v < m:
            nums[idx(j)], nums[idx(k)] = nums[idx(k)], nums[idx(j)]
            k -= 1
        else:
            j += 1
```

### Why it is correct

- **Median split.** With `n` elements and `mid = (n+1)//2`, at most `mid` copies
  of any value can exist for a solution to be possible (the problem guarantees
  one exists). The larger half fills the `⌊n/2⌋` peak slots and the smaller half
  fills the `⌈n/2⌉` valley slots.
- **Non-adjacency of equal medians.** The virtual mapping fills odd (peak) slots
  first, then even (valley) slots, from opposite ends of the `> m` / `< m`
  buckets. Any copies equal to the median are pushed toward the center of the
  virtual order, so two equal medians are never mapped to adjacent real indices.
  This is exactly what makes tricky cases like `[1,1,1,1,2,2]` succeed.
- Verified by brute force: over thousands of randomly generated *solvable*
  arrays, the output is always a permutation of the input and satisfies the
  strict wiggle inequalities.

### Why it is linear

`select` is worst-case O(n) (Median of Medians recurrence
`T(n) <= T(n/5) + T(7n/10) + O(n) = O(n)`), and the three-way partition is a
single O(n) pass.

- **Time:** O(n) worst case.
- **Space:** O(n) for the copy passed to `select` (the partition itself is
  O(1) extra). A fully in-place `select` reduces this toward the O(1)-space
  follow-up.

## Key Insights & Edge Cases

- **Why virtual indexing beats naive interleaving.** Splitting into halves and
  interleaving left-to-right can place two medians next to each other. The
  `(1 + 2*i) % (n | 1)` mapping guarantees separation without extra buffers.
- **Parity `n | 1`.** For even `n`, `n | 1 = n + 1`; for odd `n`, `n | 1 = n`.
  Using plain `n` breaks the bijection and corrupts the permutation.
- **Median rank.** Use the lower-median rank `(n + 1) // 2`; pairing it with the
  "larger to peaks, smaller to valleys" convention keeps the two halves sized
  correctly for both parities.
- **`select` mutates / needs its own copy.** Pass a copy to the selection routine
  so the subsequent in-place partition works on the original ordering.
- **No valid answer.** If some value appears more than `(n+1)//2` times, no
  wiggle exists; the problem guarantees this does not happen, but a robust
  implementation may want to detect it.
- **Tiny arrays.** `n = 1` is already valid; `n = 2` needs `nums[0] < nums[1]`,
  which the partition produces.
