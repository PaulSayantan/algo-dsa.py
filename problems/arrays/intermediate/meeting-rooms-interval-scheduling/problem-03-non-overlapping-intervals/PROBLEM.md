# Non-overlapping Intervals

**Difficulty:** Medium

**Source:** LeetCode 435 — Non-overlapping Intervals

## Description

Given an array of intervals `intervals` where `intervals[i] = [start_i, end_i]`,
return the **minimum number of intervals you need to remove** to make the rest of the
intervals non-overlapping.

Intervals that only touch at an endpoint (e.g. `[1, 2]` and `[2, 3]`) are **not**
considered overlapping — they may both stay.

## Constraints

- `1 <= intervals.length <= 10^5`
- `intervals[i].length == 2`
- `-5 * 10^4 <= start_i < end_i <= 5 * 10^4`

## Examples

### Example 1

```
Input:  intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
Output: 1
Explanation: Removing [1, 3] leaves [1, 2], [2, 3], [3, 4], which are non-overlapping.
             No single other removal works, so the minimum is 1.
```

### Example 2

```
Input:  intervals = [[1, 2], [1, 2], [1, 2]]
Output: 2
Explanation: All three intervals are identical and overlap each other. You must remove
             two of them, leaving a single [1, 2].
```

### Example 3

```
Input:  intervals = [[1, 2], [2, 3]]
Output: 0
Explanation: The intervals only touch at the point 2, which is not an overlap, so
             nothing needs to be removed.
```

## Hint

Use **Meeting Rooms / Interval Scheduling**: this is the classic *activity selection*
greedy. Sort by end time and keep as many intervals as possible; every interval you
cannot keep is one removal.
