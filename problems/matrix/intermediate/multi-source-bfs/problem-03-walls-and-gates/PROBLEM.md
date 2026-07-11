# Walls and Gates

**Difficulty:** Medium

**Source:** LeetCode 286 — Walls and Gates

## Description

You are given an `m x n` grid `rooms` initialized with these three possible values:

- `-1` — a **wall** or obstacle.
- `0` — a **gate**.
- `2147483647` (`INF`, i.e. `2^31 - 1`) — an **empty room**.

Fill each empty room with the distance to its **nearest gate**, measured as the number
of 4-directional steps. If it is impossible to reach a gate (blocked by walls), the
room should keep the value `INF`.

Modify the grid **in place**; you do not return anything.

## Constraints

- `m == rooms.length`
- `n == rooms[i].length`
- `1 <= m, n <= 250`
- `rooms[i][j]` is `-1`, `0`, or `2147483647`.

## Examples

### Example 1

```
Input:  rooms = [[INF, -1,  0, INF],
                 [INF, INF, INF, -1],
                 [INF, -1, INF, -1],
                 [  0, -1, INF, INF]]

Output:         [[  3, -1,  0,  1],
                 [  2,  2,  1, -1],
                 [  1, -1,  2, -1],
                 [  0, -1,  3,  4]]
```

**Explanation:** `INF` denotes `2147483647`. There are two gates, at `(0,2)` and
`(3,0)`. Each empty room is labeled with its distance to the closer gate; walls
(`-1`) stay untouched. For example, room `(0,0)` is 3 steps from the top gate (down,
down-ish paths around the wall), and room `(1,1)` is 2 steps from the top gate.

### Example 2

```
Input:  rooms = [[0, INF],
                 [INF, INF]]

Output:         [[0, 1],
                 [1, 2]]
```

**Explanation:** The single gate is at `(0,0)`. Its two neighbors `(0,1)` and `(1,0)`
are 1 step away, and `(1,1)` is 2 steps away (through either neighbor).

### Example 3

```
Input:  rooms = [[-1, INF],
                 [INF, -1]]

Output:         [[-1, INF],
                 [INF, -1]]
```

**Explanation:** There are no gates at all, so no empty room can reach one; every
`INF` stays `INF` and the walls are unchanged.

## Hint

Seed the queue with **every gate** (`0`) simultaneously and run a single
**Multi-Source BFS** outward, skipping walls. The first time an empty room is reached
gives its distance to the nearest gate; unreached rooms remain `INF`.
