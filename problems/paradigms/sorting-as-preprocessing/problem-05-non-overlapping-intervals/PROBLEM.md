# Non-overlapping Intervals

**Difficulty:** Medium

**Source:** LeetCode 435 (Non-overlapping Intervals)

## Description

Given an array `intervals` where `intervals[i] = [start_i, end_i]`, return the
**minimum number of intervals you need to remove** so that the remaining intervals are
non-overlapping.

Intervals that only touch at an endpoint — such as `[1, 2]` and `[2, 3]` — are considered
**non-overlapping** (they may both stay).

## Constraints

- `1 <= intervals.length <= 10^5`
- `intervals[i].length == 2`
- `-5 * 10^4 <= start_i < end_i <= 5 * 10^4`

## Examples

**Example 1**

```
Input:  intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
Output: 1
Explanation: Removing [1, 3] leaves [1, 2], [2, 3], [3, 4], which are non-overlapping
(they only touch at endpoints). No single removal other than [1,3] achieves this, and
zero removals is impossible because [1,3] overlaps both [1,2] and [2,3].
```

**Example 2**

```
Input:  intervals = [[1, 2], [1, 2], [1, 2]]
Output: 2
Explanation: All three intervals are identical and mutually overlap, so you must remove
two of them, leaving a single [1, 2].
```

**Example 3**

```
Input:  intervals = [[1, 2], [2, 3]]
Output: 0
Explanation: [1, 2] and [2, 3] only touch at the point 2, which does not count as
overlapping, so nothing needs to be removed.
```

## Hint

Use **Sorting as Preprocessing**: sort the intervals by **end** time, then greedily keep
the interval that finishes earliest (classic activity-selection). Every interval that
would overlap the last kept one is a required removal.
