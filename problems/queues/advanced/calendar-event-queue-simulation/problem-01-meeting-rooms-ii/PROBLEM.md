# Meeting Rooms II

**Difficulty:** Medium

**Source:** LeetCode 253 — Meeting Rooms II

## Description

Given `intervals` where `intervals[i] = [start, end]` for meetings, return the minimum number of conference rooms required so no two overlapping meetings share a room.

## Examples

### Example 1

```
Input:  intervals = [[0,30],[5,10],[15,20]]
Output: 2
```

## Hint

Sort by start; a min-heap of end times — if the earliest end <= current start, reuse that room, else allocate.
