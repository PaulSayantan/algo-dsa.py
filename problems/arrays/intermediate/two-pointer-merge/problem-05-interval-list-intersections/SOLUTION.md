# Interval List Intersections — Solution

## Brute Force

Compare every interval in `firstList` against every interval in `secondList`, keeping
each non-empty overlap.

```python
def intervalIntersection(firstList, secondList):
    out = []
    for a, b in firstList:
        for c, d in secondList:
            lo, hi = max(a, c), min(b, d)
            if lo <= hi:
                out.append([lo, hi])
    return out
```

- **Time:** `O(m * n)`.
- **Space:** `O(1)` beyond the output.

Correct (and, because both lists are sorted, the emitted overlaps even come out sorted),
but the nested scan wastes the sorted structure.

## Optimal Approach (Two-Pointer Merge)

Both lists are sorted by start and internally disjoint, so a single merge-style pass
suffices. Keep a pointer `i` into `firstList` and `j` into `secondList`.

For the current pair `firstList[i] = [a, b]` and `secondList[j] = [c, d]`:

1. The overlap is `[max(a, c), min(b, d)]`. If `max(a, c) <= min(b, d)`, record it.
2. Advance the interval that **ends first**: if `b < d`, increment `i`, else increment
   `j`. The one that ends earlier cannot overlap any *later* interval in the other list,
   so we are done with it.

```python
def intervalIntersection(firstList, secondList):
    out = []
    i = j = 0
    while i < len(firstList) and j < len(secondList):
        a, b = firstList[i]
        c, d = secondList[j]
        lo, hi = max(a, c), min(b, d)
        if lo <= hi:
            out.append([lo, hi])
        if b < d:
            i += 1
        else:
            j += 1
    return out
```

**Why it is correct.** Because the lists are sorted and disjoint, once we have compared
`[a, b]` and `[c, d]` and know (say) `b < d`, interval `[a, b]` lies entirely to the left
of every remaining interval in `secondList` beyond overlap already captured, so it can be
retired. We never skip a possible overlap because we only advance past an interval that
has been compared against the interval currently blocking it.

**Step-by-step** on `first = [[0,2],[5,10],[13,23],[24,25]]`,
`second = [[1,5],[8,12],[15,24],[25,26]]`:

| [a,b] / [c,d] | overlap `[max,min]` | emit? | advance (ends first) |
| --- | --- | --- | --- |
| [0,2] / [1,5]   | [1,2]  | yes | b=2 < d=5 -> i++ |
| [5,10] / [1,5]  | [5,5]  | yes | d=5 < b=10 -> j++ |
| [5,10] / [8,12] | [8,10] | yes | b=10 < d=12 -> i++ |
| [13,23] / [8,12]| [13,12] invalid | no | d=12 < b=23 -> j++ |
| [13,23] / [15,24]| [15,23]| yes | b=23 < d=24 -> i++ |
| [24,25] / [15,24]| [24,24]| yes | d=24 < b=25 -> j++ |
| [24,25] / [25,26]| [25,25]| yes | b=25 < d=26 -> i++ |
| i out of range -> stop | | | |

Result: `[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]`.

- **Time:** `O(m + n)` — each interval retired once.
- **Space:** `O(1)` auxiliary beyond the output.

## Key Insights & Edge Cases

- The decisive rule is **advance the interval that ends first** (`min` of the two end
  points); its right edge is the binding constraint.
- Overlap is `[max(starts), min(ends)]`; it is a real interval only when
  `max(starts) <= min(ends)` — use `<=` because the intervals are *closed*, so touching
  endpoints like `[5,10]` and `[1,5]` still share the point `5`.
- Either list empty: the `while` never executes and the result is `[]`.
- Because both lists are sorted, the emitted overlaps are automatically sorted by start
  — no final sort needed.
- One interval can intersect several intervals of the other list (e.g. `[5,10]` meets
  both `[1,5]` and `[8,12]`); advancing only the earlier-ending pointer preserves the
  still-active interval so those multiple overlaps are all found.
