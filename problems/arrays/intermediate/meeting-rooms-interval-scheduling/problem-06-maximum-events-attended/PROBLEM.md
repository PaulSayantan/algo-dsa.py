# Maximum Number of Events That Can Be Attended

**Difficulty:** Hard

**Source:** LeetCode 1353 — Maximum Number of Events That Can Be Attended

## Description

You are given an array of `events` where `events[i] = [startDay_i, endDay_i]`. Event
`i` starts at `startDay_i` and ends at `endDay_i`, both inclusive.

You can attend an event `i` on any single day `d` such that
`startDay_i <= d <= endDay_i`. You can attend **only one event per day** (even though
several events may be available that day). An event occupies exactly one day of your
schedule.

Return the **maximum number of events** you can attend.

## Constraints

- `1 <= events.length <= 10^5`
- `events[i].length == 2`
- `1 <= startDay_i <= endDay_i <= 10^5`

## Examples

### Example 1

```
Input:  events = [[1, 2], [2, 3], [3, 4]]
Output: 3
Explanation: Attend [1, 2] on day 1, [2, 3] on day 2, and [3, 4] on day 3.
             All three events are attended.
```

### Example 2

```
Input:  events = [[1, 2], [2, 3], [3, 4], [1, 2]]
Output: 4
Explanation: Day 1 -> attend the first [1, 2]. Day 2 -> attend the duplicate [1, 2].
             Day 3 -> attend [2, 3]. Day 4 -> attend [3, 4]. All four are attended.
```

### Example 3

```
Input:  events = [[1, 1], [1, 1], [1, 1]]
Output: 1
Explanation: All three events can only be attended on day 1, but you may attend just
             one event per day, so at most one event is possible.
```

## Hint

Use **Meeting Rooms / Interval Scheduling** with a greedy twist: sweep the calendar day
by day, and each day attend the currently-available event that **ends soonest** (track
open events in a min-heap keyed by end day). Postponing an event that ends later keeps
more options alive.
