# Meeting Rooms II

**Difficulty:** Medium

**Source:** LeetCode 253 — "Meeting Rooms II"

## Description

You are given an array `intervals` where `intervals[i] = [start_i, end_i]`
represents the start and end times of the `i`-th meeting. A meeting occupies a
room for the half-open interval `[start_i, end_i)` — that is, a meeting that
ends exactly when another begins can hand off the **same** room (no conflict at
the shared instant).

Return the **minimum number of conference rooms** required so that no two
meetings that overlap in time share a room.

Equivalently: over all instants `t`, what is the **maximum number of meetings
that are simultaneously in progress**? That peak is the number of rooms you must
have.

## Constraints

- `1 <= intervals.length <= 10^4`
- `0 <= start_i < end_i <= 10^6`

## Examples

### Example 1

```
Input:  intervals = [[0, 30], [5, 10], [15, 20]]
Output: 2
Explanation:
  At time 5, meetings [0,30] and [5,10] are both running  -> 2 concurrent.
  At time 15, meetings [0,30] and [15,20] are running      -> 2 concurrent.
  The peak concurrency is 2, so 2 rooms are needed.
```

### Example 2

```
Input:  intervals = [[7, 10], [2, 4]]
Output: 1
Explanation:
  The two meetings never overlap ([2,4) ends before [7,10) starts),
  so a single room can host both in sequence. Peak concurrency = 1.
```

### Example 3

```
Input:  intervals = [[1, 5], [5, 9], [9, 12]]
Output: 1
Explanation:
  Each meeting ends exactly when the next begins. Because rooms are freed at
  the end instant (half-open [start, end)), one room is reused three times.
  Peak concurrency = 1.
```

## Hint

Split every meeting into two point events — a `+1` at its start and a `-1` at
its end — then apply a **Sweep Line (1D events)**: process the events in time
order while keeping a running count of meetings in progress, and remember its
maximum. Think carefully about which event wins a tie when a start and an end
share the same coordinate.
