# Making a Large Island

**Difficulty:** Hard

**Source:** LeetCode 827 (Making a Large Island)

## Description

You are given an `n x n` binary matrix `grid`. You are allowed to change **at most one** `0` to
a `1`.

Return the size of the **largest island** in `grid` after applying this operation. An island is
a maximal group of `1`s connected 4-directionally. If the grid is already all `1`s, no flip is
needed and you return `n * n`.

## Constraints

- `n == grid.length == grid[i].length`
- `1 <= n <= 500`
- `grid[i][j]` is `0` or `1`.

## Examples

### Example 1

```
Input: grid = [[1,0],[0,1]]
Output: 3
```

**Explanation:** Flip one `0` to `1`. Flipping (0,1) joins the island at (0,0) with the island
at (1,1), giving a connected island of size 3. (Any single flip here yields 3.)

### Example 2

```
Input: grid = [[1,1],[1,0]]
Output: 4
```

**Explanation:** Flip the single `0` at (1,1) to `1`; the whole grid becomes one island of
size 4.

### Example 3

```
Input: grid = [[1,1],[1,1]]
Output: 4
```

**Explanation:** There is no `0` to flip. The grid is already a single island of size 4.

## Hint

First label every existing island and record its size with **Union–Find on Grid**. Then for
each `0`, imagine flipping it and sum the sizes of the **distinct** island roots among its four
neighbors (plus one for the flipped cell). Take the maximum.
