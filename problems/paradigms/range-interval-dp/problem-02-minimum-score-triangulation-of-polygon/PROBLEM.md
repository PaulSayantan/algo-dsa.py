# Minimum Score Triangulation of Polygon

**Difficulty:** Medium

**Source:** LeetCode 1039 — Minimum Score Triangulation of Polygon

## Description

You have a convex polygon with `n` vertices, where the value of the `i`-th vertex
is `values[i]` (vertices are given in order, either clockwise or
counter-clockwise).

You will **triangulate** the polygon into `n - 2` triangles. For each triangle,
the value of that triangle is the **product of the values of its three
vertices**, and the **total score** of the triangulation is the **sum** of these
products over all `n - 2` triangles.

Return the **smallest possible total score** that you can achieve over all
possible triangulations of the polygon.

## Constraints

- `n == values.length`
- `3 <= n <= 50`
- `1 <= values[i] <= 100`

## Examples

### Example 1
```
Input:  values = [1, 2, 3]
Output: 6
Explanation: The polygon is already a single triangle. The score is
1 * 2 * 3 = 6.
```

### Example 2
```
Input:  values = [3, 7, 4, 5]
Output: 144
Explanation: There are two ways to triangulate the quadrilateral.
- Cut with diagonal (0,2): triangles (3,7,4) and (3,4,5) -> 84 + 60 = 144.
- Cut with diagonal (1,3): triangles (3,7,5) and (7,4,5) -> 105 + 140 = 245.
The minimum is 144.
```

### Example 3
```
Input:  values = [1, 3, 1, 4, 1, 5]
Output: 13
Explanation: An optimal triangulation gives a total score of 13, the minimum
over all ways to split the hexagon into 4 triangles.
```

## Hint

Think **Range / Interval DP**: let `dp[i][j]` be the best score to triangulate
the sub-polygon spanned by vertices `i..j`, and pick an apex vertex `k` that
forms a triangle with the fixed edge `(i, j)`.
