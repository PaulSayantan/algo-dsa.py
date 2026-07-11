# Nearest Exit from Entrance in Maze

**Difficulty:** Medium

**Source:** LeetCode 1926 — Nearest Exit from Entrance in Maze

## Description

You are given an `m x n` matrix `maze` (0-indexed) with empty cells
(represented as `'.'`) and walls (represented as `'+'`). You are also given the
entrance of the maze, where `entrance = [entrancerow, entrancecol]` denotes the
row and column of the cell you start at.

In one step, you can move one cell **up, down, left, or right**. You cannot step
into a wall, and you cannot step outside the maze. Your goal is to find the
**nearest exit** from the entrance.

An **exit** is defined as an **empty cell that is at the border** of the maze.
The entrance itself does **not** count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest
exit, or `-1` if no such path exists.

## Constraints

- `maze.length == m`
- `maze[i].length == n`
- `1 <= m, n <= 100`
- `maze[i][j]` is either `'.'` or `'+'`.
- `entrance.length == 2`
- `0 <= entrancerow < m`
- `0 <= entrancecol < n`
- `entrance` will always be an empty cell.

## Examples

### Example 1

```
Input: maze = [["+","+",".","+"],
               [".",".",".","+"],
               ["+","+","+","."]], entrance = [1,2]
Output: 1
```

**Explanation:** There are 3 exits in this maze at `[1,0]`, `[0,2]`, and
`[2,3]`. Starting from `[1,2]`, you can reach `[0,2]` by moving 1 step up.
That is the closest border exit, so the answer is 1.

### Example 2

```
Input: maze = [["+","+","+"],
               [".",".","."],
               ["+","+","+"]], entrance = [1,0]
Output: 2
```

**Explanation:** The only exit is `[1,2]`. Although `[1,0]` is on the border, it
is the entrance and does not count. Moving right twice (`[1,1]` then `[1,2]`)
reaches the exit in 2 steps.

### Example 3

```
Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
```

**Explanation:** The only other cell `[0,1]` is a wall, and the entrance itself
cannot count as an exit, so there is no reachable exit.

## Hint

Model each empty cell as a graph node with edges to its 4 orthogonal neighbours,
then use the **Lee Algorithm** (BFS): the first border cell (other than the
entrance) you reach is guaranteed to be the nearest exit.
