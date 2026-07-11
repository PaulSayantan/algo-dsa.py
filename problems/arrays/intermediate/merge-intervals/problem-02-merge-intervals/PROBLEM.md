# Merge Intervals

**Difficulty:** Medium

**Source:** LeetCode 56 — Merge Intervals

## Description

You are given an array `intervals` where `intervals[i] = [start_i, end_i]`
represents a closed interval on the number line. Merge all **overlapping**
intervals and return an array of the non-overlapping intervals that cover exactly
the same set of points as the input.

Two intervals overlap when they share at least one point, including the case where
one ends exactly where another begins. For example `[1, 4]` and `[4, 5]` overlap
and merge into `[1, 5]`. The returned list may be in any order, though it is
conventional to return it sorted by start.

## Constraints

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^4`

## Examples

**Example 1**

```
Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: [1,3] and [2,6] overlap (2 <= 3), so they merge into [1,6].
             [8,10] and [15,18] overlap with nothing, so they stay as-is.
```

**Example 2**

```
Input:  intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: The intervals touch at the point 4, which counts as overlapping,
             so they merge into [1,5].
```

**Example 3**

```
Input:  intervals = [[1,4],[2,3]]
Output: [[1,4]]
Explanation: [2,3] is entirely inside [1,4]. The merged end is max(4, 3) = 4,
             so the result is the single interval [1,4].
```

## Hint

This is the archetypal **Merge Intervals** problem. Sort the intervals by their
start value, then walk through them keeping one "current" interval; whenever the
next interval's start is `<=` the current interval's end, extend the current
end to the larger of the two ends instead of opening a new interval.
