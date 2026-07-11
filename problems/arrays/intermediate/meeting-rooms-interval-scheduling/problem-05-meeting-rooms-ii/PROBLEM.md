# Meeting Rooms II

**Difficulty:** Medium

**Source:** LeetCode 253 — Meeting Rooms II

## Description

Given an array of meeting time intervals `intervals` where
`intervals[i] = [start_i, end_i]`, return the **minimum number of conference rooms**
required so that no meeting is ever left without a room.

Equivalently, return the maximum number of meetings that are in progress at the same
time. A meeting that ends exactly when another begins (`prev_end == next_start`) can
reuse the same room — they are not simultaneously in progress.

## Constraints

- `1 <= intervals.length <= 10^4`
- `0 <= start_i < end_i <= 10^6`

## Examples

### Example 1

```
Input:  intervals = [[0, 30], [5, 10], [15, 20]]
Output: 2
Explanation: [0, 30] runs the whole time. [5, 10] overlaps it (needs a 2nd room), then
             ends; [15, 20] can reuse that freed room. Peak simultaneous meetings = 2.
```

### Example 2

```
Input:  intervals = [[7, 10], [2, 4]]
Output: 1
Explanation: [2, 4] finishes before [7, 10] starts, so a single room is reused for
             both meetings.
```

### Example 3

```
Input:  intervals = [[1, 5], [5, 10], [2, 7]]
Output: 2
Explanation: At time 2-5 both [1, 5] and [2, 7] are running, needing 2 rooms. [5, 10]
             starts exactly when [1, 5] ends, so it reuses that room. Peak = 2.
```

## Hint

Use **Meeting Rooms / Interval Scheduling**: sort by start time and keep a min-heap of
the end times of meetings currently using a room. Reuse a room whenever the earliest
end time is free; the heap's peak size is the answer.
