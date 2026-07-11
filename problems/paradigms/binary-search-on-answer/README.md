# Binary Search on Answer

## What it is

**Binary Search on Answer** (also called *parametric search* or *binary search on
the result*) is a paradigm where you do **not** binary-search the input array.
Instead you binary-search the **space of possible answers**.

The trick works whenever the answer is a number in some range `[lo, hi]` and you
can write a **feasibility predicate** `check(x)` that returns a boolean, such that
the predicate is **monotonic** in `x`:

```
check(x):   F F F F F T T T T T        (find first True  → minimization)
check(x):   T T T T T F F F F F        (find last  True  → maximization)
```

If `check` flips from `False` to `True` exactly once as `x` increases, the value
space is *sorted* by the predicate even though the raw data is not. So you can
binary-search for the boundary: the smallest `x` that is feasible (a
*minimize-the-max* problem) or the largest `x` that is feasible (a
*maximize-the-min* problem).

## When to reach for it

Look for these tell-tale signs in a problem statement:

- It asks for the **minimum** value that still makes something possible, or the
  **maximum** value that keeps something possible ("smallest capacity such that
  ...", "largest minimum distance such that ...", "minimum speed to finish in
  time").
- A candidate answer can be **verified far more cheaply than it can be
  constructed**. You can quickly test "is answer `x` good enough?" even if you
  cannot directly compute the optimum.
- The feasibility of a candidate is **monotonic**: if `x` works, everything on
  one side of `x` also works (a bigger ship capacity is never *worse*; a faster
  eating speed never *misses* a deadline it already met).
- The answer range is numeric and bounded (integer speeds, capacities,
  distances, matrix values, pair distances).

If you can articulate a monotonic `check(x)`, you can almost always replace an
`O(range)` linear scan over candidate answers with an `O(log range)` search.

## Why it works

Binary search only needs the search space to be **sorted with respect to the
question you ask**, not sorted in value. The predicate `check` imposes exactly
that order: once it becomes `True` it stays `True` (or vice-versa). Each step
halves the candidate interval, and the invariant "the boundary lies inside
`[lo, hi]`" is preserved, so the loop converges to the flip point.

The classic template for **minimize** (find the smallest feasible `x`):

```
lo, hi = smallest_possible, largest_possible
while lo < hi:
    mid = (lo + hi) // 2
    if check(mid):      # mid is feasible → answer is mid or smaller
        hi = mid
    else:               # mid too small   → answer is strictly larger
        lo = mid + 1
return lo               # first x with check(x) == True
```

For **maximize** (find the largest feasible `x`), bias `mid` upward and keep the
feasible half:

```
while lo < hi:
    mid = (lo + hi + 1) // 2   # +1 avoids an infinite loop
    if check(mid):
        lo = mid
    else:
        hi = mid - 1
return lo
```

## Typical complexity

| Cost   | Value                                                                 |
|--------|-----------------------------------------------------------------------|
| Time   | `O(C * log(hi - lo))` where `C` is the cost of one `check` call        |
| Space  | `O(1)` beyond whatever `check` itself needs                           |

The `log` factor is over the **value range**, so even ranges up to `10^18` cost
only ~60 iterations. The predicate cost `C` (often `O(n)`) dominates.

## Problems

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 1 | [Sqrt(x)](problem-01-sqrt-x/PROBLEM.md) | Search integer `k` with `k*k <= x`; classic minimize/last-true boundary | Easy |
| 2 | [Koko Eating Bananas](problem-02-koko-eating-bananas/PROBLEM.md) | Minimize eating speed subject to a monotonic "finishes in time" predicate | Medium |
| 3 | [Capacity To Ship Packages Within D Days](problem-03-capacity-to-ship-packages/PROBLEM.md) | Minimize ship capacity subject to "packs into <= D days" | Medium |
| 4 | [Magnetic Force Between Two Balls](problem-04-magnetic-force-between-balls/PROBLEM.md) | Maximize the minimum gap ("aggressive cows") — maximize-the-min | Medium |
| 5 | [Kth Smallest Element in a Sorted Matrix](problem-05-kth-smallest-in-sorted-matrix/PROBLEM.md) | Binary-search the *value* range using a "how many <= x" counter | Medium |
| 6 | [Find K-th Smallest Pair Distance](problem-06-kth-smallest-pair-distance/PROBLEM.md) | Binary-search the distance value; count pairs with a sliding window | Hard |
