# Merge Intervals — Solution

## Brute Force

Repeatedly scan the list looking for any two intervals that overlap, merge that pair
into one interval, and restart the scan. Keep going until a full pass finds no
overlapping pair.

- **Time:** `O(n^2)` (or worse) — each merge can trigger another full scan.
- **Space:** `O(n)` for the working list.

Correct but quadratic, because it never exploits the ordering of the intervals.

## Optimal Approach (Meeting Rooms / Interval Scheduling)

Sort by **start** time and sweep once, maintaining the current open merged interval.

Steps:

1. Sort `intervals` by `start`.
2. Initialize `result = [intervals[0]]` (a copy of the first interval).
3. For each subsequent interval `[s, e]`:
   - Let `last = result[-1]`, the most recently emitted merged block.
   - If `s <= last[1]`, the new interval overlaps (or touches) `last`; extend the
     block: `last[1] = max(last[1], e)`.
   - Otherwise there is a gap; append `[s, e]` as a new block.
4. Return `result`.

```python
def merge(intervals):
    intervals.sort(key=lambda iv: iv[0])
    result = [intervals[0][:]]
    for s, e in intervals[1:]:
        last = result[-1]
        if s <= last[1]:            # overlap or touch
            last[1] = max(last[1], e)
        else:
            result.append([s, e])
    return result
```

- **Time:** `O(n log n)` for the sort plus `O(n)` for the sweep.
- **Space:** `O(n)` for the output (`O(log n)` to `O(n)` for the sort itself).

### Why it is correct

After sorting by start, all intervals that belong to one merged block appear
consecutively. The block's running end is the maximum end seen so far in the block.
Any interval whose start is `<= running_end` must intersect the block (its start lies
inside `[block_start, running_end]`), so it belongs to the same block and can only push
the end further right. The first interval whose start exceeds the running end cannot
touch anything already merged (all previous starts were smaller and all previous ends
`<= running_end`), so it safely opens a new block. Hence one pass produces exactly the
maximal merged intervals.

## Key Insights & Edge Cases

- **Use `<=`, not `<`.** Touching intervals `[1, 4]` and `[4, 5]` are defined to
  overlap here (unlike the Meeting Rooms attend-all problem where touching is fine).
- **Take `max` for the end.** A later interval can be *fully contained*
  (`[1, 10]` then `[2, 3]`); `max(last_end, e)` keeps the wider end so you do not
  accidentally shrink the block.
- **Copy the first interval** (`intervals[0][:]`) before mutating it, so you do not
  clobber the caller's input while extending ends in place.
- **Single interval / already disjoint input:** returns the input unchanged (each
  interval becomes its own block).
- Sorting is the only reason the "compare against the last emitted block" trick is
  valid — never skip it.
