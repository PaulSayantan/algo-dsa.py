# Minimum Spanning Tree (Prim)

**Difficulty:** Medium

**Source:** Classic — Prim's MST via a priority queue

## Description

Given `n` nodes and an undirected weighted edge list `[u, v, w]` (connected graph), return the total weight of a minimum spanning tree using Prim's algorithm with a priority queue.

## Hint

Grow the tree from node 0; a min-heap yields the cheapest edge crossing the cut; skip already-in-tree nodes.
