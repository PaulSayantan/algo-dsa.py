# Solution — Weighted Median

## Brute Force

Sort the (value, weight) pairs by value, then scan while accumulating weight.
Return the first value whose running total reaches `W / 2`.

```python
def weighted_median(nums, weights):
    order = sorted(range(len(nums)), key=lambda i: nums[i])
    W = sum(weights)
    acc = 0.0
    for i in order:
        acc += weights[i]
        if 2 * acc >= W:          # cumulative weight has reached W/2
            return nums[i]
```

- **Time:** O(n log n) for the sort.
- **Space:** O(n).

Correct and simple, but the sort makes it superlinear. We can do the same
"find the crossing point" idea without ever sorting.

## Optimal Approach — Median of Medians

The weighted median is the value where the cumulative weight first crosses
`W / 2`. Instead of sorting, we repeatedly partition around the
**median-of-medians pivot**, measure how much weight lies on each side, and
recurse into the side that must contain the crossing point — carrying the weight
already accounted for on the low side downward.

### State we track

`below` = total weight of all values (in the *original* array) strictly less
than the current subproblem. We start with `below = 0` and update it as we
discard low buckets.

### Step by step

1. **Base case.** If the subarray has one element, it is the answer.
2. **Pick pivot.** Use Median of Medians to select the median *value* of the
   current subarray. (Values are distinct, so it is a single element.)
3. **Partition** into `lows` (values `< pivot`) and `highs` (values `> pivot`),
   keeping each element's weight attached. Let `wl = sum of weights in lows` and
   `wp = weight of pivot`.
4. **Compute global side weights.**
   - `below_total = below + wl` (weight strictly below the pivot in the whole
     array),
   - `above_total = W - below_total - wp`.
5. **Decide.**
   - If `below_total < W/2` **and** `above_total <= W/2`: the pivot *is* the
     weighted median — return it.
   - Else if `below_total >= W/2`: the crossing point is among `lows`; recurse
     into `lows` with the same `below`.
   - Else (`above_total > W/2`): recurse into `highs`, updating
     `below := below_total + wp` (we now sit above pivot and all lows).

### Reference implementation

```python
def weighted_median(nums, weights):
    W = sum(weights)
    pairs = list(zip(nums, weights))

    def select_value(arr, k):                 # k-th smallest VALUE, 1-indexed
        vals = [v for v, _ in arr]
        if len(vals) <= 5:
            return sorted(vals)[k - 1]
        med = [sorted(vals[i:i + 5])[len(vals[i:i + 5]) // 2]
               for i in range(0, len(vals), 5)]
        pivot = _select_plain(med, (len(med) + 1) // 2)
        lows  = [x for x in vals if x < pivot]
        eq    = [x for x in vals if x == pivot]
        highs = [x for x in vals if x > pivot]
        if k <= len(lows):
            return select_value([(x, 0) for x in lows], k)
        elif k <= len(lows) + len(eq):
            return pivot
        else:
            return select_value([(x, 0) for x in highs],
                                k - len(lows) - len(eq))

    def solve(arr, below):
        if len(arr) == 1:
            return arr[0][0]
        pivot = select_value(arr, (len(arr) + 1) // 2)   # median value
        lows  = [(v, w) for v, w in arr if v < pivot]
        pv    = [(v, w) for v, w in arr if v == pivot]   # exactly one (distinct)
        highs = [(v, w) for v, w in arr if v > pivot]
        wl = sum(w for _, w in lows)
        wp = sum(w for _, w in pv)
        below_total = below + wl
        above_total = W - below_total - wp
        if below_total < W / 2 and above_total <= W / 2:
            return pivot
        elif below_total >= W / 2:
            return solve(lows, below)
        else:
            return solve(highs, below_total + wp)

    return solve(pairs, 0.0)
```

(`_select_plain` is the ordinary integer median-of-medians `select` from the
earlier problems; shown separately only to keep the value-vs-pair typing clear.)

### Why it is correct

- The definition "first value where cumulative weight `>= W/2`" is equivalent to
  the two-sided condition `below_total < W/2` and `above_total <= W/2`. The
  algorithm returns exactly the value satisfying it.
- Because values are distinct, the pivot bucket holds exactly one element, so
  the `below`/`above` bookkeeping is unambiguous. When we discard the low side we
  fold its total weight into `below`, preserving the global crossing condition
  inside the smaller subproblem.
- Equal-weight inputs reduce to the ordinary lower median (Example 1 -> 3).

### Why it is linear

Each level does an O(n) median-of-medians selection plus an O(n) partition, and
the median pivot guarantees each recursion shrinks the array by a constant
fraction (at most ~7n/10 remains). The total is the familiar
`T(n) <= T(n/5) + T(7n/10) + O(n) = O(n)`.

- **Time:** O(n) worst case.
- **Space:** O(n) for the buckets (reducible with in-place partitioning).

## Key Insights & Edge Cases

- **Carry the discarded weight.** The single most common bug is forgetting to
  fold the low side's weight into `below` when recursing right; then the
  `W/2` comparison is made against the wrong baseline.
- **Two-sided crossing condition.** Using `below < W/2 AND above <= W/2` (rather
  than only "cumulative `>= W/2`") makes the boundary well defined and matches
  the "lower" weighted median convention.
- **Equal weights** collapse to the plain lower median — a good sanity check.
- **Heavy single weight** (Example 3: weight 0.8 on value 3) can pull the median
  onto that value even though it is the largest; the algorithm handles this
  because the *above* weight is then `<= W/2`.
- **Distinct values assumption.** If values could repeat, aggregate equal values
  and sum their weights first so the pivot bucket stays a single logical point.
- **Post-office interpretation.** The weighted median minimizes
  `sum_i w_i * |x - v_i|`; this is why it appears in facility-location and
  robust-estimation problems.
