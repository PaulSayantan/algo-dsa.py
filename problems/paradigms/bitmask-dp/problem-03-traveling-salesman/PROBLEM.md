# Traveling Salesman — Minimum Cost Tour (Held-Karp)

**Difficulty:** Hard

**Source:** Classic (Held-Karp dynamic programming, 1962). Closely related to
LeetCode 943 (Find the Shortest Superstring) and LeetCode 847 (Shortest Path
Visiting All Nodes).

## Description

You are given `n` cities labeled `0` through `n - 1` and an `n x n` matrix
`dist`, where `dist[i][j]` is the cost of travelling directly from city `i` to
city `j`. Starting at city `0`, visit **every** city exactly once and return to
city `0`.

Return the **minimum possible total cost** of such a round trip (a Hamiltonian
cycle). You may assume a complete graph (every `dist[i][j]` is a finite
non-negative number, and `dist[i][i] = 0`).

## Constraints

- `1 <= n <= 15`
- `0 <= dist[i][j] <= 10^6`
- `dist[i][i] == 0`
- The matrix need not be symmetric (`dist[i][j]` may differ from `dist[j][i]`).

## Examples

### Example 1

```
Input: dist = [[0, 10, 15, 20],
               [10, 0, 35, 25],
               [15, 35, 0, 30],
               [20, 25, 30, 0]]
Output: 80
```

Explanation: The optimal tour is `0 -> 1 -> 3 -> 2 -> 0` with cost
`10 + 25 + 30 + 15 = 80`. No cyclic permutation of the four cities does better.

### Example 2

```
Input: dist = [[0, 1, 1],
               [1, 0, 1],
               [1, 1, 0]]
Output: 3
```

Explanation: With three mutually equidistant cities, any tour
(`0 -> 1 -> 2 -> 0`) costs `1 + 1 + 1 = 3`.

### Example 3

```
Input: dist = [[0]]
Output: 0
```

Explanation: A single city requires no travel; the tour cost is `0`.

## Hint

The exponential state you need is "which set of cities have I already visited,
and where am I standing now." Encode the visited set as an integer bitmask.
This is **Bitmask DP** — specifically the Held-Karp algorithm with state
`dp[mask][last]`.
