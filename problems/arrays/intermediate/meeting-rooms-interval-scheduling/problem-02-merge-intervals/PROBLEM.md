# Merge Intervals

**Difficulty:** Medium

**Source:** LeetCode 56 — Merge Intervals

## Description

Given an array of intervals where `intervals[i] = [start_i, end_i]`, merge all
overlapping intervals and return an array of the non-overlapping intervals that cover
all the intervals in the input.

Two intervals overlap if they share at least one point, **including touching
endpoints**: `[1, 4]` and `[4, 5]` overlap and merge into `[1, 5]`.

The returned intervals may be in any order, but the canonical answer is sorted by start
time.

## Constraints

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^4`

## Examples

### Example 1

```
Input:  intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
Output: [[1, 6], [8, 10], [15, 18]]
Explanation: Intervals [1, 3] and [2, 6] overlap (2 <= 3), so they merge into [1, 6].
             [8, 10] and [15, 18] do not touch anything and pass through unchanged.
```

### Example 2

```
Input:  intervals = [[1, 4], [4, 5]]
Output: [[1, 5]]
Explanation: [1, 4] and [4, 5] touch at the point 4, which counts as overlapping,
             so they merge into [1, 5].
```

### Example 3

```
Input:  intervals = [[1, 4], [0, 4]]
Output: [[0, 4]]
Explanation: After sorting by start we get [[0, 4], [1, 4]]. Since 1 <= 4 they overlap
             and merge into [0, 4].
```

## Hint

Use **Meeting Rooms / Interval Scheduling**: sort by start time, then walk left to
right keeping the current merged block. Extend the block when the next interval starts
before (or at) the block's end; otherwise close it off and start a new one.
