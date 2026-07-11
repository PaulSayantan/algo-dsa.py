# Maximum Subarray via Divide & Conquer

**Split, combine best-crossing subarray — an alternative to Kadane.**

## What it is

The maximum-subarray problem asks for the contiguous slice of an array with the
largest sum (or product, or other associative combine). The **divide & conquer**
approach — the one presented in CLRS chapter 4 — solves it by recursion:

1. **Divide** the array at the midpoint `mid` into a left half and a right half.
2. **Conquer** by recursively finding the best subarray that lies *entirely* in
   the left half and the best that lies *entirely* in the right half.
3. **Combine** by computing the best subarray that *crosses* the midpoint. A
   crossing subarray is always the best suffix of the left half joined to the
   best prefix of the right half, each found by a single linear scan outward
   from `mid`.
4. The answer for the whole range is the maximum of those three candidates.

The crossing step is what makes the recursion work: it is the only place the two
halves talk to each other, and it is where "the best subarray" is actually
reconstructed across the boundary.

## When to reach for it

- As an **alternative to Kadane's algorithm** when you want to *practice*
  divide & conquer, or when a linear DP is not obvious.
- When you need to answer **range maximum-subarray queries** (possibly with
  updates). Here the crossing-combine merge becomes a **segment-tree node** that
  stores `(total, best_prefix, best_suffix, best)` — this is the idiomatic and
  essentially the only clean solution, and it is pure divide & conquer.
- When the "combine" is more than a plain sum (products, circular wrap, etc.) and
  you want a structured way to reason about what a subarray crossing a boundary
  looks like.

## Typical complexity

| Variant | Time | Space |
| --- | --- | --- |
| One-shot max subarray (recursive) | `O(n log n)` | `O(log n)` recursion stack |
| Segment-tree build | `O(n)` | `O(n)` |
| Segment-tree range query / point update | `O(log n)` per op | `O(n)` |

The one-shot `O(n log n)` is asymptotically slower than Kadane's `O(n)`, so on a
single query Kadane wins — divide & conquer earns its keep when the same
structure must answer many range queries, or when the problem is a teaching
vehicle for the recursion.

## Problems

| # | Problem | Technique focus | Difficulty |
| --- | --- | --- | --- |
| 1 | [Maximum Subarray](problem-01-maximum-subarray/PROBLEM.md) | The classic sum, three-candidate recursion | Easy/Medium |
| 2 | [Maximum Subarray With Indices](problem-02-maximum-subarray-with-indices/PROBLEM.md) | Return the actual `(start, end, sum)`, CLRS style | Medium |
| 3 | [Maximum Sum Circular Subarray](problem-03-maximum-sum-circular-subarray/PROBLEM.md) | Extend the merge to a wrap-around via total − min | Medium |
| 4 | [Maximum Product Subarray](problem-04-maximum-product-subarray/PROBLEM.md) | Combine step must track min *and* max across the split | Medium/Hard |
| 5 | [Range Maximum Subarray Query](problem-05-range-maximum-subarray-query/PROBLEM.md) | Turn the merge into a segment-tree node (SPOJ GSS1) | Hard |
