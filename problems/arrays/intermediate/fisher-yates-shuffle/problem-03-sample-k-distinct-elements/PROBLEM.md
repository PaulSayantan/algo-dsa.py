# Sample K Distinct Elements

**Difficulty:** Medium

**Source:** Classic (partial Fisher–Yates / "random sample without replacement",
`random.sample` semantics)

## Description

Given an array `nums` of `n` distinct integers and an integer `k` with
`0 <= k <= n`, return a list of `k` elements chosen **uniformly at random without
replacement** from `nums`. "Uniform without replacement" means that every one of the
`C(n, k)` possible `k`-subsets is equally likely to be selected, and no element is
picked twice.

You must implement the sampling yourself; you may not call `random.sample`. Aim to do
the work in **O(k)** random draws (proportional to the sample size, not the full array
size) and without building the full random permutation when `k` is much smaller than
`n`.

This is the natural generalization of shuffling: a full shuffle is the special case
`k == n`. The insight is that you only need to run the **first `k` iterations** of a
Fisher–Yates sweep to fix the first `k` positions — the rest of the array can be left
untouched.

## Constraints

- `1 <= n <= 10^5`
- `0 <= k <= n`
- All elements of `nums` are distinct.
- Every `k`-subset (and, within the returned list, order does not affect subset
  membership) must be equally likely.

## Examples

### Example 1

```
Input:  nums = [10, 20, 30, 40], k = 2
Output: [30, 10]   (one possible result)
Explanation: There are C(4, 2) = 6 equally likely 2-subsets:
{10,20}, {10,30}, {10,40}, {20,30}, {20,40}, {30,40}, each chosen with probability
1/6. The pair {10, 30} — here returned as [30, 10] — is one valid outcome.
```

### Example 2

```
Input:  nums = [5, 6, 7], k = 3
Output: [7, 5, 6]   (one possible result)
Explanation: k == n, so this is a full shuffle. All 3! = 6 orderings are equally
likely; every element appears exactly once.
```

### Example 3

```
Input:  nums = [42], k = 0
Output: []
Explanation: Sampling zero elements returns the empty list, the only 0-subset.
```

## Hint

Use a **partial Fisher–Yates Shuffle**: run only the first `k` iterations. For each of
the `k` front positions, swap it with a uniformly random index chosen from the current
position through the end of the array, then return those first `k` elements. Work on a
copy so the input is not disturbed.
