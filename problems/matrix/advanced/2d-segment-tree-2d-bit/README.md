# 2D Segment Tree / 2D BIT (Fenwick Tree)

A **2D Binary Indexed Tree (Fenwick Tree)** and a **2D Segment Tree** extend
their 1D counterparts to answer queries over **submatrices / axis-aligned
rectangles** while still supporting updates.

Think of each structure as a "tree of trees": the outer structure indexes rows,
and every node of the outer structure holds an inner 1D structure indexing
columns. A single operation walks `O(log n)` outer nodes, and at each one walks
`O(log m)` inner nodes — hence the signature **`O(log n · log m)`** cost, usually
written `O(log² n)` for a square `n × n` grid.

## When to reach for it

- You need **both** updates and range/aggregate queries over a 2D grid.
  (If the grid is static, a plain 2D prefix-sum array is simpler and `O(1)` per
  query — reach for a tree only when values change.)
- **2D BIT** — for *invertible* aggregates: sums, counts, XOR. It is the go-to
  because it is tiny to code, cache-friendly, and uses `O(nm)` memory. It has
  several modes:
  - point-update / range-query (frequencies, submatrix sums),
  - range-update / point-query (add to a rectangle, read a cell — via a 2D
    difference decomposition),
  - range-update / range-query (four BITs, the 2D analogue of the 1D trick).
- **2D Segment Tree** — for aggregates a BIT cannot easily undo, most notably
  **range max / min** with point updates, or when you need lazy propagation
  patterns a BIT does not support.

## Complexity summary

| Structure | Build | Update | Query | Space |
|---|---|---|---|---|
| 2D BIT | `O(nm)` (or `O(nm·log n·log m)` naively) | `O(log n · log m)` | `O(log n · log m)` | `O(nm)` |
| 2D Segment Tree | `O(nm)` | `O(log n · log m)` | `O(log n · log m)` | `O(nm)` (≈ 4× const.) |

For large or sparse coordinate ranges, combine with **coordinate compression**
or an **offline sweep** so the grid dimensions stay `O(#events)`.

## Problems

| # | Problem | Technique | Difficulty |
|---|---------|-----------|------------|
| 1 | [Range Sum Query 2D - Mutable](problem-01-range-sum-query-2d-mutable/PROBLEM.md) | 2D BIT, point update + submatrix sum | Medium |
| 2 | [Increment Submatrices by One](problem-02-increment-submatrices-by-one/PROBLEM.md) | 2D BIT, range update + point/read query | Medium |
| 3 | [Count Points in a Rectangle](problem-03-count-points-in-rectangle/PROBLEM.md) | 2D BIT of frequencies, online rectangle counting | Medium |
| 4 | [Submatrix Maximum with Point Updates](problem-04-submatrix-maximum-point-update/PROBLEM.md) | 2D Segment Tree for range max | Hard |
| 5 | [Iahub and Xors](problem-05-iahub-and-xors/PROBLEM.md) | 2D BIT range-update range-query (XOR / parity buckets) | Hard |
| 6 | [The Untended Antiquity](problem-06-untended-antiquity/PROBLEM.md) | 2D BIT range-update point-query + random hashing | Hard |
