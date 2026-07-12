# Minimum Turns to Cross a Maze

**Difficulty:** Medium

**Source:** Classic — minimum-turn path in a grid (0-1 BFS)

## Description

You are given an `m x n` `grid` where `0` is an open cell and `1` is a wall. Starting at the top-left cell `(0, 0)`, you may move up, down, left, or right through open cells. Continuing straight in the direction you were already heading is free; **changing direction counts as one turn**. Return the **minimum number of turns** needed to reach the bottom-right cell `(m-1, n-1)`, or `-1` if it is unreachable (or if either the start or the goal is a wall).

Model the state as `(row, col, incoming_direction)`: moving one step in the same direction is a weight-0 edge, and moving in a different direction is a weight-1 edge (a turn). Run 0-1 BFS over these states.

## Examples

### Example 1

```
Input:  grid = [[0,0,0],[0,0,0],[0,0,0]]
Output: 1
```

**Explanation:** Go straight right along the top row, then turn once and go straight down the last column — one turn total.

### Example 2

```
Input:  grid = [[0,1],[1,0]]
Output: -1
```

**Explanation:** The walls disconnect the corner, so the goal is unreachable.

## Hint

State is `(row, col, direction)`; keep going in the same direction for weight 0 (appendleft) and turn to a new direction for weight 1 (append). Run 0-1 BFS.
