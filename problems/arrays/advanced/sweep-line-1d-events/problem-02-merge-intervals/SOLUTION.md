# Merge Intervals — Solution

## Brute Force

Repeatedly scan for any overlapping pair and fuse it.

- For every pair `(i, j)`, if they overlap, replace them with their union and
  restart. Repeat until no pair overlaps.
- Time: `O(n^3)` in the worst case (`O(n^2)` pairs per pass, up to `O(n)`
  passes). Space: `O(n)`.

A much better classic approach is **sort by start, then a single linear pass**:
keep the last merged interval and either extend it (`start <= last_end`) or push
a new one. That is `O(n log n)`. The sweep-line formulation below is the same
`O(n log n)` cost expressed as an event stream, which generalises cleanly to
weighted variants and to "total covered length".

## Optimal Approach — Sweep Line (1D events)

Each closed interval `[s, e]` becomes two events:

- a **start** event at `s` with delta `+1`,
- an **end** event at `e` with delta `-1`.

Sort events by coordinate. **Tie rule (the important part):** at an equal
coordinate, process **starts before ends**. Because the intervals are *closed*,
`[1,4]` and `[4,5]` must merge; processing the start of `[4,5]` before the end
of `[1,4]` keeps the open-count from ever dipping to `0` at the shared point
`4`, so no artificial split happens there.

Sweep left to right maintaining `cur`, the number of currently open intervals:

- When `cur` is `0` and we hit a `+1`, a new merged interval **opens** here —
  record its left endpoint.
- After applying deltas, whenever `cur` returns to `0`, the merged interval
  **closes** at the current coordinate — emit `[left, coord]`.

### Why it is correct

`cur > 0` exactly over the set of points covered by at least one input interval;
the maximal runs where `cur > 0` are precisely the connected components of the
union — i.e. the merged intervals. Recording the coordinate where `cur` leaves
`0` and the coordinate where it returns to `0` reproduces each component's
endpoints. The start-before-end tie rule ensures closed touching intervals stay
in the same component.

### Step-by-step (Example 1: `[[1,3],[2,6],[8,10],[15,18]]`)

Events sorted by `(coord, start-before-end)`:

```
(1,  +1)  cur 0->1   open a segment at 1
(2,  +1)  cur 1->2
(3,  -1)  cur 2->1
(6,  -1)  cur 1->0   close: emit [1, 6]
(8,  +1)  cur 0->1   open a segment at 8
(10, -1)  cur 1->0   close: emit [8, 10]
(15, +1)  cur 0->1   open a segment at 15
(18, -1)  cur 1->0   close: emit [15, 18]
```

Output = `[[1, 6], [8, 10], [15, 18]]`.

### Reference implementation

```python
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        events = []
        for s, e in intervals:
            # type 0 = start, type 1 = end -> starts sort before ends at a tie,
            # which makes closed *touching* intervals ([1,4] & [4,5]) merge.
            events.append((s, 0, 1))    # +1 at start
            events.append((e, 1, -1))   # -1 at end
        events.sort()

        result = []
        cur = 0
        seg_start = None
        for coord, _type, delta in events:
            if cur == 0 and delta == 1:
                seg_start = coord          # a new merged interval opens
            cur += delta
            if cur == 0:
                result.append([seg_start, coord])   # it closes here
        return result
```

- **Time:** `O(n log n)` — sorting `2n` events.
- **Space:** `O(n)` — events plus output.

## Key Insights & Edge Cases

- **Closed vs. half-open changes the tie rule.** Here (closed intervals)
  starts win ties so touching merges. In Meeting Rooms II (half-open) ends win
  ties so a hand-off is *not* an overlap. Same machinery, opposite tie-break —
  always decide this from the problem's semantics.
- **A single point / zero-length interval** `[x, x]` becomes `+1` then `-1` at
  `x`; with starts-before-ends it opens and immediately closes, emitting
  `[x, x]` correctly.
- **Fully nested** intervals (`[1,4]`, `[2,3]`) never let `cur` reach `0` until
  the outer one ends, so the union is just the outer interval.
- If you only need the **total covered length** (a common cousin), do not emit
  segments — instead add `coord - prev_coord` to an accumulator whenever
  `cur > 0` between consecutive events. Same sweep, different aggregation.
- The plain "sort by start + linear merge" solution is equally optimal and
  simpler for *this* exact problem; the event view earns its keep when weights
  or emitted per-segment values enter the picture (see problems 3 and 4).
