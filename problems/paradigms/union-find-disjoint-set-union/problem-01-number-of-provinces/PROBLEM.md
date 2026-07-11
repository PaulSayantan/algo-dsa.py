# Number of Provinces

**Difficulty:** Medium

**Source:** LeetCode 547 — Number of Provinces (formerly "Friend Circles")

## Description

There are `n` cities. Some of them are connected, while some are not. If city `a` is connected
directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is
connected indirectly with city `c`.

A **province** is a group of directly or indirectly connected cities and no other cities outside
of the group.

You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the `i`-th city
and the `j`-th city are directly connected, and `isConnected[i][j] = 0` otherwise.

Return the total number of **provinces**.

## Constraints

- `1 <= n <= 200`
- `n == isConnected.length`
- `n == isConnected[i].length`
- `isConnected[i][j]` is `1` or `0`.
- `isConnected[i][i] == 1`
- `isConnected[i][j] == isConnected[j][i]` (the matrix is symmetric)

## Examples

### Example 1

```
Input:  isConnected = [[1,1,0],
                       [1,1,0],
                       [0,0,1]]
Output: 2
```

Explanation: Cities `0` and `1` are directly connected, so they form one province. City `2` is
connected to no one else, so it forms a second province. Total = 2.

### Example 2

```
Input:  isConnected = [[1,0,0],
                       [0,1,0],
                       [0,0,1]]
Output: 3
```

Explanation: No city is connected to any other city. Each of the three cities is its own
province, giving 3 provinces.

### Example 3

```
Input:  isConnected = [[1,1,0],
                       [1,1,1],
                       [0,1,1]]
Output: 1
```

Explanation: City `0`—city `1` are directly connected and city `1`—city `2` are directly
connected, so `0` and `2` are indirectly connected. All three cities collapse into a single
province.

## Hint

Model each city as an element and each `isConnected[i][j] == 1` as a merge. The number of
provinces is exactly the number of distinct groups that remain — a textbook use of
**Union-Find (Disjoint Set Union)**.
