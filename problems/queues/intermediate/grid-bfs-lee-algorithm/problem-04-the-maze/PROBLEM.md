# The Maze

**Difficulty:** Medium

**Source:** LeetCode 490 — The Maze

## Description

A ball is placed in an `m × n` `maze` of empty spaces (`0`) and walls (`1`). The ball can roll **up, down, left, or right**, but once it starts rolling it does not stop until it hits a wall; only then can it pick a new direction.

Given `maze`, `start = [row, col]`, and `destination = [row, col]`, return `True` if the ball can stop at `destination`, else `False`. The borders act as walls, and both `start` and `destination` are empty cells.

Constraints: `1 <= m, n <= 100`; the ball must **stop** exactly on `destination`.

## Examples

### Example 1

```
Input:  maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
Output: True
```

**Explanation:** One rolling sequence is left, down, left, down, right, down, right, stopping exactly at `(4,4)`.

### Example 2

```
Input:  maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]
Output: False
```

**Explanation:** `(3,2)` sits mid-corridor; the ball always rolls past it and cannot come to rest there.

## Hint

BFS where each graph edge is a full *roll* — from a cell, slide in a direction until a wall stops you, then enqueue that stopping cell. It is Lee BFS on stopping-points rather than single steps.
