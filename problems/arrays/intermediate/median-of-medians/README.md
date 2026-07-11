# Median of Medians

**Median of Medians** is a deterministic pivot-selection strategy that lets the
classic *Quickselect* algorithm run in **guaranteed worst-case O(n)** time
instead of the O(n^2) worst case you get with a naive or random pivot. It is the
heart of the CLRS `SELECT` algorithm (Blum-Floyd-Pratt-Rivest-Tarjan, 1973), and
it answers a deep question: *can we find the k-th smallest element of an
unsorted array in linear time, in the worst case, deterministically?* Yes.

## The core idea

To pick a "good enough" pivot in linear time:

1. Divide the `n` elements into `⌈n/5⌉` groups of 5 (the last group may be
   smaller).
2. Find the median of each group by sorting it (sorting 5 elements is O(1)).
3. Recursively apply the whole selection routine to the list of `⌈n/5⌉` group
   medians to get the **median of medians**, `M`.
4. Use `M` as the pivot to partition the array (three-way / Lomuto / Hoare
   style), then recurse into only the side that contains rank `k`.

The magic is a counting argument: `M` is guaranteed to be greater than at least
`~3n/10` elements and less than at least `~3n/10` elements. So each partition
discards at least ~30% of the array, and the recurrence

```
T(n) = T(n/5)  +  T(7n/10)  +  O(n)
```

solves to **T(n) = O(n)** because `1/5 + 7/10 = 9/10 < 1`.

## When to reach for it

- You need a **worst-case** linear-time k-th order statistic (median, quantile)
  and cannot tolerate the adversarial O(n^2) of random Quickselect (e.g.
  hard real-time systems, or defending against malicious inputs).
- You need a linear-time pivot to guarantee **worst-case O(n log n)** for an
  introselect / median-partition-based algorithm.
- Any problem reducible to "find the element of rank k without fully sorting."

In practice, **randomized Quickselect** (expected O(n)) is faster due to smaller
constants; Median of Medians is the theoretical guarantee you fall back on when
the worst case must be bounded. Group size 5 is the smallest odd size that makes
the recurrence sum to `< 1` (groups of 3 fail; 7 also works but with worse
constants).

## Complexity

| Metric | Value |
| --- | --- |
| Time (worst case) | **O(n)** |
| Time (expected) | O(n) |
| Extra space | O(n) copy-based, or O(log n) in-place recursion stack |

## Problems

| # | Problem | Summary | Difficulty |
| --- | --- | --- | --- |
| 1 | [Kth Smallest Element in an Array](problem-01-kth-smallest-element/PROBLEM.md) | Find the k-th smallest value without fully sorting | Easy |
| 2 | [Median of an Unsorted Array](problem-02-median-of-unsorted-array/PROBLEM.md) | Compute the (lower) median in worst-case linear time | Medium |
| 3 | [K Closest Points to Origin](problem-03-k-closest-points-to-origin/PROBLEM.md) | Return the k points nearest the origin (LeetCode 973) | Medium |
| 4 | [Weighted Median](problem-04-weighted-median/PROBLEM.md) | Find the lower weighted median in linear time (CLRS 9-2) | Medium |
| 5 | [Wiggle Sort II](problem-05-wiggle-sort-ii/PROBLEM.md) | Reorder so nums[0]<nums[1]>nums[2]<... (LeetCode 324) | Hard |
