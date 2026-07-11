# Largest Uniform Square

**Difficulty:** Hard

*Source: Classic competitive-programming exercise (binary search + 2D range min/max).*

## Description

You are given an `n x m` integer matrix `grid` and an integer `D >= 0`. A square
submatrix is called **uniform (within tolerance D)** if the difference between
its largest and smallest value is at most `D`; that is, `max − min <= D`.

Return the side length `L` of the **largest** axis-aligned square submatrix that
is uniform within tolerance `D`. A single cell always qualifies (its spread is
`0`), so the answer is at least `1`.

## Constraints

- `1 <= n, m <= 500`
- `0 <= D <= 2 * 10^9`
- `-10^9 <= grid[i][j] <= 10^9`

## Examples

### Example 1

```
Input:
grid = [[1, 2, 3,  8],
        [2, 3, 4,  9],
        [3, 4, 5, 10],
        [9, 9, 9,  1]]
D = 2

Output: 2
```

Explanation: The `2 x 2` window at `(0,0)` covers `{1,2,2,3}`; spread `3-1 = 2 <= 2`,
so it qualifies. No `3 x 3` window is uniform: e.g. the top-left `3 x 3` window
spans values `1..5`, spread `4 > 2`. So the largest uniform square has side `2`.

### Example 2

```
Input:
grid = [[1, 2, 3,  8],
        [2, 3, 4,  9],
        [3, 4, 5, 10],
        [9, 9, 9,  1]]
D = 4

Output: 3
```

Explanation: The top-left `3 x 3` window covers values `1..5`; spread
`5 - 1 = 4 <= 4`, so a side-`3` square qualifies. No `4 x 4` square works (the
full grid spans `1..10`, spread `9 > 4`), so the answer is `3`.

## Hint

Feasibility is **monotonic** in the side length `L`: if some `L x L` square is
uniform, checking a *given* `L` needs only `max − min` over each `L x L` window.
Build **2D Sparse Tables** for `max` and `min`, then **binary search** on `L`,
testing all windows of a candidate size in O(1) each.
