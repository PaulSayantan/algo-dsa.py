# Farthest Pair of Points (Diameter of a Point Set)

**Difficulty:** Easy

*Source: Classic computational-geometry problem (CLRS-style; a.k.a. "diameter of a
point set"). Appears on many judges, e.g. UVa 10065-style variants and competitive
"closest/farthest pair" sets.*

## Description

You are given `n` distinct points on the 2-D plane. The **diameter** of the set is the
largest Euclidean distance between any two of the points.

Return the value of that maximum distance. Because the naive answer often involves an
irrational square root, this problem asks you to return the **squared** distance, which
is always an integer when the inputs are integers (and avoids floating-point error).

Formally, return

```
max over all pairs (i, j) of  (x_i - x_j)^2 + (y_i - y_j)^2
```

The straightforward `O(n^2)` double loop is correct but too slow when `n` is large;
you should aim for a near-linear method after sorting.

## Constraints

- `2 <= n <= 100_000`
- `-10^9 <= x_i, y_i <= 10^9`
- All points are distinct.
- The answer fits in a 64-bit integer.

## Examples

### Example 1

```
Input:  points = [(0, 0), (0, 1), (1, 0), (1, 1)]
Output: 2
Explanation: The four corners of the unit square. The farthest pair is a diagonal,
             e.g. (0,0)-(1,1), whose squared distance is 1^2 + 1^2 = 2.
```

### Example 2

```
Input:  points = [(0, 0), (4, 0), (2, 3), (1, 1)]
Output: 16
Explanation: The two extreme points are (0,0) and (4,0); squared distance
             = 4^2 + 0^2 = 16. No other pair is farther apart.
```

## Hint

The farthest pair is always a pair of vertices on the **convex hull**, and the two
points realizing the diameter are an *antipodal pair*. Build the hull, then sweep a
pair of parallel supporting lines around it — the **Rotating Calipers on Point Grids**
technique — to enumerate only the antipodal pairs in linear time.
