# Segment Tree

A **segment tree** is a binary tree built over an array where every node stores an
aggregate (sum, min, max, gcd, count, ...) of a contiguous *segment* (range) of the
array. The root covers the whole array `[0, n-1]`, each internal node splits its
range in half, and the leaves correspond to individual elements. Because the tree
has height `O(log n)`, both a **point update** (change one element) and a **range
query** (aggregate over `[l, r]`) touch only `O(log n)` nodes.

## When to reach for it

Reach for a segment tree when you have an array that is **queried and mutated many
times**, and each query asks for an aggregate over an arbitrary sub-range. A plain
prefix-sum array answers range-sum queries in `O(1)` but costs `O(n)` per update; a
segment tree balances both at `O(log n)`. It also generalizes to *any* associative
merge operation (min, max, gcd, product, count-in-value-range, ...), which prefix
sums cannot do.

Typical signals:
- "process a stream of updates *interleaved* with range queries"
- range min / max / sum / gcd with mutation
- counting problems reframed over a **value domain** (frequency of values in a range)
- accelerating a DP whose transition is "take the best over a range of states"

For **range updates** (update a whole interval at once) you extend the structure
with *lazy propagation* — see the sibling `segment-tree-with-lazy-propagation`
directory.

## Complexity

| Operation                | Time       | Space  |
|--------------------------|------------|--------|
| Build from array         | `O(n)`     | `O(n)` |
| Point update             | `O(log n)` | —      |
| Range query              | `O(log n)` | —      |
| (with lazy) range update | `O(log n)` | —      |

The array-backed (iterative or recursive) implementation uses `2n` to `4n` nodes,
i.e. `O(n)` space.

## Core invariant

For an internal node covering `[lo, hi]` with `mid = (lo + hi) // 2`:

```
value[node] = merge(value[left_child covering [lo, mid]],
                    value[right_child covering [mid+1, hi]])
```

A query descends from the root and combines only the `O(log n)` nodes whose ranges
are fully inside `[l, r]`. An update walks down to a leaf and re-merges on the way
back up.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Range Sum Query - Mutable](problem-01-range-sum-query-mutable/PROBLEM.md) | Point update + range **sum** — the canonical intro | Medium |
| 2 | [Range Minimum Query](problem-02-range-minimum-query/PROBLEM.md) | Same shape, **min** aggregate (any associative merge works) | Medium |
| 3 | [Count of Smaller Numbers After Self](problem-03-count-of-smaller-numbers-after-self/PROBLEM.md) | Segment tree over the **value domain** (frequency counting) | Hard |
| 4 | [Count of Range Sum](problem-04-count-of-range-sum/PROBLEM.md) | Tree over **prefix sums** + coordinate compression | Hard |
| 5 | [Longest Increasing Subsequence II](problem-05-longest-increasing-subsequence-ii/PROBLEM.md) | Range-**max** query to accelerate a DP | Hard |
