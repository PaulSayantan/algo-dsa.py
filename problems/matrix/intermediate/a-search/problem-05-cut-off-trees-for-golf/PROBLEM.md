# Cut Off Trees for Golf Event

**Difficulty:** Hard

**Source:** LeetCode 675 — Cut Off Trees for Golf Event

## Description

You are asked to cut off all the trees in a forest for a golf event. The forest is
represented as an `m x n` matrix where each cell has one of three values:

- `0` — a blocked cell, cannot be walked through.
- `1` — an empty, walkable cell (ground).
- value `> 1` — a tree that can be walked through; the number is the tree's **height**.

You must cut the trees in order of **increasing height**. When you cut a tree, its cell
becomes an empty walkable cell (value `1`). You start at the top-left corner `(0, 0)`
and may move one step in any of the four cardinal directions to an adjacent walkable
cell (value `≥ 1`).

Return the **minimum total number of steps** to walk and cut off all the trees in
increasing-height order. If you cannot cut off all the trees, return `-1`. It is
guaranteed that no two trees have the same height and that there is at least one tree
to cut.

## Constraints

- `m == forest.length`
- `n == forest[i].length`
- `1 <= m, n <= 50`
- `0 <= forest[i][j] <= 10^9`
- Heights of all trees are **distinct**.

## Examples

### Example 1

```
Input: forest = [[1,2,3],
                 [0,0,4],
                 [7,6,5]]
Output: 6
```

**Explanation:** Cutting trees in height order `2,3,4,5,6,7` and walking the shortest
path between consecutive trees (following the spiral of walkable cells) costs `6` steps
in total.

### Example 2

```
Input: forest = [[1,2,3],
                 [0,0,0],
                 [7,6,5]]
Output: -1
```

**Explanation:** The row of `0`s completely separates the top row from the bottom row,
so after cutting `2` and `3` you can never reach the trees `5,6,7`; the task is
impossible.

### Example 3

```
Input: forest = [[2,3,4],
                 [0,0,5],
                 [8,7,6]]
Output: 6
```

**Explanation:** The start cell `(0,0)` holds the shortest tree (`2`), so it is cut
first with no walking. Cutting the rest in height order `3,4,5,6,7,8` along the walkable
spiral costs `6` steps in total.

## Hint

Sort the trees by height, then the problem becomes a chain of independent **point-to-point
shortest-path** queries: from your current position to the next tree. Solve each leg
with **A\* Search** on the grid using the **Manhattan distance** to that leg's target
tree as the heuristic, and sum the leg costs. If any leg is unreachable, return `-1`.
