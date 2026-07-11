# Running Min / Max / Aggregate

**Category:** Arrays / Beginner

## What it is

A *running* (or *prefix* / *cumulative*) statistic is a single value that is
updated as you sweep through an array one element at a time. Instead of
re-scanning previously seen elements, you keep exactly the piece of history you
need in a scalar (or a couple of scalars) and fold each new element into it:

```
running = <identity>
for x in array:
    running = combine(running, x)   # e.g. running + x, min(running, x), max(running, x)
    # use `running` here to answer the question at index i
```

The `combine` operation is usually associative (sum, product, min, max), which
is exactly what makes a single left-to-right pass sufficient. The key mental
model: **at every index `i`, `running` already summarizes everything in
`array[0..i]`, so any answer that depends only on "the best so far" can be read
off in O(1).**

## When to reach for it

- The problem asks for a cumulative quantity: prefix sums, "sum up to here".
- You need the best answer *ending at* or *seen before* the current index
  (running minimum price seen so far, running max/min product, etc.).
- You want to turn an O(n^2) "for each i, look back at all j < i" brute force
  into an O(n) single pass by remembering only an aggregate of the prefix
  rather than the whole prefix.
- Kadane-style dynamic programming, where the DP state is a running best.

## Typical complexity

| Metric | Cost |
| --- | --- |
| Time | O(n) — one pass over the array |
| Space | O(1) — a handful of scalars (O(n) only if you must *store* every prefix value) |

## Problems

| # | Problem | Technique flavor | Difficulty |
| --- | --- | --- | --- |
| 1 | [Running Sum of 1d Array](problem-01-running-sum/PROBLEM.md) | Running aggregate (prefix sum) | Easy |
| 2 | [Best Time to Buy and Sell Stock](problem-02-best-time-to-buy-and-sell-stock/PROBLEM.md) | Running minimum seen so far | Easy |
| 3 | [Minimum Value to Get Positive Step-by-Step Sum](problem-03-min-value-positive-step-sum/PROBLEM.md) | Running min of prefix sums | Easy |
| 4 | [Maximum Subarray](problem-04-maximum-subarray/PROBLEM.md) | Running best-ending-here (Kadane) | Medium |
| 5 | [Maximum Product Subarray](problem-05-maximum-product-subarray/PROBLEM.md) | Running max AND min together | Medium |
| 6 | [Shortest Unsorted Continuous Subarray](problem-06-shortest-unsorted-continuous-subarray/PROBLEM.md) | Running max (fwd) & running min (bwd) | Medium |
