# Maximum Number of Events That Can Be Attended — Solution

Unlike the earlier problems, an event here is a *flexible* range: you may attend it on
any single day within `[startDay, endDay]`, but only one event per day. The greedy
principle is still "earliest deadline first," but applied day by day instead of once
per interval.

## Brute Force

Model it as bipartite matching between events and days (each event connects to the days
in its range) and find a maximum matching, or try every assignment of events to days.

- **Time:** exponential for brute-force assignment; even the polynomial matching
  (Hopcroft–Karp) is `O(E * sqrt(V))` over up to `10^5` days and events — heavy and
  awkward to implement.
- **Space:** `O(days + events)`.

Overkill given the clean greedy below.

## Optimal Approach (Meeting Rooms / Interval Scheduling — day sweep + min-heap)

Sweep over days in increasing order. On each day, make every event that has *started*
(and not yet expired) available, then attend the available event with the **earliest
end day**. That event is the most "urgent," so consuming today's slot on it — while
deferring events that remain attendable later — is always safe.

Steps:

1. Sort `events` by `startDay` so we can add them to the pool as the day advances.
2. Use a min-heap `heap` of **end days** of currently-open events. Use an index `i`
   into the sorted events.
3. For each `day` from `min start` to `max end`:
   - Push the end day of every event whose `startDay == day` (advance `i` while
     `events[i][0] == day`).
   - Discard expired events from the top of the heap: while `heap` and
     `heap[0] < day`, pop (those events can no longer be attended).
   - If the heap is non-empty, pop the smallest end day and count `attended += 1`
     (attend that event today).
4. Return `attended`.

```python
import heapq

def maxEvents(events):
    events.sort(key=lambda e: e[0])          # by start day
    heap = []                                 # end days of open events
    i, n = 0, len(events)
    attended = 0
    day = 0
    while i < n or heap:
        if not heap:
            # jump to the next event's start day to skip empty gaps
            day = events[i][0]
        # add all events that start on/by today
        while i < n and events[i][0] <= day:
            heapq.heappush(heap, events[i][1])
            i += 1
        # drop events that already ended before today
        while heap and heap[0] < day:
            heapq.heappop(heap)
        if heap:
            heapq.heappop(heap)               # attend earliest-ending event
            attended += 1
        day += 1
    return attended
```

- **Time:** `O(n log n)` — sorting plus each event entering/leaving the heap once at
  `O(log n)`. (Iterating raw days is `O(D + n log n)`; the "jump to next start when the
  heap is empty" trick keeps it near `O(n log n)`.)
- **Space:** `O(n)` for the heap.

### Why the greedy is correct

Consider any day `d` on which at least one event is available. Attending the available
event with the smallest end day is optimal by an exchange argument: if an optimal
schedule attends a different event `B` on day `d` while the earliest-deadline event `A`
(with `endDay_A <= endDay_B`) is attended on some later day `d'` (or not at all), we can
swap them. `A` is still valid on day `d` (it is available), and `B` remains valid on
day `d'` because `d' <= endDay_A <= endDay_B`. The swap keeps the schedule feasible and
does not reduce the count. Repeating the exchange transforms any optimal schedule into
the greedy one, so the greedy attends the maximum number of events.

## Key Insights & Edge Cases

- **Earliest end day wins**, so the heap is keyed on `endDay`. Sorting the array is by
  `startDay` (to know when an event becomes available) — the two keys serve different
  roles.
- **Prune expired events** (`heap[0] < day`) before attending, or you might "attend" an
  event whose deadline already passed.
- **One event per day** is enforced by attending exactly one heap element per day.
- **All events on the same single day** (Example 3, `[[1,1],[1,1],[1,1]]`) → only one
  can be attended → `1`.
- **Sparse calendars:** jumping `day` to the next event's start when the heap empties
  avoids looping over empty days and keeps the runtime tied to `n`, not the day range.
