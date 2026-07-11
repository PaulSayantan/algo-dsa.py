# Max Sum of Rectangle No Larger Than K

**Difficulty:** Hard

**Source:** LeetCode 363 — Max Sum of Rectangle No Larger Than K

## Description

Given an `m x n` matrix `matrix` and an integer `k`, return the maximum sum of a
rectangle in the matrix such that its sum is **no larger than `k`**.

It is guaranteed that there will be a rectangle with a sum no larger than `k`.

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-100 <= matrix[i][j] <= 100`
- `-10^5 <= k <= 10^5`

## Examples

### Example 1

```
Input: matrix = [[1, 0, 1],
                 [0, -2, 3]], k = 2
Output: 2
Explanation: The rectangle covering columns 1..2 and rows 0..1 is
[[0, 1], [-2, 3]] with sum 0 + 1 - 2 + 3 = 2, which is the largest sum
that is <= 2.
```

### Example 2

```
Input: matrix = [[2, 2, -1]], k = 3
Output: 3
Explanation: The rectangle [2, 2, -1] has sum 3, which equals k, so it is the
largest sum <= 3.
```

### Example 3

```
Input: matrix = [[5, -4, -3, 4],
                 [-3, -4, 4, 5],
                 [5, 1, 5, -4]], k = 8
Output: 8
Explanation: There is a rectangle whose sum is exactly 8 (for example rows 0..2
of column 2: -3 + 4 + 5 = 6, and other rectangles reach exactly 8), which is the
best value not exceeding k = 8.
```

## Hint

Fix a pair of columns and use a **2D Prefix Sum (Integral Image)** (or row
prefix sums) to collapse the band into a 1D array of row sums; then find the
maximum subarray sum `<= k` using a running prefix sum and a sorted set / binary
search.

## Follow-up

What if the number of rows is much larger than the number of columns? Fix the
pair over the **smaller** dimension so the inner 1D search runs over the larger
one.
