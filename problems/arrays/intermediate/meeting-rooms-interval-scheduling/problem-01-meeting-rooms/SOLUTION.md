# Meeting Rooms — Solution

## Brute Force

Compare every pair of meetings. For each pair `(i, j)` check whether they overlap,
which happens when `start_i < end_j` **and** `start_j < end_i`. If any pair overlaps,
return `False`; otherwise return `True`.

- **Time:** `O(n^2)` — every pair is examined.
- **Space:** `O(1)`.

This works but is wasteful: overlap is a *local* property once the meetings are lined
up in time.

## Optimal Approach (Meeting Rooms / Interval Scheduling)

Sort the meetings by their **start** time. Once sorted, the only way a meeting can
collide with an earlier one is by colliding with its **immediate predecessor** — if
meeting `i` starts before meeting `i-1` ends, they overlap. If it does *not* overlap
the predecessor, it cannot overlap anything before that either, because all earlier
meetings start no later and we only need the earliest-ending neighbour to clear.

Steps:

1. Sort `intervals` by `start`.
2. Iterate from the second meeting onward. Keep `prev_end` = end of the previous
   meeting.
3. If the current meeting's `start < prev_end`, the meetings overlap → return `False`.
4. Otherwise update `prev_end = max(prev_end, current end)` (a plain assignment to the
   current end also works after sorting by start) and continue.
5. If the loop finishes, return `True`.

Use a **strict** `<` comparison so that touching endpoints (`[1, 5]`, `[5, 8]`) are
treated as compatible.

```python
def canAttendMeetings(intervals):
    intervals.sort(key=lambda iv: iv[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True
```

- **Time:** `O(n log n)` for the sort, then `O(n)` for the single pass.
- **Space:** `O(1)` extra (ignoring the sort's implementation cost / `O(n)` if the
  sort is not in place).

### Why it is correct

After sorting by start time the starts are non-decreasing. Suppose meeting `i` does
not overlap meeting `i-1`, i.e. `start_i >= end_{i-1}`. Because `start_{i-1} <=
start_i` for all earlier meetings and each earlier meeting `k < i-1` satisfies
`end_k <= end_{i-1}` only when they were themselves non-overlapping — the invariant we
maintain is that once a prefix is overlap-free, the largest end seen so far is
`end_{i-1}`. Comparing against the immediate predecessor is therefore sufficient. The
first violating pair, if any, is detected the moment we reach it.

## Key Insights & Edge Cases

- **Empty or single meeting:** `intervals = []` or a single interval trivially returns
  `True`; the loop never runs.
- **Touching endpoints are OK:** use `<`, not `<=`. `[[1, 5], [5, 8]]` → `True`.
- **Duplicate meetings:** two identical intervals `[[1, 4], [1, 4]]` overlap → `False`.
- **Sorting key:** sort by start time. If you accidentally sort by end time you can
  still detect *some* overlaps but the "compare to predecessor" shortcut no longer
  holds cleanly, so start-time sorting is the clean choice here.
