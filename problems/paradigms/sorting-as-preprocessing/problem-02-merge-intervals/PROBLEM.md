# Merge Intervals

**Difficulty:** Medium

**Source:** LeetCode 56 (Merge Intervals)

## Description

You are given an array `intervals` where `intervals[i] = [start_i, end_i]` represents a
closed interval. **Merge all overlapping intervals** and return an array of the
non-overlapping intervals that cover all the intervals in the input.

Two intervals `[a, b]` and `[c, d]` overlap (and must be merged) when they touch or
intersect, i.e. `c <= b`. The merged interval spans `[a, max(b, d)]`.

Return the merged intervals in any order (conventionally sorted by start).

## Constraints

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^4`

## Examples

**Example 1**

```
Input:  intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
Output: [[1, 6], [8, 10], [15, 18]]
Explanation: [1,3] and [2,6] overlap because 2 <= 3, so they merge into [1,6].
[8,10] and [15,18] do not overlap with anything, so they stay as-is.
```

**Example 2**

```
Input:  intervals = [[1, 4], [4, 5]]
Output: [[1, 5]]
Explanation: [1,4] and [4,5] are considered overlapping because they touch at 4
(4 <= 4), so they merge into [1,5].
```

**Example 3**

```
Input:  intervals = [[1, 4], [2, 3]]
Output: [[1, 4]]
Explanation: [2,3] is fully contained inside [1,4] (2 <= 4), so the merge keeps the
wider end: max(4, 3) = 4, giving [1,4].
```

## Hint

Use **Sorting as Preprocessing**: sort the intervals by start time so that any interval
that could merge with the current one appears immediately next, letting you merge in a
single greedy left-to-right pass.
