# Insert Interval — Solution

## Brute Force

Append `newInterval` to the list, then run the full **Merge Intervals** routine
(sort by start, sweep, merge overlaps).

- **Time:** `O(n log n)` because of the re-sort.
- **Space:** `O(n)`.

This is perfectly correct and easy to write, but it throws away the fact that the
input is already sorted and disjoint. We can do better in `O(n)`.

## Optimal Approach (Merge Intervals in one linear pass)

Since `intervals` is already sorted and non-overlapping, `newInterval` interacts
with only a **contiguous block** of them. Walk left to right in three phases:

1. **Before:** while the current interval ends strictly before `newInterval`
   starts (`interval[1] < newInterval[0]`), it cannot overlap — copy it to the
   output as-is.
2. **Merge:** while the current interval starts at or before `newInterval` ends
   (`interval[0] <= newInterval[1]`), it overlaps — absorb it into `newInterval`
   by taking `newInterval = [min(starts), max(ends)]`. After the loop, append the
   grown `newInterval` once.
3. **After:** copy all remaining intervals unchanged.

```python
def insert(intervals, newInterval):
    res = []
    i, n = 0, len(intervals)
    ns, ne = newInterval

    # Phase 1: intervals entirely before the new one.
    while i < n and intervals[i][1] < ns:
        res.append(intervals[i])
        i += 1

    # Phase 2: overlapping intervals fold into [ns, ne].
    while i < n and intervals[i][0] <= ne:
        ns = min(ns, intervals[i][0])
        ne = max(ne, intervals[i][1])
        i += 1
    res.append([ns, ne])

    # Phase 3: intervals entirely after the new one.
    while i < n:
        res.append(intervals[i])
        i += 1

    return res
```

**Why it is correct:** with sorted, disjoint input the intervals that overlap
`newInterval` form one run — everything before that run ends too early to touch it,
and everything after starts too late. Phase 2's `min`/`max` computes the union of
`newInterval` with exactly that run, which is itself a single interval because the
run plus `newInterval` is contiguous. Phases 1 and 3 preserve order and disjointness.

- **Time:** `O(n)` — each interval is examined once, no sorting.
- **Space:** `O(n)` for the output.

## Key Insights & Edge Cases

- **Touching boundaries merge:** using `intervals[i][1] < ns` (strict) in Phase 1
  and `intervals[i][0] <= ne` (non-strict) in Phase 2 makes `[1,3]` and `[3,5]`
  merge, matching the closed-interval convention.
- **Empty input** returns `[newInterval]` — Phases 1 and 3 do nothing, Phase 2
  appends the untouched new interval.
- **New interval before everything** (e.g. insert `[0,0]` into `[[3,4]]`): Phase 2
  runs zero times, so `[0,0]` is appended first, then `[3,4]` in Phase 3.
- **New interval after everything:** all intervals leave in Phase 1, then the new
  one is appended last.
- **New interval swallows several intervals:** Phase 2's `max(ends)` guarantees the
  end grows to cover fully-contained intervals like `[6,7]` inside `[4,8]`.
