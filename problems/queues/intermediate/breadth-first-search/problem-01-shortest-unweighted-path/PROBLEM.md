# Shortest Path in an Unweighted Graph

**Difficulty:** Medium

**Source:** Classic — BFS shortest path

## Description

Given `n` nodes `0..n-1`, an undirected edge list `edges`, and nodes `src` and `dst`, return the number of edges on the shortest path from `src` to `dst`, or `-1` if `dst` is unreachable.

## Hint

BFS from src tracking distance; the first time you dequeue dst, that distance is the answer.
