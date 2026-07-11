# Max Sum of Rectangle No Larger Than K

**Difficulty:** Hard

**Source:** LeetCode 363 — Max Sum of Rectangle No Larger Than K

## Description

Given an `m × n` matrix `matrix` and an integer `k`, return the maximum sum of a
non-empty rectangle in the matrix such that its sum is **no larger than `k`**.

It is guaranteed that there will be a rectangle with a sum no larger than `k`.

In other words, among all rectangular submatrices whose sum is `<= k`, return
the largest such sum. Note that the globally maximum rectangle might exceed `k`,
in which case you must settle for the best rectangle that stays within the cap.

This is Kadane 2D with a constrained 1D subroutine: instead of "largest
subarray sum" you need "largest subarray sum not exceeding `k`," which is solved
with sorted prefix sums and binary search rather than plain Kadane.

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-100 <= matrix[i][j] <= 100`
- `-10^5 <= k <= 10^5`

## Examples

### Example 1

```
Input:  matrix = [[1, 0, 1], [0, -2, 3]], k = 2
Output: 2
```

**Explanation:** The rectangle covering columns 0..1 of both rows is
`[[1, 0], [0, -2]]` with sum `-1`; the best rectangle whose sum is `<= 2` is the
rectangle `[[0, 1], [-2, 3]]` (columns 1..2, both rows) with sum
`0 + 1 - 2 + 3 = 2`. No rectangle with sum `<= 2` beats `2`.

### Example 2

```
Input:  matrix = [[2, 2, -1]], k = 3
Output: 3
```

**Explanation:** The full row sums to `2 + 2 - 1 = 3`, which is exactly `k`. The
unconstrained best would be `[2, 2] = 4`, but `4 > 3` is not allowed, so the
answer is `3`.

### Example 3

```
Input:  matrix = [[1, 2, -1], [-3, 4, 2], [1, -1, 5]], k = 8
Output: 8
```

**Explanation:** The unconstrained maximum rectangle here sums to `11`, but that
exceeds `k = 8`. The best rectangle with sum `<= 8` achieves exactly `8`, so the
answer is `8`.

## Hint

Use **Kadane 2D (max sum submatrix)** — fix the row band and compress columns as
usual, but replace 1D Kadane with a search over sorted prefix sums: for each
prefix `pre`, find the smallest earlier prefix `>= pre - k` to get the best
window sum not exceeding `k`.
