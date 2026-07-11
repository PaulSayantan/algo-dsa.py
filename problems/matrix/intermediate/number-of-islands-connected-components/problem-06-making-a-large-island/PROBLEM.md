# Making A Large Island

**Difficulty:** Hard

**Source:** LeetCode 827 (Making A Large Island)

## Description

You are given an `n x n` binary matrix `grid`. You are allowed to change **at
most one** `0` to be `1`.

Return the size of the largest island in `grid` after applying this operation.
An **island** is a 4-directionally connected group of `1`s. (If the grid is
already all `1`s, no flip is possible and the answer is the size of the whole
grid.)

## Constraints

- `n == grid.length == grid[i].length`
- `1 <= n <= 500`
- `grid[i][j]` is `0` or `1`.

## Examples

### Example 1

```
Input: grid = [[1,0],
               [0,1]]
Output: 3
```

**Explanation:** Change the `0` at `(0,1)` to `1`. It now touches the island at
`(0,0)` (to its left) and the island at `(1,1)` (below it), merging them into a
single island of size `1 + 1 + 1 = 3`.

### Example 2

```
Input: grid = [[1,1],
               [1,0]]
Output: 4
```

**Explanation:** The three `1`s already form one island of size `3`. Change the
`0` at `(1,1)` to `1`; it connects to that island, growing it to size `4`
(the whole grid).

### Example 3

```
Input: grid = [[1,1],
               [1,1]]
Output: 4
```

**Explanation:** There are no `0`s to flip, so the grid is untouched. The single
island already spans all `4` cells.

## Hint

Two-phase **Connected Components**: first label every island with a unique id
and record each island's size. Then for each `0`, imagine flipping it and sum
the sizes of the **distinct** island ids among its 4 neighbours (plus `1` for
the flipped cell itself). Take the maximum.
