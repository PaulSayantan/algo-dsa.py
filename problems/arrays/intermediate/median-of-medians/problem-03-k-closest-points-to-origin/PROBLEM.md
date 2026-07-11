# K Closest Points to Origin

**Difficulty:** Medium

Source: LeetCode 973 "K Closest Points to Origin".

## Description

Given an array `points` where `points[i] = [xi, yi]` represents a point on the
XY plane, and an integer `k`, return the `k` points that are **closest to the
origin** `(0, 0)`.

The distance between a point and the origin is the Euclidean distance
`sqrt(xi^2 + yi^2)`. Because comparing `sqrt(a)` and `sqrt(b)` is the same as
comparing `a` and `b` for non-negative values, you can rank points by the
**squared distance** `xi^2 + yi^2` and avoid floating point entirely.

You may return the `k` points **in any order**. The answer is guaranteed to be
unique **except for the order** that the points are returned in (ties in distance
are broken arbitrarily, so any valid set of `k` closest points is accepted).

Target complexity: **worst-case O(n)** average work using a deterministic
selection to find the distance threshold, rather than the O(n log n) full sort.

## Constraints

- `1 <= k <= points.length <= 10^4`
- `-10^4 <= xi, yi <= 10^4`

## Examples

### Example 1
```
Input:  points = [[1, 3], [-2, 2]], k = 1
Output: [[-2, 2]]
Explanation: Squared distances are 1^2 + 3^2 = 10 and (-2)^2 + 2^2 = 8.
Since 8 < 10, the point [-2, 2] is closer, so the single closest point is
[-2, 2].
```

### Example 2
```
Input:  points = [[3, 3], [5, -1], [-2, 4]], k = 2
Output: [[3, 3], [-2, 4]]
Explanation: Squared distances are 18, 26, and 20. The two smallest are 18 and
20, corresponding to [3, 3] and [-2, 4]. (Any order of these two is accepted.)
```

## Hint

Rank the points by squared distance and use **Median of Medians** selection to
find the k-th closest distance in worst-case linear time, then collect every
point at or under that threshold — no full sort required.
