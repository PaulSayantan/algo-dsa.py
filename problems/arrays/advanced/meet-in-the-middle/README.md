# Meet in the Middle

**Meet in the Middle (MITM)** is a divide-and-combine technique for problems where a
brute-force enumeration of all `2^n` subsets (or `k^n` choices) is too slow, but `n`
is small enough (typically `n ≈ 30–40`) that `2^(n/2)` is comfortably manageable.

## The core idea

1. **Split** the `n` elements into two halves `A` (size `⌈n/2⌉`) and `B` (size `⌊n/2⌋`).
2. **Enumerate** all subsets of each half independently. Each half has at most
   `2^(n/2)` subsets, so this is cheap even when `2^n` is astronomical.
3. **Combine** the two lists of partial results. Sort one list and use binary search,
   a hash map, or a two-pointer sweep so that combining costs
   `O(2^(n/2) · (n/2))` instead of `O(2^(n/2) · 2^(n/2)) = O(2^n)`.

Because `2^(n/2) = sqrt(2^n)`, MITM turns an infeasible `2^40 ≈ 10^12` search into a
very feasible `2^20 ≈ 10^6` search (times a log factor for sorting/binary search).

## When to reach for it

- Subset-sum / partition / "closest sum" style problems with `n` up to ~40.
- 0/1 knapsack where the *capacity* is huge (so weight-indexed DP is impossible) but
  the *number of items* is small (`n ≤ 40`).
- Any problem where each element independently makes an O(1)-choice (include/exclude,
  or one of a few options) and only an aggregate (sum, XOR, count) of the choices
  matters for combining.
- The tell-tale constraint is a suspiciously small `n` (30–45) paired with values or a
  target far too large for a polynomial DP.

## Typical complexity

- **Time:** `O(2^(n/2) · n)` — dominated by generating and sorting the half-subsets and
  a binary search / hash lookup per subset of the other half.
- **Space:** `O(2^(n/2))` to store the enumerated partial sums of at least one half.

Compare this to naive brute force at `O(2^n)` and (where applicable) subset-sum DP at
`O(n · target)` — MITM wins precisely when `target`/capacity is enormous but `n` is tiny.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Subset Sum Exists](problem-01-subset-sum-exists/PROBLEM.md) | Decide whether some subset of up to 40 numbers sums to a target. | Medium |
| 2 | [Count Subsets With Given Sum](problem-02-count-subsets-with-given-sum/PROBLEM.md) | Count how many subsets of up to 40 numbers sum exactly to a target. | Medium |
| 3 | [Closest Subsequence Sum](problem-03-closest-subsequence-sum/PROBLEM.md) | Minimize `|subset sum − goal|` over all subsequences (LeetCode 1755). | Hard |
| 4 | [Partition Array to Minimize Sum Difference](problem-04-partition-min-sum-difference/PROBLEM.md) | Split `2n` numbers into two equal-size halves minimizing the sum difference (LeetCode 2035). | Hard |
| 5 | [Maximum Subset Value Under Weight Limit](problem-05-max-value-under-weight-limit/PROBLEM.md) | 0/1 knapsack with `n ≤ 40` items and huge capacity. | Hard |
