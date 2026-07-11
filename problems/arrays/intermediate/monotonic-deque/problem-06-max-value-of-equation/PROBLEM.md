# Max Value of Equation

**Difficulty:** Hard

**Source:** LeetCode 1499 — Max Value of Equation

## Description

You are given an array `points` containing the coordinates of points on a 2D
plane, sorted by the x-values in **strictly increasing** order, where
`points[i] = [x_i, y_i]`. You are also given an integer `k`.

Return the **maximum value** of the equation

```
y_i + y_j + |x_i - x_j|
```

over all pairs of points `(i, j)` such that `|x_i - x_j| <= k` and `1 <= i < j`
(0-indexed: `i < j`). It is guaranteed that at least one valid pair exists.

Because the points are sorted by x and we require `i < j`, we have `x_i < x_j`,
so `|x_i - x_j| = x_j - x_i`. The quantity to maximize becomes
`(y_j + x_j) + (y_i - x_i)`.

## Constraints

- `2 <= points.length <= 10^5`
- `points[i].length == 2`
- `-10^8 <= x_i, y_i <= 10^8`
- `0 <= k <= 2 * 10^8`
- `x_i < x_j` for all `i < j` (strictly increasing x-values)

## Examples

### Example 1

```
Input:  points = [[1, 3], [2, 0], [5, 10], [6, -10]], k = 1
Output: 4
```

**Explanation:** The only pairs with `|x_i - x_j| <= 1` are `([1,3],[2,0])`
(gap `1`) and `([5,10],[6,-10])` (gap `1`). Their equation values are
`3 + 0 + 1 = 4` and `10 + (-10) + 1 = 1`. The maximum is `4`.

### Example 2

```
Input:  points = [[0, 0], [3, 0], [9, 2]], k = 3
Output: 3
```

**Explanation:** Only the pair `([0,0],[3,0])` has an x-gap `<= 3` (gap `3`); its
value is `0 + 0 + 3 = 3`. The pair `([3,0],[9,2])` has gap `6 > 3`, and
`([0,0],[9,2])` has gap `9 > 3`, so both are invalid. The answer is `3`.

## Hint

For a fixed right point `j`, the term `y_j + x_j` is constant, so you want to
maximize `y_i - x_i` over earlier points `i` with `x_j - x_i <= k`. That is a
sliding-window maximum of `y_i - x_i` — maintain it with a **Monotonic Deque**.
