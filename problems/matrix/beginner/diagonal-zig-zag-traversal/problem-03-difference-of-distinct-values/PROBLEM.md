# Difference of Number of Distinct Values on Diagonals

**Difficulty:** Medium

**Source:** LeetCode 2711 — "Difference of Number of Distinct Values on Diagonals"

## Description

Given a 2D `grid` of size `m x n`, you should find a matrix `answer` of size
`m x n`.

For each cell `(r, c)`, look along its **main diagonal** (the `\` direction, where
`i - j` is constant):

- `topLeft[r][c]` = the number of **distinct** values strictly above-left of
  `(r, c)` on that diagonal, i.e. among cells `(r-1, c-1), (r-2, c-2), ...`.
- `bottomRight[r][c]` = the number of **distinct** values strictly below-right of
  `(r, c)` on that diagonal, i.e. among cells `(r+1, c+1), (r+2, c+2), ...`.

Then `answer[r][c] = |topLeft[r][c] - bottomRight[r][c]|`.

Return the matrix `answer`.

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `1 <= grid[i][j] <= 100`

## Examples

### Example 1

```
Input:  grid = [[1,2,3],
                [3,1,5],
                [3,2,1]]
Output: [[1,1,0],
         [1,0,1],
         [0,1,1]]
```

**Explanation:** Take cell `(0,0)=1`. Above-left there is nothing, so `topLeft=0`.
Below-right along the `\` diagonal are `grid[1][1]=1` and `grid[2][2]=1`, whose
distinct values are `{1}`, so `bottomRight=1`. Thus `answer[0][0]=|0-1|=1`. Applying
the same reasoning to every cell yields the matrix above.

### Example 2

```
Input:  grid = [[1]]
Output: [[0]]
```

**Explanation:** The only cell has nothing above-left and nothing below-right, so
both counts are `0` and the difference is `0`.

### Example 3

```
Input:  grid = [[5,5],
                [5,5]]
Output: [[1,0],
         [0,1]]
```

**Explanation:** For `(0,0)`, below-right is `grid[1][1]=5`, giving distinct set
`{5}` (count 1) versus nothing above-left (count 0) -> `|0-1|=1`. Cells `(0,1)` and
`(1,0)` are each alone on their diagonals, giving `0`. For `(1,1)`, above-left is
`grid[0][0]=5` (count 1) versus nothing below-right (count 0) -> `1`.

## Hint

Use **Diagonal / Zig-Zag Traversal**: cells on one `\` diagonal share the constant
`i - j`. From each cell, walk up-left and down-right along that diagonal collecting
distinct values.
