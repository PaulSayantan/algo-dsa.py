# Non-overlapping Intervals — Solution

Removing the fewest intervals to eliminate all overlaps is the same as **keeping the
most** intervals that are mutually non-overlapping. The answer is then
`n - (max intervals kept)`. Keeping the maximum number of compatible intervals is the
textbook **activity-selection** problem.

## Brute Force

Try every subset of intervals, check whether it is overlap-free, and track the largest
valid subset. The answer is `n` minus that size.

- **Time:** `O(2^n * n)` — exponentially many subsets, each checked in `O(n)`.
- **Space:** `O(n)` for the recursion / subset bookkeeping.

Infeasible for `n` up to `10^5`.

## Optimal Approach (Meeting Rooms / Interval Scheduling — greedy activity selection)

**Sort by end time.** Greedily keep the interval that finishes earliest, because
finishing earlier leaves the most room for future intervals. Walk through the sorted
list tracking the end of the last interval we kept.

Steps:

1. Sort `intervals` by `end`.
2. Set `kept_end = -inf` and `removals = 0`.
3. For each `[s, e]`:
   - If `s >= kept_end`, this interval does not overlap the last kept one — keep it and
     set `kept_end = e`.
   - Otherwise it overlaps a kept interval — remove it: `removals += 1`.
4. Return `removals`.

```python
def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda iv: iv[1])
    kept_end = float("-inf")
    removals = 0
    for s, e in intervals:
        if s >= kept_end:      # compatible -> keep
            kept_end = e
        else:                   # overlaps a kept interval -> drop
            removals += 1
    return removals
```

- **Time:** `O(n log n)` for the sort, `O(n)` for the sweep.
- **Space:** `O(1)` extra beyond the sort.

### Why the greedy is correct

Classic exchange argument. Among all intervals, the one with the smallest end time can
always be part of some optimal "keep" set: given any optimal solution, its
first-finishing interval can be swapped for the globally first-finishing interval
without creating any new conflict (the replacement ends no later, so it conflicts with
no more of the remaining intervals). Repeating this argument on the intervals that
start at or after that end time shows the greedy choice — always keep the compatible
interval that ends earliest — yields a maximum-size compatible set. Every interval the
greedy cannot keep must be removed, giving the minimum removal count.

## Key Insights & Edge Cases

- **Sort by END, not start.** Sorting by end is what makes "earliest finish" the right
  greedy. (Sorting by start and greedily dropping the interval with the *larger* end on
  each conflict is an equivalent alternative, but sort-by-end is the cleanest form.)
- **Touching is allowed:** use `s >= kept_end` so `[1, 2]` and `[2, 3]` both survive.
- **Identical intervals:** `[[1,2],[1,2],[1,2]]` → keep one, remove two → `2`.
- **Empty / single interval:** `0` removals.
- Equivalent framing: `removals = n - (number kept)`; both formulations produce the
  same number.
