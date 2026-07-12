# Design Underground System

**Difficulty:** Medium

**Source:** LeetCode 1396 — Design Underground System

## Description

Track travel times in a subway. `checkIn(id, station, t)` and `checkOut(id, station, t)` bracket a trip; `getAverageTime(start, end)` returns the average travel time over all completed trips from `start` to `end`.

## Examples

### Example 1

```
Input:  one A->B trip of 5
Output: 5.0
```

## Hint

id -> (startStation, startTime); (start,end) -> [totalTime, tripCount]; average = total/count.
