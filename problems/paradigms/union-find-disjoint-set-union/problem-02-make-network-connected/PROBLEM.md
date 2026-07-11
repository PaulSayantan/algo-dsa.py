# Number of Operations to Make Network Connected

**Difficulty:** Medium

**Source:** LeetCode 1319 — Number of Operations to Make Network Connected

## Description

There are `n` computers numbered from `0` to `n - 1` connected by ethernet cables `connections`
forming a network, where `connections[i] = [a, b]` represents a connection between computers `a`
and `b`. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network `connections`. You can extract certain cables between
two directly connected computers, and place them between any pair of disconnected computers to
make them directly connected.

Return the **minimum number of times** you need to do this in order to make all the computers
connected. If it is not possible, return `-1`.

## Constraints

- `1 <= n <= 10^5`
- `1 <= connections.length <= min(n * (n - 1) / 2, 10^5)`
- `connections[i].length == 2`
- `0 <= a_i, b_i < n`
- `a_i != b_i`
- There are no repeated connections.
- No two computers are connected by more than one cable.

## Examples

### Example 1

```
Input:  n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
```

Explanation: Computers `0`, `1`, `2` form one connected group and computer `3` is alone. Remove
the redundant cable `[1,2]` (the group stays connected) and use it to connect computer `3`. One
operation suffices.

### Example 2

```
Input:  n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
```

Explanation: There are two connected groups: `{0,1,2,3}` and the singletons `{4}`, `{5}` — three
groups total. We need `3 - 1 = 2` extra cables to join them. There are enough redundant cables
inside the first group (5 cables span 4 nodes, so 2 are spare), so the answer is `2`.

### Example 3

```
Input:  n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
```

Explanation: There are only `4` cables but connecting `6` computers into one network requires at
least `6 - 1 = 5` cables. It is impossible, so return `-1`.

## Hint

First check whether you even have enough cables (`edges >= n - 1`). Then count the connected
components with **Union-Find (Disjoint Set Union)** — the answer is `components - 1`.
