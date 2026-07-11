# The Skyline Problem — Solution

## Brute Force

Evaluate the max height at every unit of x.

- Collect all critical x-coordinates (all lefts and rights). For each critical
  `x`, scan all `n` buildings and take the max height of those covering `x`
  (i.e. `left <= x < right`); record `[x, maxHeight]` and finally suppress
  consecutive equal heights.
- Time: `O(n^2)` (for each of up to `2n` coordinates, scan all `n` buildings).
  Space: `O(n)`.

At `n = 10^4` that is `~10^8` operations. Correct but slow, and it recomputes
the max from scratch at every coordinate instead of maintaining it
incrementally.

## Optimal Approach — Sweep Line (1D events) + max-heap frontier

Unlike the counter/sum sweeps, the skyline's value at a point is the **maximum**
of the active heights, so the running state is a **multiset of active heights**
rather than a scalar. A max-heap (with lazy deletion) maintains that maximum in
`O(log n)` per event.

Build events:

- For each building `[l, r, h]`, a **start** event at `x = l` carrying height
  `h`, and an **end** event at `x = r` carrying height `h`.
- Sort events by `x`. **Tie rules to get corners right:** at the same `x`,
  process **starts before ends**, and among starts process **taller first**,
  among ends process **shorter first**. A compact trick that encodes all of this
  is to represent a start as `(l, -h, r)` and an end as `(r, 0, 0)` and sort the
  tuples: negative start-heights sort before the `0` end-marker at the same `x`,
  and a taller start (more negative) sorts before a shorter one.

Sweep the events maintaining a max-heap of `(-h, end_x)` for active buildings:

1. On a start event, push `(-h, r)`.
2. Lazily discard heap-top entries whose `end_x <= x` (their buildings have
   ended and no longer cross the line).
3. The current skyline height is `-heap[0][0]` (or `0` if the heap is empty
   apart from the ground sentinel).
4. If this height differs from the last emitted height, append `[x, height]`.

### Why it is correct

At any x, the skyline height is the tallest building whose span covers x. The
heap holds exactly the heights of buildings currently crossing the sweep line
(lazy deletion removes those whose right edge has been passed), so its max is the
skyline height there. The height can only change at a building edge — an event
coordinate — so checking after each event catches every change. Emitting only
when the max differs from the previous emitted value enforces the
"no consecutive equal-height segments" rule and produces the minimal key-point
list. The tie rules ensure that at a shared x the tallest relevant height is
resolved before we read the max (rising edges win over the falling edge at the
same x).

### Step-by-step (Example 1)

`buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]`

```
x=2  start h=10       heap max = 10  -> emit [2, 10]
x=3  start h=15       heap max = 15  -> emit [3, 15]
x=5  start h=12       heap max = 15  (unchanged, no emit)
x=7  end   h=15       heap max = 12  -> emit [7, 12]
x=9  end   h=10       heap max = 12  (unchanged)
x=12 end   h=12       heap empty     -> emit [12, 0]
x=15 start h=10       heap max = 10  -> emit [15, 10]
x=19 start h=8        heap max = 10  (unchanged)
x=20 end   h=10       heap max = 8   -> emit [20, 8]
x=24 end   h=8        heap empty     -> emit [24, 0]
```

Output = `[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]`.

### Reference implementation

```python
import heapq
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # start -> (x, -h, right);  end -> (x, 0, 0)
        events = []
        for l, r, h in buildings:
            events.append((l, -h, r))
            events.append((r, 0, 0))
        events.sort()

        result = []
        heap = [(0, float("inf"))]   # (neg height, end x) ground sentinel
        for x, neg_h, r in events:
            # lazily drop buildings whose right edge we have passed
            while heap[0][1] <= x:
                heapq.heappop(heap)
            if neg_h != 0:                 # a start event
                heapq.heappush(heap, (neg_h, r))
            cur = -heap[0][0]
            if not result or result[-1][1] != cur:
                result.append([x, cur])
        return result
```

- **Time:** `O(n log n)` — sorting `2n` events plus `O(log n)` heap work each.
  Lazy deletions are amortised (each building is pushed and popped at most once).
- **Space:** `O(n)` — events and heap.

## Key Insights & Edge Cases

- **Frontier is a max, not a count.** This is the qualitative jump from the
  earlier problems: you keep a heap/multiset and read its extremum, paying an
  extra `log n` per event.
- **Lazy deletion** avoids the cost of removing an arbitrary element from a
  binary heap. Discard stale tops only when they surface, using each entry's
  stored `end_x`. (A balanced multiset / `SortedList` supports exact deletion
  and works too.)
- **Tie handling drives the corners.** Starts before ends, taller starts first,
  shorter ends first. The `(x, -h, r)` vs `(x, 0, 0)` encoding bakes these in:
  Example 2 `[[0,2,3],[2,5,3]]` correctly suppresses the point at `x=2` because
  the height stays `3`; Example 3 emits only the tallest, `[1,3]`, at the shared
  left edge.
- **Ground sentinel** `(0, inf)` in the heap keeps `heap[0]` always valid and
  makes the "drop to `0`" key point fall out naturally when all real buildings
  have ended.
- **Consecutive equal heights** (abutting equal-height buildings, or a taller
  building fully shadowing a shorter one) are suppressed by the
  `result[-1][1] != cur` guard — this is required by the problem.
- **Large coordinates/heights** (up to `2^31 - 1`) are fine in Python; in typed
  languages use 32/64-bit integers appropriately.
