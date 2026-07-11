# Remove Covered Intervals

**Difficulty:** Medium

**Source:** LeetCode 1288 — Remove Covered Intervals

## Description

You are given an array `intervals` where `intervals[i] = [l_i, r_i]` represents a
closed interval.

Interval `[a, b)` — informally, `[a, b]` — is **covered** by interval `[c, d]` if
and only if `c <= a` and `b <= d`. That is, `[a, b]` sits entirely inside
`[c, d]`.

Remove every interval that is covered by some **other** interval in the list, and
return the number of intervals that remain.

## Constraints

- `1 <= intervals.length <= 1000`
- `intervals[i].length == 2`
- `0 <= l_i <= r_i <= 10^5`
- All the given intervals are **unique** (no two intervals are identical).

## Examples

**Example 1**

```
Input:  intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: [3,6] is covered by [2,8] (2 <= 3 and 6 <= 8), so it is removed.
             [1,4] and [2,8] remain, giving 2.
```

**Example 2**

```
Input:  intervals = [[1,4],[2,3]]
Output: 1
Explanation: [2,3] is covered by [1,4] (1 <= 2 and 3 <= 4), so only [1,4] remains.
```

**Example 3**

```
Input:  intervals = [[1,2],[1,4],[3,4]]
Output: 1
Explanation: [1,2] is covered by [1,4], and [3,4] is covered by [1,4].
             Only [1,4] survives, giving 1.
```

## Hint

Sort with a twist so that a single sweep exposes coverage: order intervals by
start **ascending**, and break ties by end **descending**. Then, as in **Merge
Intervals**, walk left to right tracking the largest end seen so far — any
interval whose end does not exceed that running maximum is covered.
