# Prefix Sum (1D)

## What it is

A **prefix sum** (also called a cumulative sum) is a precomputed array where each
entry holds the sum of all elements up to that position in the original array.
Once you have it, the sum of **any** contiguous range can be answered by a single
subtraction instead of re-adding the elements every time.

Given `nums`, define the prefix array `P` with `P[0] = 0` and
`P[i] = nums[0] + nums[1] + ... + nums[i-1]`. Then the sum of the half-open
range `[l, r)` (i.e. indices `l` through `r-1`) is simply:

```
sum(l, r) = P[r] - P[l]
```

Using the length-`n+1` convention with a leading `0` avoids awkward special cases
for ranges that start at index 0.

## When to reach for it

- You need to answer **many range-sum queries** on a fixed array.
- You want to detect subarrays with a target sum, a sum divisible by `k`, or a
  balanced count of two symbols — often by pairing prefix sums with a hash map.
- Any time you catch yourself recomputing overlapping partial sums in a loop.

Prefix sums are the 1D building block behind difference arrays, 2D integral
images, and Fenwick/segment trees.

## Complexity

| Phase | Time | Space |
|-------|------|-------|
| Build the prefix array | O(n) | O(n) |
| Answer one range-sum query | O(1) | O(1) |
| `q` queries total | O(n + q) | O(n) |

The core trade-off: spend O(n) time and space up front so every later query is O(1).

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Running Sum of 1d Array](problem-01-running-sum-of-1d-array/PROBLEM.md) | Produce the prefix-sum array itself | Easy |
| 2 | [Range Sum Query - Immutable](problem-02-range-sum-query-immutable/PROBLEM.md) | Answer many range-sum queries in O(1) each | Easy |
| 3 | [Find Pivot Index](problem-03-find-pivot-index/PROBLEM.md) | Locate the index where left sum equals right sum | Easy |
| 4 | [Subarray Sum Equals K](problem-04-subarray-sum-equals-k/PROBLEM.md) | Count subarrays summing to `k` via prefix sums + hash map | Medium |
| 5 | [Contiguous Array](problem-05-contiguous-array/PROBLEM.md) | Longest subarray with equal 0s and 1s via a +1/-1 transform | Medium |
| 6 | [Subarray Sums Divisible by K](problem-06-subarray-sums-divisible-by-k/PROBLEM.md) | Count subarrays whose sum is divisible by `k` using prefix mod | Medium |
