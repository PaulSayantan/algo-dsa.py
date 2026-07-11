# Prefix Sum + Hash Map

## What it is

A **prefix sum** (a.k.a. running/cumulative sum) is the sum of all array
elements from the start up to (and including) index `i`:

```
prefix[i] = nums[0] + nums[1] + ... + nums[i]
```

The key identity is that the sum of any subarray `nums[i..j]` equals a
difference of two prefix sums:

```
sum(nums[i..j]) = prefix[j] - prefix[i-1]
```

So "does a subarray with sum `S` end at index `j`?" becomes "have I ever seen
a prefix sum equal to `prefix[j] - S`?". A **hash map** answers that question
in O(1): as we sweep left to right, we store every prefix sum we have seen
(mapping it to a *count* of occurrences, or to its *earliest index*, depending
on what the problem asks). This turns an O(n^2) "check every subarray" search
into a single O(n) pass.

## When to reach for it

Reach for Prefix Sum + Hash Map when a problem asks about **contiguous
subarrays** and a property that can be expressed as a *difference of running
sums*, such as:

- Count / find subarrays whose sum equals a target `k`.
- Find the **longest** (or shortest) subarray with a given sum — store the
  *earliest* index of each prefix sum.
- **Count** how many subarrays satisfy a sum condition — store *counts* of
  each prefix sum.
- Sum divisibility / "multiple of k" problems — key the map on the prefix-sum
  **remainder mod k** instead of the raw sum.
- Binary-array "equal counts" problems — remap values (e.g. `0 -> -1`) so the
  target becomes a subarray of sum `0`.

If the array has only non-negative values and you need a contiguous window,
consider the sliding-window technique too — but prefix sum + hash map also
handles **negative numbers**, which sliding window generally cannot.

## Typical complexity

- **Time:** O(n) — a single pass, with O(1) expected hash-map operations.
- **Space:** O(n) — the map may hold up to n distinct prefix sums (or up to
  `k` distinct remainders for modular variants).

## The seed-with-zero trick

Almost every variant initializes the map with the "empty prefix":
`{0: 1}` (count form) or `{0: -1}` (earliest-index form). This represents the
prefix sum *before* any element, so that a subarray starting at index `0` is
counted correctly.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Subarray Sum Equals K](problem-01-subarray-sum-equals-k/PROBLEM.md) | Count contiguous subarrays whose sum equals `k`. | Medium |
| 2 | [Contiguous Array](problem-02-contiguous-array/PROBLEM.md) | Longest subarray with equal numbers of 0s and 1s (remap `0 -> -1`). | Medium |
| 3 | [Maximum Size Subarray Sum Equals k](problem-03-maximum-size-subarray-sum-equals-k/PROBLEM.md) | Length of the *longest* subarray summing to `k`. | Medium |
| 4 | [Binary Subarrays With Sum](problem-04-binary-subarrays-with-sum/PROBLEM.md) | Count binary-array subarrays summing to `goal`. | Medium |
| 5 | [Continuous Subarray Sum](problem-05-continuous-subarray-sum/PROBLEM.md) | Detect a length >= 2 subarray whose sum is a multiple of `k` (remainder map). | Medium |
| 6 | [Subarray Sums Divisible by K](problem-06-subarray-sums-divisible-by-k/PROBLEM.md) | Count subarrays whose sum is divisible by `k` (remainder counts). | Medium |
