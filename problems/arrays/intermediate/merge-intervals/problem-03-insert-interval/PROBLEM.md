# Insert Interval

**Difficulty:** Medium

**Source:** LeetCode 57 — Insert Interval

## Description

You are given an array `intervals` representing a set of **non-overlapping**
intervals sorted in ascending order by their start, where
`intervals[i] = [start_i, end_i]`. You are also given a single interval
`newInterval = [start, end]`.

Insert `newInterval` into `intervals` so that the result is still sorted by start
and still contains no overlapping intervals (merging overlaps as needed). Return
the resulting array.

You should **not** need to re-sort the whole list — the input is already sorted,
and the new interval affects only a contiguous run of existing intervals.

## Constraints

- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^5`
- `intervals` is sorted by `start_i` in ascending order and has no overlaps.
- `newInterval.length == 2`
- `0 <= start <= end <= 10^5`

## Examples

**Example 1**

```
Input:  intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Explanation: [2,5] overlaps [1,3] (2 <= 3), merging to [1,5]. It does not reach
             [6,9] (5 < 6), so [6,9] is left untouched.
```

**Example 2**

```
Input:  intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: [4,8] overlaps [3,5], [6,7], and [8,10]. Merging those three with
             [4,8] yields [3,10]. [1,2] (before) and [12,16] (after) are unchanged.
```

**Example 3**

```
Input:  intervals = [], newInterval = [5,7]
Output: [[5,7]]
Explanation: There is nothing to merge with, so the new interval is the entire
             result.
```

## Hint

Because the existing intervals are already sorted and disjoint, you can insert in
a single linear pass without re-sorting: emit every interval strictly before the
new one, **merge** the block that overlaps it (this is the **Merge Intervals**
step), emit the merged interval, then emit everything strictly after it.
