# Meet in the Middle

**Meet in the Middle (MITM)** is a divide-and-combine paradigm for search
problems whose brute force is exponential (typically `O(2^n)` or `O(k^n)`).
The idea: split the input into two halves, **enumerate every possibility of
each half independently**, then **combine** the two precomputed halves cheaply
(hash lookup, sorting + binary search, or two pointers) to reconstruct answers
that span both halves.

The payoff is a square-root-style speedup on the exponent:

```
Brute force over the whole input : O(2^n)
Meet in the middle               : O(2^(n/2) * poly(n))   time
                                   O(2^(n/2))              space
```

Because `2^(n/2) = sqrt(2^n)`, MITM turns an impossible `n = 40` (about
`10^12` states) into a very comfortable `2^20 ≈ 10^6` per half.

## When to reach for it

- The natural brute force is exponential and `n` is *just* out of reach:
  roughly `30 <= n <= 45` for `2^n` problems.
- Each element makes an independent binary (or small) choice: pick/skip,
  assign to group A/B, add/subtract, etc.
- A candidate solution can be **split into two independent parts** whose
  contributions simply **add up** (or compose associatively), so half-answers
  can be combined by matching a "left value" against a needed "right value".
- You are willing to trade memory (`O(2^(n/2))`) for time.

Typical combine tools once each half is enumerated:

| Combine goal                         | Tool                                  |
|--------------------------------------|---------------------------------------|
| Exact match / count of matches       | Hash map / `Counter`                  |
| Closest value to a target            | Sort one half + binary search         |
| Best pair under a monotone condition | Sort both + two pointers              |

MITM also powers number-theory algorithms such as **Baby-Step Giant-Step**
for discrete logarithms, where the two "halves" are the exponent written as
`i*m + j`.

## Complexity at a glance

- **Time:** `O(2^(n/2) * f)` where `f` is the per-item combine cost
  (`O(1)` for hashing, `O(n)` for a binary search / sort factor).
- **Space:** `O(2^(n/2))` to store one (or both) halves' enumerations.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [4Sum II](problem-01-four-sum-ii/PROBLEM.md) | Split 4 arrays into 2 + 2, hash one pair-sum, look up the complement | Medium |
| 2 | [Count Subsets with Given Sum (n ≤ 40)](problem-02-subset-sum/PROBLEM.md) | Enumerate subset sums of each half, match with a `Counter` | Medium |
| 3 | [Closest Subsequence Sum](problem-03-closest-subsequence-sum/PROBLEM.md) | Half subset sums + sort + binary search for the nearest total | Hard |
| 4 | [Partition Array to Minimize Sum Difference](problem-04-partition-min-diff/PROBLEM.md) | MITM grouped by chosen-count, sort + binary search per group | Hard |
| 5 | [Discrete Logarithm (Baby-Step Giant-Step)](problem-05-discrete-logarithm/PROBLEM.md) | Write `x = i*m + j`; baby-step table meets giant steps | Hard |
