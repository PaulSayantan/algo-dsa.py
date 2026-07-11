# Employee Free Time — Solution

## Brute Force

Discretize time: for every unit (or every distinct boundary) mark whether *any*
employee is busy, then scan the timeline for maximal runs where nobody is busy
and emit those runs (dropping the leading/trailing unbounded ones).

- **Time:** `O(T)` where `T` is the timeline length — up to `10^8` here, so this
  is infeasible. Even a boundary-compressed version costs `O(n * m)` to fill.
- **Space:** `O(T)` or `O(number of boundaries)`.

The employee grouping is irrelevant to the answer, and enumerating time is
wasteful. Flattening plus Merge Intervals is far cleaner.

## Optimal Approach (flatten, then Merge Intervals)

The individual employees do not matter — only the **union** of all busy time
does. Free time common to everyone is exactly the time not covered by that union.

1. **Flatten:** collect every `Interval` from every employee into one list.
2. **Sort** the flattened list by `start`.
3. **Merge** overlapping/touching intervals into disjoint busy blocks (the
   standard Merge Intervals sweep).
4. **Take the gaps:** for each pair of consecutive merged blocks
   `[.., prev_end]` and `[cur_start, ..]`, if `prev_end < cur_start` then
   `[prev_end, cur_start]` is a common free interval. Emit it.

```python
def employeeFreeTime(schedule):
    intervals = [iv for emp in schedule for iv in emp]
    intervals.sort(key=lambda iv: iv.start)

    free = []
    prev_end = intervals[0].end
    for iv in intervals[1:]:
        if iv.start > prev_end:            # a real gap: everyone is free here
            free.append(Interval(prev_end, iv.start))
            prev_end = iv.end
        else:                               # overlap/touch: extend busy block
            prev_end = max(prev_end, iv.end)
    return free
```

**Why it is correct:** a moment `t` is common free time iff no employee's interval
contains `t`, i.e. `t` is not in the union of all busy intervals. After sorting
and merging, the union is a set of disjoint blocks; the finite complement of that
union (ignoring `(-inf, first_start)` and `(last_end, +inf)`) is precisely the set
of gaps between consecutive blocks. The `max(prev_end, iv.end)` guard is the
Merge Intervals extension that prevents a fully-contained interval (e.g. a short
shift inside a longer merged block) from spuriously ending the block early.

- **Time:** `O(N log N)` where `N` is the total number of intervals across all
  employees (flatten is `O(N)`, sort dominates, sweep is `O(N)`).
- **Space:** `O(N)` for the flattened list and output.

### Heap variant

Because each employee's list is already sorted, you can k-way merge with a
min-heap of size `k = len(schedule)` to produce the flattened stream in sorted
order in `O(N log k)`. This is the theoretically tighter version, but the
flatten-and-sort approach is simpler and plenty fast for the constraints.

## Key Insights & Edge Cases

- **Gaps require a strict `<`:** only emit `[prev_end, cur_start]` when
  `prev_end < cur_start`. When `prev_end == cur_start` the blocks touch, leaving a
  zero-length gap that must be skipped (no free time).
- **Only extend `prev_end` inside overlaps** with `max(prev_end, iv.end)` — a
  later interval may be entirely inside the current block, in which case
  `prev_end` must not shrink.
- **Do not emit the unbounded free time** before the first busy block or after the
  last; the loop naturally handles this by starting `prev_end` at the first
  interval's end and never looking past the last.
- **Single employee / single interval** yields no internal gaps → return `[]`.
- **Sort by start is required**; a common bug is forgetting to sort after
  flattening, since employee lists are individually sorted but not jointly.
