# Coordinate Compression

**Coordinate compression** is the technique of remapping a set of sparse, arbitrarily
large (or negative, or floating-point) values onto a small, dense range of consecutive
integers `0, 1, 2, ..., k-1` while preserving their relative order. Only the *order*
of the values matters for the algorithm, not their actual magnitudes, so we can shrink
the "coordinate space" down to at most `n` distinct positions.

## What it looks like

Given values `[100, 3, 3, 999, -7]`, the sorted distinct values are `[-7, 3, 100, 999]`.
Coordinate compression replaces each original value by the index of that value in the
sorted-unique list:

```
-7  -> 0
 3  -> 1
100 -> 2
999 -> 3
```

so `[100, 3, 3, 999, -7]` becomes `[2, 1, 1, 3, 0]`.

## When to reach for it

- You need a Fenwick tree (BIT) or segment tree **indexed by value**, but the values are
  up to `10^9` (or negative, or `2*10^9` after doubling) — far too large to allocate an
  array over. Compress first so the index range is `O(n)`.
- You only care about **relative order / ranking** (e.g. "how many earlier elements are
  smaller", inversion counting, rank transforms).
- A **sweep line** over intervals where the endpoints are huge but few in number — compress
  the endpoints so each "slot" between consecutive events is a single unit you can index.
- Any problem whose answer is invariant under any strictly-increasing relabeling of the
  inputs.

## The recipe

1. Collect all values that will ever be queried or updated into one list.
2. `sorted(set(values))` to get the sorted-unique coordinates.
3. Build a map `value -> index` (or use binary search / `bisect_left` on the sorted list).
4. Replace every value by its index and run your index-based structure over `[0, k-1]`.

## Complexity

- Building the compression: `O(n log n)` time (dominated by the sort), `O(n)` extra space.
- Each lookup: `O(log n)` with `bisect`, or `O(1)` with a precomputed hash map.
- Downstream structure (BIT / segment tree) then runs over `k <= n` positions instead of
  the full value range.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Rank Transform of an Array](problem-01-rank-transform-of-an-array/PROBLEM.md) | Pure compression: replace each value by its rank | Easy |
| 2 | [Count of Smaller Numbers After Self](problem-02-count-of-smaller-numbers-after-self/PROBLEM.md) | Compression + Fenwick tree over values | Hard |
| 3 | [Reverse Pairs](problem-03-reverse-pairs/PROBLEM.md) | Compress `nums` and `2*nums` together, then BIT | Hard |
| 4 | [Count of Range Sum](problem-04-count-of-range-sum/PROBLEM.md) | Compress prefix sums, then BIT for range counts | Hard |
| 5 | [Falling Squares](problem-05-falling-squares/PROBLEM.md) | Compress x-coordinates, then segment tree | Hard |
| 6 | [Rectangle Area II](problem-06-rectangle-area-ii/PROBLEM.md) | Compress x-coordinates + sweep line over y-events | Hard |
