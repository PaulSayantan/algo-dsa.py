# Campus Bikes II

**Difficulty:** Medium

**Source:** LeetCode 1066 — "Campus Bikes II".

## Description

On a campus represented as a 2D grid, there are `n` workers and `m` bikes, with
`n <= m`. Each worker and each bike is a point `[x, y]` on the grid.

Assign a bike to each worker. Among the available bikes and workers, we want to
choose an assignment where **each worker gets exactly one distinct bike** so that
the **sum of the Manhattan distances** between each worker and their assigned
bike is **minimized**.

The Manhattan distance between `p1 = [x1, y1]` and `p2 = [x2, y2]` is
`|x1 - x2| + |y1 - y2|`.

Return the **minimum possible sum of Manhattan distances** over all such
assignments.

## Constraints

- `1 <= n <= m <= 10`
- `workers[i].length == bikes[j].length == 2`
- `0 <= workers[i][k], bikes[j][k] < 1000`
- All worker and bike positions are given as integer coordinates.

## Examples

### Example 1

```
Input:  workers = [[0,0],[2,1]]
        bikes   = [[1,2],[3,3]]
Output: 6
Explanation: Assign worker 0 -> bike 0 (distance |0-1| + |0-2| = 3) and worker 1
-> bike 1 (distance |2-3| + |1-3| = 3). Total = 3 + 3 = 6. The other assignment
(worker 0 -> bike 1, worker 1 -> bike 0) costs 5 + 2 = 7, so 6 is the minimum.
```

### Example 2

```
Input:  workers = [[0,0],[1,1],[2,0]]
        bikes   = [[1,0],[2,2],[2,1]]
Output: 4
Explanation: Worker 0 -> bike 0 (distance 1), worker 1 -> bike 2 (distance 1),
worker 2 -> bike 1 (distance 2). Total = 1 + 1 + 2 = 4, which is optimal.
```

### Example 3

```
Input:  workers = [[0,0]]
        bikes   = [[3,4],[1,1]]
Output: 2
Explanation: There is one worker and two bikes. Bike 0 is at distance 7 and
bike 1 is at distance 2, so assigning the single worker to bike 1 gives the
minimum total distance of 2.
```

## Hint

Build a cost matrix `cost[i][j]` = Manhattan distance from worker `i` to bike
`j`. Because there may be more bikes than workers (`n <= m`), the matrix is
rectangular — pad it to a square with dummy zero-cost columns (or use a
Hungarian implementation that natively handles `n <= m`). Then run the
**Hungarian Algorithm** to minimize total distance.
