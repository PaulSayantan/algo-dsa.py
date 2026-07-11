# As Far from Land as Possible

**Difficulty:** Medium

**Source:** LeetCode 1162 — As Far from Land as Possible

## Description

Given an `n x n` grid containing only values `0` and `1`, where `0` represents **water**
and `1` represents **land**, find a **water** cell such that its distance to the
**nearest land** cell is **maximized**, and return that maximum distance. If no land or
no water exists in the grid, return `-1`.

The distance used is the **Manhattan distance**: the distance between `(x0, y0)` and
`(x1, y1)` is `|x0 - x1| + |y0 - y1|`, which for 4-directional grid movement equals the
number of steps in a shortest path.

## Constraints

- `n == grid.length`
- `n == grid[i].length`
- `1 <= n <= 100`
- `grid[i][j]` is `0` or `1`.

## Examples

### Example 1

```
Input:  grid = [[1, 0, 1],
                [0, 0, 0],
                [1, 0, 1]]
Output: 2
```

**Explanation:** The center water cell `(1,1)` is distance 2 from every land cell in
the corners. No water cell is farther from land than that, so the answer is `2`.

### Example 2

```
Input:  grid = [[1, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
Output: 4
```

**Explanation:** The only land cell is at `(0,0)`. The farthest water cell is the
opposite corner `(2,2)`, whose distance to that land is `|2-0| + |2-0| = 4`.

### Example 3

```
Input:  grid = [[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]]
Output: -1
```

**Explanation:** There is no water cell at all, so there is nothing to measure a
distance from; the answer is `-1`. (The all-water grid is symmetric: no land means
`-1` as well.)

## Hint

Instead of measuring outward from each water cell, seed the queue with **all land
cells** and expand a single **Multi-Source BFS**. The last (deepest) BFS level reached
is the maximum nearest-land distance over all water cells.

## Related

This is the max-of-nearest-distances companion to *01 Matrix* and *Map of Highest
Peak*: the BFS is identical, but instead of returning the whole distance grid you
return the largest distance produced.
