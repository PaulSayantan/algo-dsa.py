# Number of Provinces

**Difficulty:** Medium

**Source:** LeetCode 547 (Number of Provinces) — formerly "Friend Circles"

## Description

There are `n` cities. Some of them are connected, while some are not. If city
`a` is connected directly with city `b`, and city `b` is connected directly
with city `c`, then city `a` is connected indirectly with city `c`.

A **province** is a group of directly or indirectly connected cities, with no
other cities outside of the group.

You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if
the `i`-th city and the `j`-th city are directly connected, and
`isConnected[i][j] = 0` otherwise.

Return the total number of provinces.

## Constraints

- `1 <= n <= 200`
- `n == isConnected.length == isConnected[i].length`
- `isConnected[i][j]` is `1` or `0`.
- `isConnected[i][i] == 1` (every city is connected to itself).
- `isConnected[i][j] == isConnected[j][i]` (the relation is symmetric).

## Examples

### Example 1

```
Input: isConnected = [[1,1,0],
                      [1,1,0],
                      [0,0,1]]
Output: 2
```

**Explanation:** City `0` and city `1` are directly connected, forming one
province. City `2` is connected to no one else, forming a second province. So
there are `2` provinces.

### Example 2

```
Input: isConnected = [[1,0,0],
                      [0,1,0],
                      [0,0,1]]
Output: 3
```

**Explanation:** No two distinct cities are connected, so each city is its own
province: `3` in total.

### Example 3

```
Input: isConnected = [[1,1,0,0],
                      [1,1,1,0],
                      [0,1,1,0],
                      [0,0,0,1]]
Output: 2
```

**Explanation:** Cities `0`, `1`, and `2` are linked (0-1 directly, 1-2
directly, so 0-2 indirectly) into one province. City `3` stands alone as a
second province.

## Hint

This is **Connected Components** where the input is an *adjacency matrix* rather
than a grid. Traverse the implicit graph with DFS/BFS, or union every connected
pair with **Union-Find** and count the distinct roots.
