# Count of Smaller Numbers After Self — Solution

## Brute Force

For every `i`, scan all `j > i` and count how many satisfy `nums[j] < nums[i]`.

- **Time:** O(n²) — up to ~10¹⁰ operations for n = 10⁵, far too slow.
- **Space:** O(1) beyond the output.

## Optimal Approach (Binary Indexed Tree / Fenwick Tree)

The key reframing: "elements to the right that are smaller than `nums[i]`" equals "among
the elements we have already inserted while scanning **right to left**, how many are
strictly less than `nums[i]`." A Fenwick Tree indexed by value answers "how many inserted
values are `< x`?" as a **prefix count**.

**Coordinate compression.** Values range over [-10⁴, 10⁴], which is small, but in general
(and to keep the tree tight) map the distinct values to ranks `1..k` via sorting. If `x`
has rank `r` (1-based), then the number of strictly smaller values already inserted is
`prefix(r - 1)`.

**Algorithm.**

1. Compress: `sorted_unique = sorted(set(nums))`; `rank[x] = bisect_left(sorted_unique, x) + 1`
   so ranks are 1-based (Fenwick Trees require 1-based indices).
2. Create a BIT of size `k` (number of distinct values), all zeros.
3. Iterate `i` from `n - 1` down to `0`:
   - `r = rank[nums[i]]`
   - `counts[i] = prefix(r - 1)` — count of already-inserted values with a smaller rank.
   - `add(r, 1)` — mark that `nums[i]` is now present.
4. Return `counts`.

**Why it is correct.** When we process index `i`, the BIT contains exactly the elements at
indices `i+1 .. n-1` (everything to the right, inserted in previous iterations). Because
ranks preserve the strict order of values, `prefix(r - 1)` counts precisely those
right-side elements whose value is strictly less than `nums[i]`. Using `r - 1` (not `r`)
excludes equal values, matching the "strictly smaller" requirement — this is why
`[-1, -1]` gives `[0, 0]`.

**Reference implementation:**

```python
from bisect import bisect_left

class Solution:
    def countSmaller(self, nums):
        sorted_unique = sorted(set(nums))
        k = len(sorted_unique)
        tree = [0] * (k + 1)

        def add(i, delta):
            while i <= k:
                tree[i] += delta
                i += i & (-i)

        def prefix(i):
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & (-i)
            return s

        counts = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            r = bisect_left(sorted_unique, nums[i]) + 1   # 1-based rank
            counts[i] = prefix(r - 1)                     # strictly smaller
            add(r, 1)
        return counts
```

- **Time:** O(n log n) — one BIT query and one BIT update per element, plus the O(n log n)
  compression sort.
- **Space:** O(n) for the BIT and the compression arrays.

## Key Insights & Edge Cases

- **Direction matters.** Sweeping right to left is what makes "already inserted" mean "to
  the right." A left-to-right sweep would instead count smaller elements to the *left*.
- **`prefix(r - 1)` vs `prefix(r)`.** Query the rank *below* the current value to keep the
  count **strictly** smaller; querying `prefix(r)` would wrongly include equal values.
- **1-based ranks.** Compression must produce ranks starting at 1, or the `i & (-i)` walk
  stalls at index 0.
- **Duplicates** collapse to the same rank — handled naturally by `set` + `bisect_left`.
- **Negatives** are irrelevant after compression; the BIT only ever sees ranks.
- This same right-to-left "count smaller/greater seen so far" pattern generalizes to
  "count of greater elements" (`prefix(k) - prefix(r)`) and to inversion counting.
