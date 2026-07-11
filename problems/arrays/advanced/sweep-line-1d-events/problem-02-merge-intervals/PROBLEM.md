# Merge Intervals

**Difficulty:** Medium

**Source:** LeetCode 56 — "Merge Intervals"

## Description

Given an array `intervals` where `intervals[i] = [start_i, end_i]` (a **closed**
interval), merge all overlapping intervals and return an array of the
non-overlapping intervals that together cover exactly the same set of points.

Two intervals overlap if they share at least one point; because the intervals
are closed, intervals that merely **touch** at an endpoint (e.g. `[1, 4]` and
`[4, 5]`) are considered overlapping and must be merged into `[1, 5]`.

The output may be returned in any order, but the conventional and expected form
is sorted by start coordinate.

## Constraints

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^4`

## Examples

### Example 1

```
Input:  intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
Output: [[1, 6], [8, 10], [15, 18]]
Explanation:
  [1,3] and [2,6] overlap (they share the range [2,3]) and merge into [1,6].
  [8,10] and [15,18] overlap with nothing, so they pass through unchanged.
```

### Example 2

```
Input:  intervals = [[1, 4], [4, 5]]
Output: [[1, 5]]
Explanation:
  The intervals touch at the point 4. Since intervals are closed, touching
  counts as overlapping, so they merge into the single interval [1, 5].
```

### Example 3

```
Input:  intervals = [[1, 4], [2, 3]]
Output: [[1, 4]]
Explanation:
  [2,3] is completely contained inside [1,4]. The union is just [1,4].
```

## Hint

Turn each interval into a `+1` start event and a `-1` end event and run a
**Sweep Line (1D events)**. Keep a running count of how many intervals are
currently open: a merged output interval begins the moment the count rises from
`0` and ends the moment it falls back to `0`. To make *touching* intervals
merge, be deliberate about whether a start or an end is processed first when they
share a coordinate.
