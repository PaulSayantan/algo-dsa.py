# Merge Intervals — Solution

## Brute Force

Repeatedly scan every pair of intervals; whenever two overlap, replace them with
their union and restart the scan. Keep going until a full pass makes no merges.

- **Time:** `O(n^2)` per pass and up to `O(n)` passes → `O(n^3)` worst case
  (or `O(n^2)` with a smarter union-find style grouping).
- **Space:** `O(n)`.

This is correct but wasteful: it rechecks pairs that can never overlap and does
not exploit any ordering.

## Optimal Approach (Merge Intervals)

Sort the intervals by start, then sweep once:

1. **Sort** `intervals` ascending by `start`.
2. Initialize the output with the first interval.
3. For each subsequent interval `[s, e]`, compare `s` to the end of the **last**
   interval in the output, call it `[ps, pe]`:
   - If `s <= pe`, they overlap (or touch), so merge by setting
     `pe = max(pe, e)`.
   - Otherwise there is a gap, so append `[s, e]` as a new interval.

```python
def merge(intervals):
    intervals.sort(key=lambda iv: iv[0])
    merged = [intervals[0]]
    for s, e in intervals[1:]:
        if s <= merged[-1][1]:          # overlap or touch
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])
    return merged
```

**Why it is correct:** after sorting by start, consider the last interval in
`merged`, which has the largest start seen so far. Any interval that overlaps some
earlier-added interval must also overlap this last one (because its start is
`>=` all previous starts, if it slips past the current end it cannot reach back to
an earlier interval that ended even sooner). So comparing only against the last
merged interval never misses an overlap. Taking `max(pe, e)` handles the case
where the new interval is fully contained (`e < pe`) as well as the case where it
extends the window (`e > pe`).

- **Time:** `O(n log n)` dominated by the sort; the sweep is `O(n)`.
- **Space:** `O(n)` for the output (`O(log n)` to `O(n)` auxiliary for sorting,
  language dependent). Sorting in place makes it output-only extra space.

## Key Insights & Edge Cases

- **Touching counts as overlap** here (`[1,4]` + `[4,5]` = `[1,5]`) because
  intervals are closed. If the problem used half-open intervals you would use the
  strict comparison `s < pe` instead of `s <= pe`.
- **Full containment** (`[1,4]` swallowing `[2,3]`) is handled by
  `max(pe, e)` — never assume the later interval extends the end.
- **Single interval** input returns a copy of that interval unchanged.
- **Already-disjoint, unsorted input** like `[[3,4],[1,2]]` still works because we
  sort first; forgetting to sort is the most common bug.
- **Mutating vs copying:** appending references to the input rows (as above) lets
  later `max` writes mutate shared lists; if the caller reuses `intervals`,
  append copies `[s, e]` instead.
