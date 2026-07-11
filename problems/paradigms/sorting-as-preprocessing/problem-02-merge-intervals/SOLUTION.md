# Merge Intervals — Solution

## Brute Force

Repeatedly scan the list looking for any two intervals that overlap, merge them into one,
and restart. Keep looping until a full pass finds no overlapping pair.

- Each merge can require another `O(n)` scan, and you may need `O(n)` rounds.
- **Time:** `O(n^2)` (or worse if you rescan naively). **Space:** `O(n)` for the output.

The pain comes from overlaps being scattered anywhere in the unsorted list, so you never
know when you're done without rescanning everything.

## Optimal Approach (Sorting as Preprocessing)

**Idea:** Sort the intervals by **start**. After sorting, every interval that could merge
with the current accumulated interval is guaranteed to appear right after it, so a single
left-to-right greedy pass suffices.

**Why it is correct:** After sorting by start, consider the interval you're currently
building, `cur = [lo, hi]`. The next interval `[s, e]` has `s >= lo`. If `s <= hi` they
overlap, and the union is `[lo, max(hi, e)]` — still a single interval starting at `lo`.
If `s > hi`, then because starts are non-decreasing, **no later interval** can start at
or before `hi` either, so `cur` can never grow again and is safely finalized. This is the
invariant that makes one pass sufficient.

**Step by step:**

1. Sort `intervals` by start (ties broken by end, harmless).
2. Initialize the result with the first interval.
3. For each subsequent interval `[s, e]`:
   - Let `last = result[-1]`. If `s <= last[1]`, they overlap — extend:
     `last[1] = max(last[1], e)`.
   - Otherwise start a new block: append `[s, e]`.
4. Return `result`.

```python
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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

- **Time:** `O(n log n)` for the sort, then `O(n)` for the single merge pass.
- **Space:** `O(n)` for the output (or `O(1)` extra beyond output if sort is in place;
  `O(log n)`–`O(n)` for sort internals depending on the language).

## Key Insights & Edge Cases

- **Sort by start, merge greedily.** The sort converts "find overlaps anywhere" into
  "check only your immediate neighbor," collapsing `O(n^2)` to `O(n log n)`.
- **Touching counts as overlap** here (`s <= last[1]`, not `<`), because `[1,4]` and
  `[4,5]` share the point 4. If the problem defined open intervals you would use `<`.
- **Containment:** `max(last[1], e)` correctly keeps the wider end when the new interval
  is fully inside the current one (e.g. `[1,4]` swallowing `[2,3]`).
- **Single interval:** returns it unchanged.
- **Copy the first interval** (`intervals[0][:]`) before mutating its end, so you don't
  clobber the caller's input list.
- **Already-sorted or reverse-sorted input** both work; the sort normalizes either case.
