# Non-overlapping Intervals — Solution

## Brute Force

The complement of "remove the fewest" is "keep the most non-overlapping intervals."
Brute force enumerates every subset of intervals, checks each for pairwise
disjointness, and keeps the largest disjoint subset; the answer is `n - (that size)`.

- **Time:** `O(2^n * n)` — exponential subsets, each validated in linear time.
- **Space:** `O(n)`.

You could also write an interval DP in `O(n^2)`, but the greedy is both faster and
simpler.

## Optimal Approach (Greedy — interval scheduling)

**Idea:** To keep the maximum number of mutually non-overlapping intervals, repeatedly
keep the interval that **ends earliest**, because finishing early leaves the most room
for later intervals. Sort by end coordinate, then sweep: track the end of the last
interval you kept; if the next interval starts at or after that end, keep it and update
the boundary; otherwise it overlaps, so count it as a removal.

```python
def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda iv: iv[1])   # sort by END, ascending
    removals = 0
    prev_end = float("-inf")
    for start, end in intervals:
        if start >= prev_end:      # non-overlapping (touching is OK)
            prev_end = end         # keep it
        else:
            removals += 1          # overlaps → must remove
    return removals
```

**Why it is correct (exchange argument):** This is the classic *activity selection*
result. Among all intervals, the one with the smallest end must belong to some optimal
"keep" set: if an optimal solution kept a different first interval, swap it for the
earliest-ending one — it ends no later, so it cannot conflict with anything the optimal
set kept afterward, and the set size is unchanged. Induct on the remaining intervals.
Thus greedily locking in the earliest finisher at each step is optimal, and every
skipped (overlapping) interval is a necessary removal.

- **Time:** `O(n log n)` — dominated by the sort; the scan is `O(n)`.
- **Space:** `O(1)` extra (besides the sort).

## Key Insights & Edge Cases

- **Sort by END, not start.** Sorting by start can force you to keep a long interval
  that ends late and blocks many others. The earliest-end rule is what makes greedy
  optimal here.
- **Touching endpoints don't overlap:** use `start >= prev_end` (not strict `>`).
  If the problem instead treated `[1,2]` and `[2,3]` as overlapping, you'd use `>`.
- **Identical intervals** (`[[1,2],[1,2],[1,2]]`): only the first is kept; the other
  two overlap → 2 removals.
- **Already disjoint / single interval:** 0 removals.
- The same "sort by end" engine solves *Maximum Number of Non-overlapping intervals*,
  *Minimum Arrows to Burst Balloons* (LeetCode 452), and meeting-room scheduling.
