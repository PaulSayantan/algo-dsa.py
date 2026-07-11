# Number of Islands II

**Difficulty:** Hard

**Source:** LeetCode 305 — Number of Islands II (premium)

## Description

You are given an empty 2D binary grid `grid` of size `m x n`. The grid represents a map where
`0`s represent water and `1`s represent land. Initially, all the cells of `grid` are water cells
(i.e., all the cells are `0`s).

We may perform an **add land** operation which turns the water at position `[r, c]` into a land
cell. You are given an array `positions` where `positions[i] = [r_i, c_i]` is the position
`(r_i, c_i)` at which we should operate the `i`-th operation.

Return an array of integers `answer` where `answer[i]` is the **number of islands** after turning
the cell `(r_i, c_i)` into land.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or
vertically. You may assume all four edges of the grid are all surrounded by water.

## Constraints

- `1 <= m, n, positions.length <= 10^4`
- `1 <= m * n <= 10^4`
- `positions[i].length == 2`
- `0 <= r_i < m`
- `0 <= c_i < n`
- A position may be repeated (adding land where land already exists is a no-op for the count).

## Examples

### Example 1

```
Input:  m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
Output: [1,1,2,3]
```

Explanation:
- Add `(0,0)`: one island → `1`.
- Add `(0,1)`: adjacent to `(0,0)`, so they merge into one island → `1`.
- Add `(1,2)`: isolated, a new island → `2`.
- Add `(2,1)`: touches none of the existing land, a third island → `3`.

### Example 2

```
Input:  m = 2, n = 2, positions = [[0,0],[1,1],[0,1]]
Output: [1,2,1]
```

Explanation:
- Add `(0,0)`: one island → `1`.
- Add `(1,1)`: not adjacent to `(0,0)` (diagonal does not count) → `2`.
- Add `(0,1)`: adjacent to both `(0,0)` and `(1,1)`, bridging the two islands into one → `1`.

### Example 3

```
Input:  m = 1, n = 1, positions = [[0,0]]
Output: [1]
```

Explanation: The single cell becomes land, forming exactly one island → `1`.

## Hint

Add cells one at a time. Each new land cell starts as its own island (`count += 1`), then union
it with any already-land orthogonal neighbor, decrementing the count on each real merge — an
online application of **Union-Find (Disjoint Set Union)**.
