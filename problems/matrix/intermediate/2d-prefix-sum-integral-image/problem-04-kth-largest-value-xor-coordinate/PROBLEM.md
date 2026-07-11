# Find Kth Largest XOR Coordinate Value

**Difficulty:** Medium

**Source:** LeetCode 1738 — Find Kth Largest XOR Coordinate Value

## Description

You are given a 2D `matrix` of size `m x n` and an integer `k`.

The value of coordinate `(a, b)` of the matrix is the **XOR** of all
`matrix[i][j]` where `0 <= i <= a` and `0 <= j <= b` (0-indexed).

Find the `k`-th largest value (**1-indexed**) of all the coordinate values.
That is, among the `m * n` coordinate values, return the one that is the `k`-th
largest (duplicates count separately).

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 1000`
- `0 <= matrix[i][j] <= 10^6`
- `1 <= k <= m * n`

## Examples

### Example 1

```
Input: matrix = [[5, 2],
                 [1, 6]], k = 1
Output: 7
Explanation: The coordinate values are:
  value(0,0) = 5
  value(0,1) = 5 XOR 2 = 7
  value(1,0) = 5 XOR 1 = 4
  value(1,1) = 5 XOR 2 XOR 1 XOR 6 = 0
Sorted in descending order: [7, 5, 4, 0]. The 1st largest is 7.
```

### Example 2

```
Input: matrix = [[5, 2],
                 [1, 6]], k = 3
Output: 4
Explanation: The same coordinate values [7, 5, 4, 0] sorted descending are
[7, 5, 4, 0]; the 3rd largest is 4.
```

### Example 3

```
Input: matrix = [[5, 2],
                 [1, 6]], k = 4
Output: 0
Explanation: The 4th (smallest here) of [7, 5, 4, 0] is 0.
```

## Hint

This is a **2D Prefix Sum (Integral Image)** where the combining operation is
**XOR** instead of addition. Because XOR is its own inverse, the build
recurrence uses XOR in place of `+`/`-`. After computing every coordinate value,
select the k-th largest.
