# Non-overlapping Intervals — Solution

## Brute Force

"Minimum removals to make the rest non-overlapping" is equivalent to "maximum number of
intervals you can **keep** that are mutually non-overlapping," and the answer is
`n - (max kept)`. A brute force enumerates subsets of intervals, checks each for pairwise
non-overlap, and keeps the largest valid subset.

- **Time:** `O(2^n * n)` to test every subset. **Space:** `O(n)`.

Exponential and hopeless for `n` up to `10^5`. The trouble is choosing *which* intervals
to keep without a guiding order.

## Optimal Approach (Sorting as Preprocessing)

**Idea:** This is the classic **activity-selection** problem. Sort the intervals by
**end** time. Greedily keep the interval that finishes earliest; then keep the next
interval whose start is `>= ` the last kept interval's end. Every interval you have to
skip because it overlaps is one required removal.

**Why it is correct (greedy exchange):** Among all intervals, the one that finishes
earliest is always safe to keep in some optimal "kept" set: it leaves the maximum amount
of room for the remaining intervals. If an optimal solution kept a different first
interval, we could swap in the earliest-finishing one without reducing the count (it ends
no later, so it conflicts with no more of the rest). Applying this repeatedly yields the
maximum non-overlapping subset. Sorting by end time is exactly what surfaces
"finishes earliest" at every step.

**Step by step:**

1. Sort `intervals` by end value.
2. Track `kept_end = -infinity` and `removed = 0`.
3. For each `[s, e]` in end-sorted order:
   - If `s >= kept_end`, this interval doesn't overlap the last kept one — keep it and set
     `kept_end = e`.
   - Otherwise it overlaps — increment `removed` (drop this one, keep the earlier-ending
     interval already chosen).
4. Return `removed`.

```python
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda iv: iv[1])   # sort by end
    kept_end = float("-inf")
    removed = 0
    for s, e in intervals:
        if s >= kept_end:      # no overlap (touching is allowed)
            kept_end = e       # keep it
        else:
            removed += 1       # overlaps -> must remove this one
    return removed
```

- **Time:** `O(n log n)` for the sort, then `O(n)` for the single greedy pass.
- **Space:** `O(1)` beyond the sort.

## Key Insights & Edge Cases

- **Sort by end, not start.** Keeping the earliest-finishing interval is the greedy
  choice that maximizes how many intervals survive; sorting by start would not directly
  give this and needs extra care.
- **Touching is allowed:** the test is `s >= kept_end` (not `>`), so `[1,2]` followed by
  `[2,3]` are both kept and contribute 0 removals.
- **When overlapping, drop the current interval** (the one that ends later) and keep the
  already-selected earlier-ending one — that's why `kept_end` is *not* updated on a
  removal.
- **Identical intervals** (`[[1,2],[1,2],[1,2]]`): the first is kept, the other two each
  overlap and are removed -> 2.
- **Single interval or already disjoint input** yields 0 removals.
- **Equivalent framing:** `removed = n - maxKept`; the greedy computes `removed` directly
  by counting skips, which is the same thing.
