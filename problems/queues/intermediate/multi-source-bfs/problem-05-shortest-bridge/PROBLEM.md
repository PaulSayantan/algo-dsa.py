# Shortest Bridge

**Difficulty:** Medium

**Source:** LeetCode 934 — Shortest Bridge

## Description

You are given an `n x n` binary grid where `1` is land and `0` is water. There are exactly **two** islands (maximal 4-directionally connected groups of `1`s).

You may flip `0`s to `1`s to connect the two islands into one. Return the *smallest* number of `0`s you must flip to build a bridge joining them.

Constraints: `2 <= n <= 100`; the grid contains exactly two islands.

## Examples

### Example 1

```
Input:  grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
```

**Explanation:** Flipping the two water cells on the shortest path between the island at `(0, 1)` and the island at `(2, 2)` connects them.

## Hint

Flood-fill one island and seed the BFS queue with *all* of its cells at once; expand through water in waves until you touch the other island — the wave count is the bridge length.
