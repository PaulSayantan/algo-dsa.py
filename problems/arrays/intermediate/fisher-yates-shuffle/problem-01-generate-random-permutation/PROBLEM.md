# Generate a Random Permutation

**Difficulty:** Easy

**Source:** Classic (CLRS "Randomize-In-Place", *Introduction to Algorithms* §5.3)

## Description

Given an integer `n`, return a **uniformly random permutation** of the numbers
`[0, 1, 2, ..., n - 1]`. Each of the `n!` possible orderings must be equally likely —
that is, every ordering should occur with probability exactly `1/n!`.

You must implement the shuffle yourself; you may **not** call a library routine such as
`random.shuffle`. You may only draw uniform random integers from a bounded range (for
example `random.randint(a, b)`). Aim to run in linear time and to shuffle the array in
place using constant extra space.

The naive idea of "for each position, pick a random index from the whole array and
swap" looks correct but is actually **biased**: it can generate certain permutations
more often than others. The task is to produce a *provably unbiased* permutation.

## Constraints

- `1 <= n <= 10^5`
- The result must be a permutation of `[0, n - 1]` (each value appears exactly once).
- Every permutation must be equally likely.

## Examples

### Example 1

```
Input:  n = 1
Output: [0]
Explanation: With a single element there is only 1! = 1 permutation, so the result is
always [0].
```

### Example 2

```
Input:  n = 3
Output: [2, 0, 1]   (one possible result)
Explanation: There are 3! = 6 equally likely orderings of [0, 1, 2]:
[0,1,2], [0,2,1], [1,0,2], [1,2,0], [2,0,1], [2,1,0]. Any single run returns one of
these, each with probability 1/6. [2, 0, 1] is one valid outcome.
```

### Example 3

```
Input:  n = 2
Output: [1, 0]   (one possible result)
Explanation: The two equally likely results are [0, 1] and [1, 0], each with
probability 1/2.
```

## Hint

Use the **Fisher–Yates Shuffle**: iterate from the last index down to the first, and
at each index `i` swap with a uniformly random index chosen in the **inclusive** range
`[0, i]`. The inclusive upper bound (including `i` itself) is exactly what keeps the
permutation unbiased.
