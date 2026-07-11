# Remove Covered Intervals — Solution

## Brute Force

For every interval, check all other intervals to see if any one covers it. Count
the intervals that are **not** covered by anyone.

```python
def removeCoveredIntervals(intervals):
    n = len(intervals)
    covered = [False] * n
    for i in range(n):
        for j in range(n):
            if i != j and intervals[j][0] <= intervals[i][0] and intervals[i][1] <= intervals[j][1]:
                # Careful: identical intervals would cover each other; the
                # problem guarantees uniqueness so this is safe.
                covered[i] = True
                break
    return n - sum(covered)
```

- **Time:** `O(n^2)`.
- **Space:** `O(n)` (or `O(1)` if you count on the fly).

With `n <= 1000` this passes, but it does redundant work and the coverage
comparison has subtle tie issues. Sorting gives a cleaner `O(n log n)` sweep.

## Optimal Approach (sort + Merge-Intervals sweep)

The key is the **sort order**:

- Sort by `start` **ascending**.
- When two intervals share a start, sort by `end` **descending**.

After this sort, whenever we reach an interval it already has a start `>=` every
interval before it. So it is covered **iff** its end is `<=` the maximum end seen
so far. We sweep left to right, keep `prev_end` = largest end encountered, and
count the survivors.

```python
def removeCoveredIntervals(intervals):
    intervals.sort(key=lambda iv: (iv[0], -iv[1]))
    count = 0
    prev_end = -1
    for _, end in intervals:
        if end > prev_end:      # not covered -> a new "outer" interval
            count += 1
            prev_end = end
        # else: end <= prev_end -> covered, skip it
    return count
```

**Why the tie-break matters:** consider `[1,4]` and `[1,2]`. Both start at 1, and
`[1,2]` is covered by `[1,4]`. Sorting end **descending** places `[1,4]` first, so
`prev_end` becomes 4 and `[1,2]` is correctly seen as covered (`2 <= 4`). If we had
sorted end ascending, `[1,2]` would be processed first and wrongly counted as a
survivor before `[1,4]` widened the window.

**Why comparing only `end` to `prev_end` suffices:** because starts are
non-decreasing, the current interval's `start >= prev interval's start <=` the
start of whichever interval produced `prev_end`. Coverage requires the outer
start `<=` current start (true by sort order) **and** outer end `>=` current end
(exactly the `end <= prev_end` test). So the single end comparison captures full
coverage.

- **Time:** `O(n log n)` for the sort, `O(n)` for the sweep.
- **Space:** `O(1)` beyond the sort.

## Key Insights & Edge Cases

- **The tie-break `(start asc, end desc)` is essential** and is the part people
  most often get wrong.
- **Uniqueness matters for the brute force**: two identical intervals would each
  "cover" the other; the problem forbids duplicates, and the sort-based sweep
  naturally counts identical-start intervals once regardless.
- **Nested chains** like `[[1,10],[2,9],[3,8]]` collapse to 1 — `prev_end` stays
  10 and every later end is smaller.
- **Fully disjoint intervals** like `[[1,2],[3,4],[5,6]]` yield the full count 3,
  since each end strictly exceeds the previous.
- **Single interval** trivially returns 1.
