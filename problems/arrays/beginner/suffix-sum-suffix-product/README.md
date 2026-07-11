# Suffix Sum / Suffix Product

## What it is

A **suffix sum** (or **suffix product**) is a cumulative aggregate computed from
the **right** end of an array. It is the mirror image of a prefix sum: instead of
accumulating from left to right, you accumulate from right to left.

Given `nums` of length `n`, a common convention uses a length-`n+1` array `S`
with a trailing identity element:

```
suffixSum[n]  = 0
suffixSum[i]  = nums[i] + nums[i+1] + ... + nums[n-1]   (so suffixSum[i] = nums[i] + suffixSum[i+1])
```

For products, swap addition for multiplication and use the multiplicative
identity `1` as the trailing value:

```
suffixProd[n] = 1
suffixProd[i] = nums[i] * nums[i+1] * ... * nums[n-1]
```

The real power shows up when you combine a **prefix** aggregate with a **suffix**
aggregate. For any index `i`, the prefix holds "everything to the left" and the
suffix holds "everything to the right", so you can answer "aggregate of all
elements except `i`" (or split the array at `i`) in O(1). That pairing is what
makes the classic *Product of Array Except Self* problem solvable without
division and in linear time.

## When to reach for it

- You need, for every index, an aggregate of the elements **to its right**
  (or the combination of left-side and right-side aggregates).
- The problem asks for "array except self", "split the array into a left part
  and a right part", or "how much water/space is bounded on the right".
- You catch yourself running an inner loop that rescans the tail of the array
  from each position — that repeated tail work collapses into one right-to-left
  pass.

Suffix sums pair naturally with prefix sums (see the `prefix-sum-1d` notes):
prefix answers "left of i", suffix answers "right of i", and together they cover
"everything but i".

## Complexity

| Phase | Time | Space |
|-------|------|-------|
| Build the suffix array | O(n) | O(n) |
| Read one suffix value | O(1) | O(1) |
| Prefix + suffix combined pass | O(n) | O(n), or O(1) extra if reused |

The trade-off mirrors prefix sums: one O(n) right-to-left pass replaces repeated
O(n) tail scans, turning an O(n^2) approach into O(n).

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Left and Right Sum Differences](problem-01-left-and-right-sum-differences/PROBLEM.md) | For each index, `|leftSum - rightSum|` using prefix and suffix sums | Easy |
| 2 | [Number of Ways to Split Array](problem-02-number-of-ways-to-split-array/PROBLEM.md) | Count split points where left sum >= right sum | Medium |
| 3 | [Product of Array Except Self](problem-03-product-of-array-except-self/PROBLEM.md) | Product of all elements except self, no division, O(n) | Medium |
| 4 | [Sum of Absolute Differences in a Sorted Array](problem-04-sum-of-absolute-differences-in-a-sorted-array/PROBLEM.md) | Sum of `|nums[i]-nums[j]|` for each i using prefix/suffix sums | Medium |
| 5 | [Trapping Rain Water](problem-05-trapping-rain-water/PROBLEM.md) | Water trapped using left-max prefix and right-max suffix | Hard |
