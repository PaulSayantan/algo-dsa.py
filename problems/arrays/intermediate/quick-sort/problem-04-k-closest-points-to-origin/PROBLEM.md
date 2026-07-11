# K Closest Points to Origin

**Difficulty:** Medium

**Source:** LeetCode 973 — K Closest Points to Origin

## Description

Given an array `points` where `points[i] = [xi, yi]` represents a point on the X-Y
plane, and an integer `k`, return the `k` points that are closest to the origin
`(0, 0)`.

The distance between two points on the X-Y plane is the Euclidean distance
`sqrt((x1 - x2)^2 + (y1 - y2)^2)`. To rank points you can compare **squared** distances
`x^2 + y^2` and skip the square root entirely (it is monotonic and cheaper).

You may return the answer in **any order**. The answer is guaranteed to be unique
(except for the order that it is in).

Sorting all points by distance is O(n log n), but you only need the closest `k`, not a
full ordering — so partition the points by squared distance with **Quickselect** and
return the first `k` in average O(n) time.

## Constraints

- `1 <= k <= points.length <= 10^4`
- `-10^4 <= xi, yi <= 10^4`

## Examples

### Example 1

```
Input:  points = [[1, 3], [-2, 2]], k = 1
Output: [[-2, 2]]
Explanation: Squared distances are 1^2 + 3^2 = 10 and (-2)^2 + 2^2 = 8.
Since 8 < 10, the closest single point is [-2, 2].
```

### Example 2

```
Input:  points = [[3, 3], [5, -1], [-2, 4]], k = 2
Output: [[3, 3], [-2, 4]]
Explanation: Squared distances are 18, 26, and 20. The two smallest are 18 ([3, 3])
and 20 ([-2, 4]). (Any order of these two is accepted.)
```

### Example 3

```
Input:  points = [[0, 1], [1, 0]], k = 2
Output: [[0, 1], [1, 0]]
Explanation: Both points have squared distance 1, and k equals the number of points,
so all points are returned.
```

## Hint

Use **Quickselect** on the squared distance `x^2 + y^2` as the key. Partition so the
`k` smallest-distance points occupy the first `k` slots of the array; you never need
those `k` to be internally sorted, so recurse into only the side containing index `k`.
