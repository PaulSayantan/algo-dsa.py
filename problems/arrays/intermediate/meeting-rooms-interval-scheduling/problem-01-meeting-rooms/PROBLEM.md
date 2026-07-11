# Meeting Rooms

**Difficulty:** Easy

**Source:** LeetCode 252 — Meeting Rooms

## Description

Given an array of meeting time intervals `intervals` where
`intervals[i] = [start_i, end_i]`, determine if a single person could attend **all**
meetings.

A person can attend all meetings only if no two meetings overlap. Two meetings that
merely touch at an endpoint (one ends exactly when the next begins, e.g. `[1, 5]` and
`[5, 8]`) are **not** considered overlapping — the person can attend both.

Return `True` if all meetings can be attended, and `False` otherwise.

## Constraints

- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i < end_i <= 10^6`

## Examples

### Example 1

```
Input:  intervals = [[0, 30], [5, 10], [15, 20]]
Output: false
Explanation: The meeting [0, 30] overlaps with both [5, 10] and [15, 20],
             so the person cannot attend all three.
```

### Example 2

```
Input:  intervals = [[7, 10], [2, 4]]
Output: true
Explanation: After sorting by start time we get [[2, 4], [7, 10]]. Meeting [2, 4]
             finishes at 4, well before [7, 10] begins at 7, so there is no overlap.
```

### Example 3

```
Input:  intervals = [[1, 5], [5, 8]]
Output: true
Explanation: The first meeting ends exactly when the second begins. Touching
             endpoints do not count as an overlap, so both can be attended.
```

## Hint

Use **Meeting Rooms / Interval Scheduling**: sort the meetings by their start time,
then walk through neighbouring pairs and look for a start that comes before the
previous meeting's end.
