# Number of Provinces

**Difficulty:** Medium

**Source:** LeetCode 547 — Number of Provinces

## Description

Given an `n x n` adjacency matrix `isConnected`, return the number of connected components (provinces) among the `n` cities.

## Examples

### Example 1

```
Input:  [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
```

## Hint

DFS from each unvisited city, marking a visited set; each launch is one province.
