# Best Position for a Service Centre

**Difficulty:** Hard

**Source:** LeetCode 1515 — Best Position for a Service Centre

## Description

A delivery company wants to build a new service centre. Given the integer coordinates
`positions[i] = [x_i, y_i]` of `n` customers on the plane, choose a location `(x, y)`
that **minimizes the sum of Euclidean distances** to all customers:

```
cost(x, y) = sum over i of sqrt((x - x_i)^2 + (y - y_i)^2)
```

Return that minimum total distance. This optimal point is the **geometric median**
(a.k.a. the Weber point); unlike the centroid, it has no simple closed form for `n > 2`.

The cost function is **convex** in `(x, y)` (each term is a convex distance function,
and a sum of convex functions is convex). A convex function of one variable is
unimodal, which lets us nest two ternary searches: an outer search over `x`, and for
each fixed `x`, an inner search over `y`. Answers within `1e-5` of the true value are
accepted.

## Constraints

- `1 <= positions.length <= 50`
- `positions[i].length == 2`
- `0 <= x_i, y_i <= 100`
- The answer is a real number; tolerance `1e-5`.

## Examples

### Example 1

```
Input:  positions = [[0, 1], [1, 0], [1, 2], [2, 1]]
Output: 4.00000
```

Explanation: The four points form a diamond centred at `(1, 1)`. Placing the centre at
`(1, 1)` gives distance `1` to each of the four points, for a total of `4`. No other
point does better.

### Example 2

```
Input:  positions = [[1, 1], [3, 3]]
Output: 2.82843
```

Explanation: With only two points, any location on the segment between them yields a
total distance equal to the distance between the two points, `sqrt((3-1)^2 + (3-1)^2)
= sqrt(8) ≈ 2.82843`.

### Example 3

```
Input:  positions = [[1, 1]]
Output: 0.00000
```

Explanation: With a single customer, build the centre right on top of it; the total
distance is `0`.

## Hint

The cost is a convex function of `(x, y)`, so it is unimodal along each axis. Use a
**nested Ternary Search**: ternary-search `x`, and inside evaluate each candidate `x`
by ternary-searching the best `y` for it. The inner search returns the value used to
compare `x` probes.
