# Nearest Exit from Entrance in Maze

**Difficulty:** Medium

**Source:** LeetCode 1926 — Nearest Exit from Entrance in Maze

## Description

You are given an `m × n` matrix `maze` where each cell is `'.'` (empty) or `'+'` (wall), and a starting cell `entrance = [row, col]` that is empty. In one step you may move to an adjacent **4-directionally** empty cell (up/down/left/right) without leaving the maze.

An *exit* is any empty border cell **other than** `entrance` itself. Return the number of steps in the shortest path from `entrance` to the nearest exit, or `-1` if no exit is reachable.

Constraints: `1 <= m, n <= 100`; `maze[entrance[0]][entrance[1]] == '.'`.

## Examples

### Example 1

```
Input:  maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
```

**Explanation:** From `(1,2)` step up to the border cell `(0,2)`, which is an exit — 1 step.

### Example 2

```
Input:  maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
```

**Explanation:** `(1,0)` is a border cell but it is the entrance, so it does not count; the nearest exit is `(1,2)`, 2 steps away.

## Hint

Lee-algorithm BFS from `entrance`: the first time BFS dequeues a *border* empty cell that is not the entrance, its distance is the answer.
