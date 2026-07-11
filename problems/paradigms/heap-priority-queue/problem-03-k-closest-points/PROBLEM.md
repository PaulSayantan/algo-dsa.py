# K Closest Points to Origin

**Difficulty:** Medium

**Source:** LeetCode 973 (K Closest Points to Origin)

## Description

Given an array `points` where `points[i] = [xi, yi]` represents a point on the X-Y
plane, and an integer `k`, return the `k` closest points to the origin `(0, 0)`.

The distance between two points on the plane is the Euclidean distance:
`sqrt((x1 - x2)^2 + (y1 - y2)^2)`.

You may return the answer in **any order**. The answer is guaranteed to be **unique**
(except for the order in which it is returned).

## Constraints

- `1 <= k <= points.length <= 10^4`
- `-10^4 <= xi, yi <= 10^4`

## Examples

### Example 1

```
Input:  points = [[1, 3], [-2, 2]], k = 1
Output: [[-2, 2]]
```

Explanation: The squared distance of `[1, 3]` is `1 + 9 = 10`; of `[-2, 2]` is
`4 + 4 = 8`. Since `8 < 10`, the point `[-2, 2]` is closer, so with `k = 1` the answer
is `[[-2, 2]]`.

### Example 2

```
Input:  points = [[3, 3], [5, -1], [-2, 4]], k = 2
Output: [[3, 3], [-2, 4]]
```

Explanation: Squared distances are `[3,3] -> 18`, `[5,-1] -> 26`, `[-2,4] -> 20`. The
two smallest are `18` and `20`, so the two closest points are `[3, 3]` and `[-2, 4]`
(returned in any order).

## Hint

Use a **Heap / Priority Queue**. Keep a **max-heap of size `k`** keyed on (squared)
distance: the farthest of your current best `k` sits at the root, so a closer newcomer
can evict it in `O(log k)`. Compare **squared** distances — no need for the square root.
