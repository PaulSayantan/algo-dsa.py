# Longest Consecutive Sequence — Solution

## Brute Force

For each value `x`, try to extend a run upward by repeatedly searching the array
for `x+1`, `x+2`, ... Each search is a linear scan.

```python
best = 0
for x in nums:
    length = 1
    while (x + length) in nums:   # `in` on a list is O(n)
        length += 1
    best = max(best, length)
return best
```

- **Time:** O(n^2) or worse — each `in nums` on a list is O(n), inside two nested
  loops.
- **Space:** O(1).

Sorting is the natural next thought:

```python
nums = sorted(set(nums))
# then walk adjacent elements, resetting the run when the gap is > 1
```

- **Time:** O(n log n) — dominated by the sort.
- **Space:** O(n).

Sorting is fine but does not meet the required **O(n)**. Hashing does.

## Optimal Approach (Hashing)

Insert all values into a hash set `s` (this also deduplicates). The key idea:
**only begin counting a run at its smallest element.** A value `x` is the start of
a run exactly when `x - 1` is not in the set. From each such start, walk upward
`x, x+1, x+2, ...` while each successor is in the set, measuring the run length.

```python
def longestConsecutive(nums):
    s = set(nums)
    best = 0
    for x in s:
        if x - 1 in s:        # x is not the start of its run -> skip
            continue
        length = 1
        y = x
        while y + 1 in s:     # extend upward
            y += 1
            length += 1
        best = max(best, length)
    return best
```

**Why it is correct.** Every consecutive run has a unique smallest element `x0`
(the one for which `x0 - 1` is absent). The `if x - 1 in s: continue` guard ensures
the inner `while` loop runs *only* from that smallest element, and it then counts
the full run. Every run is therefore measured exactly once, and `best` keeps the
maximum.

**Why it is O(n), despite the nested loop.** The inner `while` only ever runs for
run-start elements, and across all runs it advances through each set element at
most once total. So the combined work of all inner loops is O(n), plus O(n) to
build the set and O(n) to iterate it — O(n) overall.

- **Time:** O(n) average — each element is visited a constant number of times.
- **Space:** O(n) — the set of distinct values.

### Trace on `nums = [100, 4, 200, 1, 3, 2]`

Set = {1, 2, 3, 4, 100, 200}.

- `x = 1`: `0` absent -> start. Walk 1->2->3->4 (5 absent). length = 4. best = 4.
- `x = 2, 3, 4`: each has a predecessor in the set -> skipped.
- `x = 100`: `99` absent -> start. `101` absent. length = 1.
- `x = 200`: `199` absent -> start. `201` absent. length = 1.

Result = 4, matching the expected output.

## Key Insights & Edge Cases

- **The predecessor guard is what makes it O(n).** Without `if x - 1 in s`, you
  would re-walk the same run from every element, degrading to O(n^2).
- **Iterate over the set, not the list**, so duplicates do not cause repeated work
  (Example 2's duplicate `0` is collapsed).
- **Empty input** (`[]`): the set is empty, the loop never runs, and `best` stays
  `0`. Correct.
- **Single element** returns `1`.
- **Duplicates** are handled by the set — they never extend a run.
- **Large magnitudes / negatives** hash fine; the algorithm never indexes by value,
  so no bounded-array trick is needed.
