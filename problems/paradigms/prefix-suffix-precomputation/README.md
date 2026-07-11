# Prefix / Suffix Precomputation

## What it is

**Prefix / Suffix Precomputation** is a paradigm where you scan an array (or string)
once and store *cumulative* information about everything to the **left** of each
index (a prefix array) and/or everything to the **right** of each index (a suffix
array). Once these arrays exist, a question that would otherwise require re-scanning
part of the input can be answered in **O(1)** by combining a couple of precomputed
values.

The canonical example is the **prefix-sum** array:

```
prefix[i] = nums[0] + nums[1] + ... + nums[i-1]      (prefix[0] = 0)
```

With `prefix` in hand, the sum of any range `nums[l..r]` is just
`prefix[r+1] - prefix[l]` — no re-summation needed.

The idea generalizes far beyond addition. The operation only needs to be
**associative** (and ideally invertible for the subtraction trick): sums, products,
XOR, min/max (prefix-max / suffix-max), counts, and "best so far" values all work.
When the operation is not invertible (like `max`), you keep both a prefix array and
a suffix array and combine them at each index.

## When to reach for it

- You must answer **many range queries** (sum / product / xor / min / max) over a
  **static** array. Precompute once, answer each query in O(1).
- The answer at index `i` depends on **both** what comes before it and what comes
  after it (e.g. "product of all other elements", "water trapped above bar `i`",
  "can I split the array here?"). Build a prefix pass and a suffix pass, then merge.
- You want to detect subarrays with a target aggregate (e.g. sum `== k`) by pairing
  prefix values with a **hash map**.

## Typical complexity

| Phase | Time | Space |
|-------|------|-------|
| Build prefix/suffix arrays | O(n) | O(n) |
| Answer one query | O(1) | — |
| Total for `q` queries | O(n + q) | O(n) |

Many single-answer problems can drop the arrays and keep just two running variables,
reducing extra space to **O(1)** (see Trapping Rain Water's two-pointer variant, or
computing suffix products on the fly).

## Problems

| # | Problem | Technique highlight | Difficulty |
|---|---------|---------------------|------------|
| 1 | [Running Sum of 1d Array](problem-01-running-sum-of-1d-array/PROBLEM.md) | Build a plain prefix-sum array | Easy |
| 2 | [Range Sum Query - Immutable](problem-02-range-sum-query-immutable/PROBLEM.md) | Prefix sums to answer O(1) range queries | Easy |
| 3 | [Find Pivot Index](problem-03-find-pivot-index/PROBLEM.md) | Left sum vs. right sum via total − prefix | Easy |
| 4 | [Product of Array Except Self](problem-04-product-of-array-except-self/PROBLEM.md) | Combine prefix products with suffix products | Medium |
| 5 | [Subarray Sum Equals K](problem-05-subarray-sum-equals-k/PROBLEM.md) | Prefix sums + hash map of counts | Medium |
| 6 | [Trapping Rain Water](problem-06-trapping-rain-water/PROBLEM.md) | Prefix-max and suffix-max at each bar | Hard |
