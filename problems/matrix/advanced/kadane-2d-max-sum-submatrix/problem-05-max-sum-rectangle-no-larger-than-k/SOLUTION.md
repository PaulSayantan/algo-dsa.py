# Solution — Max Sum of Rectangle No Larger Than K

## Brute Force

Enumerate all `(top, bottom, left, right)` rectangles with a 2D prefix-sum
table, and among those whose sum is `<= k`, keep the maximum.

- **Time:** `O(m² · n²)`.
- **Space:** `O(m · n)`.

Too slow when both dimensions approach 100 and, more importantly, it does not
exploit the `<= k` structure.

## Optimal Approach — Kadane 2D + sorted prefix sums

Plain Kadane finds the *largest* subarray sum, but here we need the largest sum
that is still `<= k`. Kadane cannot enforce an upper bound, so we swap the 1D
subroutine for a **sorted prefix-sum search**.

For a compressed row `col`, a subarray sum equals `pre[j] - pre[i]` for some
`i < j`. We want the largest such value `<= k`, i.e. for each running prefix
`pre` we want the smallest earlier prefix `p` with `p >= pre - k` (that
minimizes `pre - p` from above while keeping it `<= k`). Maintaining earlier
prefixes in a sorted structure lets binary search find that `p` in `O(log m)`.

**Step by step:**

1. For each `top` row, reset `colSum = [0] * n`.
2. For each `bottom >= top`, add row `bottom` into `colSum` (incremental
   compression).
3. Search `colSum` for the max subarray sum `<= k`:
   - Keep a sorted list `prefixes` seeded with `0`.
   - Sweep, maintaining running `pre`. For each `pre`, binary-search the
     smallest stored prefix `>= pre - k`; if found, `pre - that_prefix` is a
     candidate `<= k`. Update the global best.
   - Insert `pre` into the sorted list.
4. Return the global best across all row bands.

```python
import bisect

def maxSumSubmatrix(matrix, k):
    m, n = len(matrix), len(matrix[0])
    best = float("-inf")
    for top in range(m):
        col = [0] * n
        for bottom in range(top, m):
            for c in range(n):
                col[c] += matrix[bottom][c]      # compress the row band
            # --- max subarray sum <= k on col ---
            prefixes = [0]
            pre = 0
            for x in col:
                pre += x
                idx = bisect.bisect_left(prefixes, pre - k)
                if idx < len(prefixes):
                    best = max(best, pre - prefixes[idx])
                bisect.insort(prefixes, pre)
    return best
```

**Why it is correct.** For a fixed row band, any candidate rectangle's sum is a
contiguous slice sum `pre_j - pre_i` with `i < j`. To make it `<= k` and as
large as possible, we need the smallest `pre_i` with `pre_i >= pre_j - k`;
`bisect_left(prefixes, pre - k)` returns exactly the position of that smallest
qualifying prefix among all prefixes seen *before* `j` (we insert `pre` only
after querying, preserving `i < j`). Trying this for every `j` covers every
column band for that row pair, and iterating all row pairs covers every
rectangle. Hence the reported maximum is the global best rectangle with sum
`<= k`.

- **Time:** `O(m² · n · log n)` — `O(m²)` row bands, each doing an `O(n)`
  compress plus an `O(n log n)` sorted-prefix sweep.
- **Space:** `O(n)` for `colSum` and the sorted prefix list.

**Optimization:** Orient the matrix so the *outer* squared loop runs over the
smaller dimension and the `log` factor sits on the larger one, giving
`O(min² · max · log max)`.

## Key Insights & Edge Cases

- **Why not plain Kadane:** Kadane maximizes without a ceiling. If the
  unconstrained best exceeds `k` (Examples 2 and 3), Kadane would overshoot; the
  sorted-prefix search is what enforces the `<= k` cap.
- **Seed `prefixes` with `0`:** This represents the empty prefix so column bands
  starting at index `0` are considered; querying `pre - k` against it handles
  the "prefix itself is a valid window" case.
- **Query before insert:** Insert the current `pre` only *after* the binary
  search, otherwise a zero-length (empty) window could be selected, which is
  invalid.
- **Exact hit `== k`:** When some window sums to exactly `k`, `bisect_left`
  lands on `pre - k` itself and yields `k` — the best possible; you can early-
  exit the whole algorithm if `best == k`.
- **Simpler `bisect.insort` vs. balanced BST:** `insort` into a Python list is
  `O(n)` per insertion in the worst case, making the inner sweep `O(n²)`; for
  the given constraints (`n <= 100`) this is fine, but a true `O(n log n)` sweep
  needs an order-statistics/balanced tree (e.g. `sortedcontainers.SortedList`).
- **All configurations `> k` impossible:** The problem guarantees at least one
  rectangle with sum `<= k`, so `best` is always updated at least once.
