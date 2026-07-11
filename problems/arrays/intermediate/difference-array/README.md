# Difference Array

A **difference array** is a companion array `diff` of an array `arr` where each
entry stores the *difference between consecutive elements*:

```
diff[0]   = arr[0]
diff[i]   = arr[i] - arr[i - 1]   (for i > 0)
```

The magic is the inverse relationship: taking the **prefix sum** of `diff`
reconstructs the original array. This means a *range update* — "add `v` to every
element in `arr[l..r]`" — can be done in **O(1)** by touching just two cells:

```
diff[l]     += v      # everything from l onward shifts up by v
diff[r + 1] -= v      # cancel the shift right after r
```

After all updates are recorded, one prefix-sum pass **materializes** the final
array in O(n). So `q` range updates cost `O(q + n)` instead of the naive
`O(q * n)`.

## When to reach for it

- You must apply **many range updates** and only care about the final array
  (updates are "offline" / batched, not interleaved with queries).
- Each update adds a constant to a contiguous range (or a contiguous
  sub-rectangle, using the 2D generalization).
- Think: "increment interval", "book seats over a range of flights",
  "passengers board at x and leave at y", "stamp a rectangle".

If you need to *query* ranges in between updates, prefer a Fenwick/segment tree.
The difference array shines when all updates come first, materialize once.

## Complexity

| | Time | Space |
|---|---|---|
| Single range update | O(1) | — |
| `q` updates + build | O(n + q) | O(n) |
| 2D: `q` rect updates + build | O(m·n + q) | O(m·n) |

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Maximum Population Year](problem-01-maximum-population-year/PROBLEM.md) | Mark birth/death deltas over years, prefix-sum to find the peak year. | Easy |
| 2 | [Range Addition](problem-02-range-addition/PROBLEM.md) | The canonical drill: apply many `[l, r, inc]` updates and return the array. | Medium |
| 3 | [Corporate Flight Bookings](problem-03-corporate-flight-bookings/PROBLEM.md) | Sum seat reservations over inclusive flight ranges. | Medium |
| 4 | [Car Pooling](problem-04-car-pooling/PROBLEM.md) | Board/drop passengers along a line; check capacity is never exceeded. | Medium |
| 5 | [Increment Submatrices by One](problem-05-increment-submatrices-by-one/PROBLEM.md) | 2D difference array: add 1 to many sub-rectangles, then materialize. | Medium |
| 6 | [Stamping the Grid](problem-06-stamping-the-grid/PROBLEM.md) | Combine 2D prefix sums (feasibility) with a 2D difference array (coverage). | Hard |
