# Car Pooling — Solution

## Brute Force

Directly compute the load at every location.

- For each of the up to `1001` distinct locations `x`, sum
  `numPassengers_i` over all trips with `from_i <= x < to_i`; if any location's
  sum exceeds `capacity`, return `false`.
- Time: `O(L * n)` where `L` is the coordinate range (`~1000`) — here about
  `10^6`, tolerable but tied to the coordinate range. Space: `O(1)`.

For larger or unbounded coordinates this coordinate-scan becomes impractical.
The sweep line removes the dependence on `L`.

## Optimal Approach — Sweep Line (1D events)

This is the overlap counter with **weights**. Each trip `[n, from, to]` emits:

- a **pickup** event at `from` with delta `+n`,
- a **drop-off** event at `to` with delta `-n`.

Sort events by location. **Tie rule:** at an equal location, apply the
**drop-off (`-n`) before the pickup (`+n`)**, matching the half-open
`[from, to)` semantics (seats free at `to` are available to a pickup at `to`).
Conveniently, sorting `(location, delta)` tuples achieves this automatically
because negative deltas sort before positive ones.

Sweep left to right maintaining `onboard`, the running sum of passengers in the
car. After each event, if `onboard > capacity`, the trips are infeasible; return
`false`. If the sweep completes without breaching capacity, return `true`.

### Why it is correct

Between two consecutive event locations the set of active trips is constant, so
`onboard` is exactly the number of passengers in the car over that whole
sub-segment. The load can only change at an event location, so evaluating
`onboard` right after each event examines every distinct load value the car ever
carries — including the maximum. The car is feasible iff that maximum stays
`<= capacity`, which is exactly the check performed.

### Step-by-step (Example 1: `trips = [[2,1,5],[3,3,7]], capacity = 4`)

Events, drop-offs before pickups on ties:

```
(1, +2)  onboard = 2   (<= 4 ok)
(3, +3)  onboard = 5   (> 4  -> return False)
```

The load reaches `5` on the segment `[3, 5)`, exceeding `4`, so the answer is
**false**. With `capacity = 5` (Example 2) the same peak `5` is `<= 5`, so the
sweep finishes and returns **true**.

Example 3 (`[[2,1,5],[3,5,7]], capacity = 3`) shows the tie rule in action:

```
(1, +2)  onboard = 2
(5, -2)  onboard = 0   # drop-off at 5 applied BEFORE the pickup at 5
(5, +3)  onboard = 3   (<= 3 ok)
(7, -3)  onboard = 0
```

Peak `3 <= 3`, so **true**.

### Reference implementation

```python
from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for n, frm, to in trips:
            events.append((frm, n))    # pickup:  +n
            events.append((to, -n))    # dropoff: -n
        # (location, delta) sort makes -n come before +n at the same location,
        # which is the half-open [from, to) behaviour.
        events.sort()

        onboard = 0
        for _, delta in events:
            onboard += delta
            if onboard > capacity:
                return False
        return True
```

Because coordinates are bounded by `1000`, a **difference array** is an equally
idiomatic sweep: `diff[from] += n`, `diff[to] -= n`, then check every prefix
sum against `capacity` — `O(n + range)` time, no sort.

- **Time:** `O(n log n)` for the event sort (or `O(n + range)` with a diff
  array). Space: `O(n)` (or `O(range)`).

## Key Insights & Edge Cases

- **Weight, not count.** The only change from Meeting Rooms II is that the delta
  is `numPassengers` instead of `1`, and you compare the running sum against a
  threshold instead of tracking a peak.
- **Half-open tie rule matters.** Example 3 would wrongly return `false` if a
  pickup at `5` were applied before the drop-off at `5`. Sorting by
  `(location, delta)` gives the correct drop-off-first order for free.
- **Never turning around** is what makes this a 1D problem — locations only
  increase, so a single left-to-right sweep suffices.
- **Early exit:** you can return `false` the instant `onboard` exceeds capacity;
  no need to finish the sweep.
- With bounded small coordinates, the difference-array variant avoids sorting
  and is often the cleanest implementation for this specific constraint set.
