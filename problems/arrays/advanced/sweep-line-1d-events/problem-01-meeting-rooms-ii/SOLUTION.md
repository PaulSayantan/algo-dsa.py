# Meeting Rooms II — Solution

## Brute Force

Ask, at every "interesting" time, how many meetings are live.

- Collect all distinct start times. For each start time `t`, scan all `n`
  meetings and count how many satisfy `start_i <= t < end_i`. Track the maximum.
- Time: `O(n^2)` (for each of up to `n` candidate instants, scan all `n`
  meetings). Space: `O(1)` beyond the input.

Correct but quadratic; at `n = 10^4` that is `10^8` comparisons, which is
wasteful given the structure of the problem.

## Optimal Approach — Sweep Line (1D events)

Every meeting `[s, e)` contributes exactly two events:

- a **start** event at coordinate `s` with delta `+1` (a room becomes occupied),
- an **end** event at coordinate `e` with delta `-1` (a room is freed).

Sort all `2n` events by coordinate. **Tie rule:** when a start and an end share
the same coordinate, process the **end first**. This encodes the half-open
`[start, end)` semantics — a room freed at time `t` is available to a meeting
that starts at `t`, so they must not both count as "occupied" at `t`.

Sweep through the sorted events maintaining `cur` (rooms in use right now).
Add each delta to `cur`; the answer is the maximum value `cur` ever reaches.

### Why it is correct

`cur` after processing all events up to (and including) coordinate `t` equals
the number of meetings whose interval covers the instant just after the last
processed event — i.e. the concurrency. The minimum number of rooms is, by
definition, the maximum concurrency over the whole timeline. Since every meeting
begins and ends at some event coordinate, the concurrency can only change *at*
an event, so scanning the events captures every value `cur` can take, including
its peak. The end-before-start tie rule guarantees a hand-off at a shared
endpoint is counted as reuse (peak does not spuriously increase).

### Step-by-step (Example 1: `[[0,30],[5,10],[15,20]]`)

Events, with end-before-start ordering on ties:

```
(0,  +1)  cur = 1   max = 1     # [0,30] starts
(5,  +1)  cur = 2   max = 2     # [5,10] starts
(10, -1)  cur = 1               # [5,10] ends
(15, +1)  cur = 2   max = 2     # [15,20] starts
(20, -1)  cur = 1               # [15,20] ends
(30, -1)  cur = 0               # [0,30] ends
```

Answer = `max` = **2**.

### Reference implementation

```python
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []
        for s, e in intervals:
            events.append((s, 1))    # start: +1
            events.append((e, -1))   # end:   -1
        # Sort by time; at equal time the end (-1) sorts before the start (+1)
        # because -1 < 1, which gives the half-open [start, end) behaviour.
        events.sort()

        cur = best = 0
        for _, delta in events:
            cur += delta
            best = max(best, cur)
        return best
```

An equivalent and very common variant is the **two-pointer** form: sort start
times and end times into two separate arrays, then walk both; increment a room
counter when the next start precedes the next end, otherwise advance the end
pointer. It is the same sweep, just with the `+1/-1` stream split by sign.

- **Time:** `O(n log n)` — dominated by sorting `2n` events.
- **Space:** `O(n)` — the event list.

## Key Insights & Edge Cases

- **Tie-breaking is the crux.** Sorting `(time, delta)` tuples makes `-1` (end)
  come before `+1` (start) automatically because `-1 < 1`. If you instead
  processed starts first on ties, Example 3 `[[1,5],[5,9],[9,12]]` would report
  `2` rooms instead of the correct `1`.
- **The answer is a peak, not a final value.** `cur` returns to `0` at the end;
  you must record the running maximum, not the last value.
- **Single meeting** → exactly `1` room. **Empty list** (if allowed) → `0`.
- If start/end times are small bounded integers, you can skip the sort entirely
  and use a **difference array**: `diff[s] += 1`, `diff[e] -= 1`, then take the
  max prefix sum — `O(n + range)` time.
- Fully nested meetings like `[[0,30],[5,10]]` are handled naturally: the inner
  meeting bumps `cur` to `2` while the outer is still open.
