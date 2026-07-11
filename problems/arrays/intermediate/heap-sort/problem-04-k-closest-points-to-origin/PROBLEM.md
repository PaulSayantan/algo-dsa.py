# K Closest Points to Origin

**Difficulty:** Medium

**Source:** LeetCode 973 — K Closest Points to Origin

## Description

You are given an array `points` where `points[i] = [xi, yi]` represents a point
on the X-Y plane, and an integer `k`. Return the `k` points **closest to the
origin** `(0, 0)`.

The distance between two points is the **Euclidean distance**
`sqrt((x1 - x2)^2 + (y1 - y2)^2)`.

You may return the answer in **any order**. The answer is **guaranteed to be
unique** (except for the order it is in).

## Constraints

- `1 <= k <= points.length <= 10^4`
- `-10^4 <= xi, yi <= 10^4`

## Examples

### Example 1

```
Input:  points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
```

**Explanation:** Squared distances are `1^2 + 3^2 = 10` for `[1,3]` and
`(-2)^2 + 2^2 = 8` for `[-2,2]`. Since `8 < 10`, `[-2,2]` is the single closest
point.

### Example 2

```
Input:  points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
```

**Explanation:** Squared distances are `[3,3] -> 18`, `[5,-1] -> 26`,
`[-2,4] -> 20`. The two smallest are `18` and `20`, so the answer is `[3,3]` and
`[-2,4]` (any order).

## Hint

Use a **heap keyed on distance**. Compare points by **squared** distance
`x*x + y*y` (no `sqrt` needed — it is monotonic and avoids floating point).
Maintain a **max-heap of size `k`**: push each point, and evict the farthest
whenever the heap exceeds `k`. The `k` points left are the closest.
