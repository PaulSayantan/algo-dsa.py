# Interpolation Search

**Interpolation Search** is a searching algorithm for **sorted** arrays that improves on
binary search when the data is **uniformly (or nearly uniformly) distributed**. Instead of
always probing the middle element, it *estimates* where the target should be, the same way a
person opening a phone book looks for "Aaron" near the front and "Zach" near the back rather
than flipping to the exact middle.

## The core idea

Given a search window `[lo, hi]`, binary search always probes `mid = (lo + hi) / 2`.
Interpolation search instead assumes values grow roughly linearly with the index and probes:

```
pos = lo + ((target - arr[lo]) * (hi - lo)) // (arr[hi] - arr[lo])
```

This is linear interpolation: it maps the target's *value* onto an estimated *index*. If the
guess is too small we move `lo = pos + 1`; if too large we move `hi = pos - 1`; if it matches
we are done.

## When to reach for it

- The array is **sorted**.
- The keys are **numeric** and **roughly uniformly distributed** (e.g. evenly spaced IDs,
  timestamps, sensor readings). On such data it dramatically beats binary search.
- You want fewer probes than binary search on large, well-behaved data sets (fewer disk/page
  reads matter for external memory).

Avoid it (or fall back to binary search) when the distribution is skewed/clustered — the probe
can land far off and performance degrades toward linear.

## Complexity

| Metric | Value |
|--------|-------|
| Time (uniform data, average) | **O(log log n)** |
| Time (worst case / skewed data) | **O(n)** |
| Space | **O(1)** (iterative) |

## Key correctness guards

- Only probe while `arr[lo] <= target <= arr[hi]` — this both bounds the estimate and rules out
  targets outside the window early.
- Guard against division by zero when `arr[lo] == arr[hi]` (all remaining values equal).
- The interpolation formula must use integer arithmetic carefully to avoid overflow in languages
  with fixed-width integers (Python integers are arbitrary precision, so this is a non-issue here).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Interpolation Search Basics](problem-01-interpolation-search-basics/PROBLEM.md) | Exact-match search in a uniform sorted array | Easy |
| 2 | [Search Insert Position](problem-02-search-insert-position/PROBLEM.md) | Locate the insertion index for a target | Easy |
| 3 | [Ceiling in a Sorted Array](problem-03-ceiling-in-a-sorted-array/PROBLEM.md) | Smallest element `>=` x (successor) | Medium |
| 4 | [Find First and Last Position](problem-04-find-first-and-last-position/PROBLEM.md) | Range boundaries of a repeated value | Medium |
| 5 | [Find K Closest Elements](problem-05-find-k-closest-elements/PROBLEM.md) | Locate anchor, then two-pointer expand | Medium |
