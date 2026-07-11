# Solution — K Closest Points to Origin

## Brute Force

Compute every squared distance, sort points by it, and take the first `k`.

```python
def k_closest(points, k):
    return sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)[:k]
```

- **Time:** O(n log n) for the sort.
- **Space:** O(n).

A max-heap of size `k` improves this to O(n log k). But neither is linear, and
we don't actually need the closest points *sorted* — only the set of them.

## Optimal Approach — Median of Medians

We only need to find the **k-th smallest squared distance** (the threshold
`d_k`) and then return every point whose squared distance is at or below it.
Selecting that k-th value is a rank query, and Median of Medians solves it in
worst-case O(n).

### Step by step

1. **Key by squared distance.** For each point compute `d = x*x + y*y`. Use
   squared distance so everything stays integer and monotone — no `sqrt`, no
   floating-point comparison error.
2. **Select the threshold.** Run deterministic selection (Median of Medians) on
   the list of squared distances to obtain the k-th smallest value `d_k`.
3. **Collect the answer.** Return every point with `d < d_k`, then top up with
   points where `d == d_k` until you have exactly `k` points. This tie-aware
   collection handles duplicate distances and guarantees exactly `k` outputs.

### Reference implementation

```python
def k_closest(points, k):
    def select(arr, k):                      # k is 1-indexed
        if len(arr) <= 5:
            return sorted(arr)[k - 1]
        medians = []
        for i in range(0, len(arr), 5):
            g = sorted(arr[i:i + 5])
            medians.append(g[len(g) // 2])
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

    dist = [p[0] ** 2 + p[1] ** 2 for p in points]
    d_k = select(dist, k)                    # k-th smallest squared distance

    result, ties = [], []
    for p, d in zip(points, dist):
        if d < d_k:
            result.append(p)
        elif d == d_k:
            ties.append(p)
    result.extend(ties[:k - len(result)])    # fill remaining slots from ties
    return result
```

### Why it is correct

- Squared distance is a strictly increasing function of true distance for
  non-negative inputs, so ranking by `x^2 + y^2` matches ranking by
  `sqrt(x^2 + y^2)`.
- `select` returns the true k-th smallest squared distance `d_k` (the Median of
  Medians selection is exact). Every point strictly below `d_k` must be in the
  answer; the remaining slots are filled by points exactly at `d_k`. Because the
  problem accepts any valid ordering and any tie-break among equal-distance
  points, this produces a correct set of `k` closest points.

### Why it is linear

`select` runs in worst-case O(n) (median-of-medians recurrence
`T(n) <= T(n/5) + T(7n/10) + O(n) = O(n)`). Computing distances and the final
collection pass are each O(n).

- **Time:** O(n) worst case.
- **Space:** O(n) for the distance array and buckets.

## Key Insights & Edge Cases

- **Use squared distance, never `sqrt`.** It keeps integers exact and dodges
  floating-point tie bugs.
- **Ties matter.** When several points share the k-th distance, only some are
  kept. Split into strict-below and equal buckets and fill exactly `k` — do not
  return all points `<= d_k`, or you may return more than `k`.
- **`k == len(points)`** returns every point (the threshold is the maximum).
- **`k == 1`** just returns the single nearest point (Example 1 -> `[[-2, 2]]`).
- **Order is unconstrained**, so no sorting of the final `k` is required — this
  is precisely why selection (not sorting) is the right tool.
- **Practical note.** LeetCode inputs are small; a heap or sort passes easily.
  Median of Medians is the choice when you must guarantee worst-case linear time.
