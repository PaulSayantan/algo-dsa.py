# Shortest Path with Small Integer Weights

**Difficulty:** Hard

**Source:** Classic — Dial's algorithm (bucket queue)

## Description

Given `n` nodes, a directed edge list `[u, v, w]` with small non-negative integer weights, and a source `src`, return the shortest-distance array from `src` (use `-1` for unreachable nodes) using a bucket queue.

## Hint

Bucket B[d] holds nodes at tentative distance d; process buckets in increasing d, relaxing edges.
