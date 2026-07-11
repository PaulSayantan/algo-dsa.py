# Non-overlapping Intervals

**Difficulty:** Medium

**Source:** LeetCode 435 (Non-overlapping Intervals)

## Description

Given an array `intervals` where `intervals[i] = [start_i, end_i]`, return the
**minimum number of intervals you need to remove** so that the remaining intervals
are non-overlapping.

Two intervals that only *touch* at an endpoint — for example `[1, 2]` and `[2, 3]` —
are considered **non-overlapping**.

## Constraints

- `1 <= intervals.length <= 10^5`
- `intervals[i].length == 2`
- `-5 * 10^4 <= start_i < end_i <= 5 * 10^4`

## Examples

### Example 1

```
Input:  intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
Output: 1
```

Explanation: Removing `[1, 3]` leaves `[[1, 2], [2, 3], [3, 4]]`, which are all
non-overlapping. One removal suffices, so the answer is **1**.

### Example 2

```
Input:  intervals = [[1, 2], [1, 2], [1, 2]]
Output: 2
```

Explanation: All three intervals are identical and overlap each other. You must
remove **2** of them to leave a single non-overlapping interval.

### Example 3

```
Input:  intervals = [[1, 2], [2, 3]]
Output: 0
```

Explanation: `[1, 2]` and `[2, 3]` only touch at the endpoint 2 and do not overlap,
so **0** removals are needed.

## Hint

This is interval scheduling in disguise: *keeping* the maximum number of
non-overlapping intervals minimizes removals. Use a **Greedy** rule — sort by end
time and always keep the interval that finishes earliest, leaving the most room for
the rest.
