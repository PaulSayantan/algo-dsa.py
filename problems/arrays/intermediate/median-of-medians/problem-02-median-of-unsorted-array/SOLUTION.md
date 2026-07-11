# Solution — Median of an Unsorted Array

## Brute Force

Sort and read off the middle element.

```python
def find_median(nums):
    s = sorted(nums)
    return s[(len(nums) - 1) // 2]
```

- **Time:** O(n log n).
- **Space:** O(n) (or O(log n) depending on the sort).

Correct, but it does far more work than needed: we only want one element, not a
total order. And it is superlinear.

## Optimal Approach — Median of Medians

The median is simply the order statistic of rank `⌈n/2⌉` (1-indexed), which for
the lower median equals `(n - 1) // 2 + 1`. So this reduces to a single
**selection** query, and Median of Medians solves selection in worst-case O(n).

### Reduction to selection

```python
def find_median(nums):
    n = len(nums)
    k = (n - 1) // 2 + 1          # 1-indexed rank of the lower median
    return select(nums, k)
```

### The `select` routine (Median of Medians)

```python
def select(arr, k):               # k is 1-indexed
    if len(arr) <= 5:
        return sorted(arr)[k - 1]

    medians = []
    for i in range(0, len(arr), 5):
        group = sorted(arr[i:i + 5])
        medians.append(group[len(group) // 2])

    pivot = select(medians, (len(medians) + 1) // 2)   # median of medians

    lows   = [x for x in arr if x < pivot]
    equals = [x for x in arr if x == pivot]
    highs  = [x for x in arr if x > pivot]

    if k <= len(lows):
        return select(lows, k)
    elif k <= len(lows) + len(equals):
        return pivot
    else:
        return select(highs, k - len(lows) - len(equals))
```

### Why it is correct

- Choosing rank `k = (n - 1) // 2 + 1` reproduces the definition of the lower
  median for both parities:
  - `n = 3` -> `k = 2` -> 2nd smallest = middle element.
  - `n = 6` -> `k = 3` -> 3rd smallest = the *smaller* of the two middle values,
    matching Example 2 (`7`, not `10`).
- The three-way partition inside `select` keeps the rank invariant intact
  (everything in `lows` `<` `equals` `<` everything in `highs`), so recursing
  into the correct bucket returns the true rank-`k` value.

### Why it is linear

The median-of-medians pivot is `>=` at least `~3n/10` elements and `<=` at least
`~3n/10` elements, so each recursive step drops at least ~30% of the array:

```
T(n) <= T(n/5) + T(7n/10) + O(n)  =>  T(n) = O(n).
```

- **Time:** O(n) worst case.
- **Space:** O(n) with copy-based buckets (reducible to O(log n) extra with an
  in-place partition).

## Key Insights & Edge Cases

- **Lower vs upper median.** For even `n` there are two middle elements. This
  problem asks for the *lower* one (`(n - 1) // 2`). The upper median would be
  rank `n // 2 + 1`; make sure the rank formula matches the definition you were
  asked for.
- **Single element / tiny arrays** fall into the base case and are returned
  directly — Example 3 (`[5]`) returns `5`.
- **Duplicates** are handled by the `equals` bucket; a median that repeats many
  times will simply land in `equals`.
- **Why not just Quickselect with a random pivot?** Expected O(n) but worst-case
  O(n^2). Median of Medians is the deterministic guarantee.
- **Streaming caveat.** This assumes the whole array is in memory. Finding a
  running median over a stream is a different problem (two heaps / order
  statistics tree), not Median of Medians.
