# Interval List Intersections

**Difficulty:** Medium

**Source:** LeetCode 986 — Interval List Intersections

## Description

You are given two lists of **closed** intervals, `firstList` and `secondList`, where
`firstList[i] = [start_i, end_i]` and `secondList[j] = [start_j, end_j]`. Each list of
intervals is pairwise **disjoint** and **sorted** by start time.

Return the **intersection** of these two interval lists — the set of intervals covered
by *both* lists — also sorted by start time.

A closed interval `[a, b]` (with `a <= b`) contains all real numbers `x` with
`a <= x <= b`. The intersection of two closed intervals `[a, b]` and `[c, d]` is
`[max(a, c), min(b, d)]`, which is a valid interval only when
`max(a, c) <= min(b, d)`.

## Constraints

- `0 <= firstList.length, secondList.length <= 1000`
- `firstList.length + secondList.length >= 1`
- `0 <= start_i <= end_i <= 10^9`
- `end_i < start_{i+1}` (intervals within a list are disjoint and sorted)
- `0 <= start_j <= end_j <= 10^9`
- `end_j < start_{j+1}`

## Examples

### Example 1

```
Input:  firstList  = [[0,2],[5,10],[13,23],[24,25]]
        secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Explanation: [0,2] ∩ [1,5] = [1,2]; [5,10] ∩ [1,5] = [5,5]; [5,10] ∩ [8,12] = [8,10];
             [13,23] ∩ [15,24] = [15,23]; [24,25] ∩ [15,24] = [24,24];
             [24,25] ∩ [25,26] = [25,25].
```

### Example 2

```
Input:  firstList  = [[1,3],[5,9]]
        secondList = []
Output: []
Explanation: secondList is empty, so there is nothing to intersect with.
```

### Example 3

```
Input:  firstList  = [[1,7]]
        secondList = [[3,10]]
Output: [[3,7]]
Explanation: [1,7] ∩ [3,10] = [max(1,3), min(7,10)] = [3,7].
```

## Hint

Both lists are sorted by start, so use the **Two-Pointer Merge** technique. At each step
compute the overlap of the two current intervals; then advance the pointer of the
interval that **ends first**, since it can never overlap any later interval in the other
list.
