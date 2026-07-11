# Meeting Rooms II — Solution

The minimum number of rooms equals the **maximum number of meetings overlapping at any
single moment** (the peak concurrency).

## Brute Force

For every meeting, count how many other meetings overlap it, or scan a fine-grained
timeline and, at each time unit, count active meetings; take the maximum.

- **Time:** `O(n^2)` for pairwise counting, or `O(n * T)` where `T` is the time range
  for a timeline scan.
- **Space:** `O(1)` or `O(T)`.

Too slow / range-dependent for large inputs.

## Optimal Approach (Meeting Rooms / Interval Scheduling — min-heap of end times)

Sort meetings by **start** time and maintain a **min-heap** whose elements are the end
times of meetings currently occupying a room. The heap's top is the meeting that frees
up its room soonest.

Steps:

1. Sort `intervals` by `start`.
2. Create an empty min-heap `heap` (of end times).
3. For each meeting `[s, e]` in start order:
   - If `heap` is non-empty and `heap[0] <= s`, the earliest-ending meeting has already
     finished — pop it (that room is now free and reused).
   - Push `e` onto the heap (this meeting occupies a room).
4. The answer is the **maximum heap size** observed — which, because we only ever pop at
   most one per iteration before pushing, equals `len(heap)` at the end.

```python
import heapq

def minMeetingRooms(intervals):
    intervals.sort(key=lambda iv: iv[0])
    heap = []  # end times of ongoing meetings
    for s, e in intervals:
        if heap and heap[0] <= s:
            heapq.heappop(heap)   # a room frees up, reuse it
        heapq.heappush(heap, e)
    return len(heap)
```

- **Time:** `O(n log n)` — sort plus up to `n` heap pushes/pops each `O(log n)`.
- **Space:** `O(n)` for the heap in the worst case (all meetings overlap).

### Alternative: two sorted arrays (chronological sweep)

Separate all start and end times into two sorted arrays and sweep with two pointers.
When the next event is a start, increment a room counter (and update the max); when it
is an end, decrement. Same `O(n log n)` time, `O(n)` space, no heap. Treat an end as
occurring before a coincident start so that `prev_end == next_start` reuses a room.

### Why it is correct

Processing meetings in start order guarantees that when we consider meeting `[s, e]`,
every meeting already placed started no later than `s`. The min-heap top is the
smallest end time among ongoing meetings; if it is `<= s`, that room is genuinely free
at time `s` and can be reused, so we do not need a new room. If every ongoing meeting
ends after `s`, all are still in progress and we must allocate a fresh room (the push
grows the heap). Thus the heap size always equals the number of concurrently running
meetings, and its peak is the minimum rooms needed.

## Key Insights & Edge Cases

- **Touching meetings reuse a room:** use `heap[0] <= s` (not `<`) so a meeting starting
  exactly when another ends does not force a new room. Example 3: `[5, 10]` reuses the
  room freed by `[1, 5]`.
- **Because we pop at most one before each push,** the final `len(heap)` already equals
  the running maximum; you do not need a separate max variable in the heap version.
- **Single meeting:** answer is `1`.
- **All identical / fully overlapping meetings:** answer equals `n` (no room is ever
  freed in time).
- Sorting by start time is essential; the heap only tracks *when rooms free up*.
