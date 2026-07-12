# Walls and Gates

**Difficulty:** Medium

**Source:** LeetCode 286 — Walls and Gates

## Description

You are given an `m x n` grid `rooms` where each cell is one of:

- `-1` — a wall or obstacle.
- `0` — a gate.
- `2147483647` (`INF`) — an empty room.

Fill each empty room with the distance to its *nearest* gate, measured in 4-directional steps. If a room cannot reach any gate, leave it as `2147483647`. Return the modified grid.

Constraints: `1 <= m, n <= 250`; each cell is `-1`, `0`, or `2147483647`.

## Examples

### Example 1

```
Input:  rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
```

**Explanation:** Every empty room is labeled with the number of steps to the closest gate; walls (`-1`) and gates (`0`) are unchanged.

## Hint

Seed the queue with *every* gate at distance 0 and BFS outward together — the first time a room is reached is its nearest-gate distance.
