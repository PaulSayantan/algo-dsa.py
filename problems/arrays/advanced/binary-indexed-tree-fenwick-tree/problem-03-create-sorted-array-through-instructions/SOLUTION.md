# Create Sorted Array Through Instructions — Solution

## Brute Force

Maintain a sorted list `nums`. For each incoming value `v`, use binary search to find the
count of elements strictly less than `v` and strictly greater than `v`, add
`min(less, greater)` to the total, then insert `v` into the sorted list.

- **Time:** binary search is O(log n), but inserting into a Python list (or shifting an
  array) is O(n), so the whole thing is O(n²) ≈ 10¹⁰ for n = 10⁵ — too slow.
- **Space:** O(n).

## Optimal Approach (Binary Indexed Tree / Fenwick Tree)

Values lie in `[1, 10^5]`, so index a Fenwick Tree directly by value (a frequency BIT: cell
`v` holds how many times value `v` has been inserted so far). Coordinate compression is
optional here but keeps the tree size at O(number of distinct values).

For each value `v`, after having inserted `t` elements total:

- `less = prefix(v - 1)` — how many inserted values are strictly less than `v`.
- `greater = t - prefix(v)` — total inserted minus those `<= v` gives those strictly greater.
- Add `min(less, greater)` to the running total (mod 1e9+7).
- `add(v, 1)` and increment `t`.

**Why it is correct.** The BIT is a running histogram of everything inserted before the
current step. `prefix(v - 1)` counts occurrences of every value `< v`, and
`prefix(v)` counts every value `<= v`; subtracting the latter from the current total `t`
leaves exactly the values `> v`. Because equal values are excluded from both `less`
(uses `v - 1`) and `greater` (subtracts `<= v`, i.e. includes equals in neither), duplicates
contribute `min(less, greater)` correctly — matching the "strictly" wording and why runs of
equal numbers cost `0` until other values surround them.

**Reference implementation:**

```python
class Solution:
    def createSortedArray(self, instructions):
        MOD = 10**9 + 7
        m = max(instructions)                 # values are in [1, m]
        tree = [0] * (m + 1)

        def add(i):
            while i <= m:
                tree[i] += 1
                i += i & (-i)

        def prefix(i):
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & (-i)
            return s

        total = 0
        for t, v in enumerate(instructions):  # t = number inserted so far
            less = prefix(v - 1)
            greater = t - prefix(v)
            total += min(less, greater)
            add(v)
        return total % MOD
```

- **Time:** O(n log m) where `m` is the value range (or O(n log n) with compression).
- **Space:** O(m) for the frequency BIT (O(n) after compression).

## Key Insights & Edge Cases

- **Two counts, one tree.** `less = prefix(v-1)` and `greater = t - prefix(v)`. Track the
  running insert count `t` so you never need a second structure.
- **`prefix(v-1)` and `prefix(v)`, not `prefix(v)` twice.** The gap between them is the count
  of values *equal* to `v`, which must be excluded from both directions — this is what makes
  duplicates cost `0` when nothing else is around.
- **Apply the modulo at the end** (or accumulate mod each step). Costs are small per step,
  but the sum can exceed 32-bit / large ranges; `min` must be taken on the *true* counts,
  never on values already reduced mod 1e9+7.
- **Value-indexed BIT vs compression.** Because `instructions[i] <= 10^5`, a direct
  value-indexed BIT is simplest. If the range were huge or sparse, compress first.
- **`v = 1` edge case:** `prefix(0) = 0`, so `less = 0` for the smallest possible value —
  the `i & (-i)` loop terminates immediately, no special-casing needed.
