# Rotting Oranges

**Difficulty:** Medium

**Source:** LeetCode 994 — Rotting Oranges

## Description

In a grid, `0` is empty, `1` is a fresh orange, `2` is rotten. Every minute, a rotten orange rots its 4-directional fresh neighbors. Return the minutes until no fresh orange remains, or `-1` if impossible.

## Examples

### Example 1

```
Input:  grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```

## Hint

Seed the queue with all rotten oranges; BFS in waves, counting minutes; check for leftover fresh.
