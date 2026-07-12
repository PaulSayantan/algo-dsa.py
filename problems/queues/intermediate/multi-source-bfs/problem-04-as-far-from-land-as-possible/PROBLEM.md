# As Far from Land as Possible

**Difficulty:** Medium

**Source:** LeetCode 1162 — As Far from Land as Possible

## Description

Given an `n x n` grid where `1` marks land and `0` marks water, find the water cell whose distance to the *nearest* land cell is maximized, and return that distance. Distance is Manhattan distance measured in 4-directional steps.

If the grid contains no water or no land, return `-1`.

Constraints: `1 <= n <= 100`; each cell is `0` or `1`.

## Examples

### Example 1

```
Input:  grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
```

**Explanation:** The center cell `(1, 1)` is 2 steps from the nearest land, which is the maximum over all water cells.

## Hint

Seed the queue with *all* land cells at distance 0; the distance of the last water cell filled by the joint BFS is the answer.
