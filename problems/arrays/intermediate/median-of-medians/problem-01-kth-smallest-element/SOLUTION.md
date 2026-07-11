# Solution — Kth Smallest Element in an Array

## Brute Force

Sort the array and index directly.

```python
def kth_smallest(nums, k):
    return sorted(nums)[k - 1]
```

- **Time:** O(n log n) for the sort.
- **Space:** O(n) (or O(log n)/O(n) depending on the sort implementation).

A heap of size `k` gives O(n log k), and randomized Quickselect gives *expected*
O(n) but **worst-case O(n^2)** if an adversary (or already-sorted data) forces
bad pivots. None of these give a deterministic worst-case linear bound, which is
the goal here.

## Optimal Approach — Median of Medians

We want a pivot that is guaranteed to be "central enough" so that partitioning
always discards a constant fraction of the elements. Median of Medians produces
exactly such a pivot in linear time.

### Step by step

1. **Base case.** If the array has `<= 5` elements, just sort it and return the
   element of the requested rank.
2. **Group and take medians.** Split the array into groups of 5. Sort each group
   (constant work per group) and collect the median of each group into a list
   `medians` of size `⌈n/5⌉`.
3. **Recurse for the pivot.** Recursively run selection on `medians` to find the
   *median of the medians*, `M`. This is the pivot.
4. **Three-way partition** around `M` into `lows` (`< M`), `equals` (`== M`), and
   `highs` (`> M`). Three-way partitioning handles duplicates cleanly.
5. **Recurse into one side** based on where rank `k` falls:
   - if `k <= len(lows)`: answer is in `lows`, recurse with the same `k`;
   - else if `k <= len(lows) + len(equals)`: the answer is `M` itself;
   - else: recurse into `highs` with `k - len(lows) - len(equals)`.

### Reference implementation

```python
def kth_smallest(nums, k):
    def select(arr, k):  # k is 1-indexed within arr
        if len(arr) <= 5:
            return sorted(arr)[k - 1]

        # medians of groups of 5
        medians = []
        for i in range(0, len(arr), 5):
            group = sorted(arr[i:i + 5])
            medians.append(group[len(group) // 2])

        # pivot = median of medians (recursive)
        pivot = select(medians, (len(medians) + 1) // 2)

        lows   = [x for x in arr if x < pivot]
        equals = [x for x in arr if x == pivot]
        highs  = [x for x in arr if x > pivot]

        if k <= len(lows):
            return select(lows, k)
        elif k <= len(lows) + len(equals):
            return pivot
        else:
            return select(highs, k - len(lows) - len(equals))

    return select(nums, k)
```

### Why it is correct

- The three-way partition preserves the rank invariant: every element in `lows`
  is strictly smaller than every element in `equals`, which is strictly smaller
  than every element in `highs`. So the rank-`k` element of `arr` is exactly the
  rank-`k` element of whichever bucket the counting logic selects.
- The recursion for the pivot terminates because `medians` has size `⌈n/5⌉ < n`
  for `n > 5`.

### Why it is linear

`M` is the median of the `⌈n/5⌉` group medians. At least half of those group
medians are `<= M`, and each such group contributes 3 elements (the median and
two smaller) that are `<= M`. That gives at least roughly `3 * (n/10) = 3n/10`
elements `<= M`; symmetrically at least `~3n/10` are `>= M`. Hence each recursive
call into `lows`/`highs` handles at most about `7n/10` elements. With the
`n/5`-sized pivot recursion, the recurrence is

```
T(n) <= T(n/5) + T(7n/10) + O(n),   and   1/5 + 7/10 = 9/10 < 1,
```

which solves to **T(n) = O(n)**.

- **Time:** O(n) worst case.
- **Space:** O(n) for the copy-based buckets (can be reduced to O(log n) extra
  with an in-place partition and tail-recursion elimination).

## Key Insights & Edge Cases

- **Group size 5 is not arbitrary.** It is the smallest odd group size making
  the two recursion fractions sum to `< 1`. Groups of 3 give `1/3 + 2/3 = 1`,
  which is *not* linear. Groups of 7 also work but with larger constants.
- **Duplicates.** A two-way partition can loop forever or misplace equal
  elements; the three-way (`lows`/`equals`/`highs`) split is the clean fix and
  makes Example 3 (`[2, 2, 3]`, k=2 -> 2) correct.
- **1-indexed vs 0-indexed.** `k = 1` is the minimum. If you store rank
  0-indexed internally, translate carefully to avoid off-by-one bugs.
- **k out of range** (`k < 1` or `k > n`) is invalid per constraints; guard if
  your environment does not guarantee it.
- **Practical note.** For typical inputs, randomized Quickselect beats Median of
  Medians on constant factors; reach for Median of Medians when you must *prove*
  a worst-case linear bound.
