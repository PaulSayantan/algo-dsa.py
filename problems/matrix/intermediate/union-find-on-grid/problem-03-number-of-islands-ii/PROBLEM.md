# Number of Islands II

**Difficulty:** Hard

**Source:** LeetCode 305 (Number of Islands II)

## Description

You are given an empty `m x n` grid where every cell starts as water (`0`). You are also given
an array `positions` where `positions[i] = [ri, ci]` is the cell that is turned into land
(`1`) during the `i`-th operation (this is called an **addLand** operation).

Return an array `result` where `result[i]` is the number of islands **after** performing the
`i`-th `addLand` operation. As before, an island is a maximal group of land cells connected
4-directionally, and the grid is surrounded by water.

Adding land at a cell that is already land is a no-op: the island count does not change for
that step.

## Constraints

- `1 <= m, n, m * n <= 10^4`
- `1 <= positions.length <= 10^4`
- `positions[i].length == 2`
- `0 <= ri < m`
- `0 <= ci < n`

## Examples

### Example 1

```
Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
Output: [1, 1, 2, 3]
```

**Explanation:**
- Add (0,0): one island → `1`.
- Add (0,1): it touches (0,0), so they merge into one island → `1`.
- Add (1,2): isolated, a new island → `2`.
- Add (2,1): isolated (no 4-dir land neighbor yet) → `3`.

### Example 2

```
Input: m = 1, n = 1, positions = [[0,0]]
Output: [1]
```

**Explanation:** A single land cell in a 1x1 grid is one island.

### Example 3

```
Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[1,2]]
Output: [1, 1, 2, 2]
```

**Explanation:** The last operation adds land at (1,2), which is already land, so the count
stays at `2` (duplicate addLand is a no-op).

## Hint

Cells appear **online**, one at a time — re-scanning the whole grid per step is wasteful. Keep
a running island count with **Union–Find on Grid**: activating a cell adds one, and each merge
with an already-active neighbor subtracts one.
