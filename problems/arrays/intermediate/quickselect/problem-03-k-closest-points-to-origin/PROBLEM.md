# K Closest Points to Origin

**Difficulty:** Medium

**Source:** LeetCode 973 — K Closest Points to Origin

## Description

Given an array `points` where `points[i] = [xi, yi]` represents a point on the X-Y
plane, and an integer `k`, return the **k closest points to the origin** `(0, 0)`.

The distance between two points on the plane is the Euclidean distance,
`sqrt((x1 - x2)^2 + (y1 - y2)^2)`. Since we compare against the origin, the distance of
a point `(x, y)` simplifies to `sqrt(x^2 + y^2)`.

You may return the answer in **any order**. The answer is guaranteed to be **unique**
(except for the order that it is in).

## Constraints

- `1 <= k <= points.length <= 10^4`
- `-10^4 <= xi, yi <= 10^4`

## Examples

### Example 1

```
Input:  points = [[1, 3], [-2, 2]], k = 1
Output: [[-2, 2]]
```

**Explanation:** The squared distances are `1^2 + 3^2 = 10` for `[1, 3]` and
`(-2)^2 + 2^2 = 8` for `[-2, 2]`. Since `8 < 10`, `[-2, 2]` is closer, so with `k = 1`
we return `[[-2, 2]]`.

### Example 2

```
Input:  points = [[3, 3], [5, -1], [-2, 4]], k = 2
Output: [[3, 3], [-2, 4]]
```

**Explanation:** Squared distances are `18` for `[3, 3]`, `26` for `[5, -1]`, and `20`
for `[-2, 4]`. The two smallest are `18` and `20`, so we return `[[3, 3], [-2, 4]]`
(any order is accepted).

## Hint

You do not need the k closest points *sorted* — only the set of them. Use **Quickselect**
on the points, comparing by **squared** distance (no need for `sqrt`), to partition the k
nearest into the first `k` slots in expected `O(n)`, then return that prefix.
