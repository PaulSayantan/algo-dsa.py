# Binary Search on Answer

**Binary Search on Answer** (also called *binary search on the value space* or *parametric search*) is a technique where, instead of binary-searching for a target inside a sorted array of indices, you binary-search over the **range of possible answers** to a problem.

## The Core Idea

Many optimization problems ask: *"What is the smallest / largest value `X` such that some condition holds?"* These become solvable with binary search when the condition is **monotonic** in `X` — i.e. there is a single "flip point" in the answer space:

```
feasible(X):  F F F F T T T T T T
                      ^
                      first T  =  the answer we want (minimize)
```

If a candidate answer `X` works, then every value on one side of `X` also works (and everything on the other side fails). Because the `feasible` predicate is monotonic, we can throw away half of the candidate answers at each step — exactly like classic binary search, but the search space is a *range of values*, not array positions.

## When to Reach for It

Look for these signals in a problem statement:

- It asks to **minimize a maximum** or **maximize a minimum** ("smallest capacity", "minimum eating speed", "largest minimum distance").
- The answer is a single number within a clear numeric range `[lo, hi]`.
- Checking *"can we achieve the answer `X`?"* is easy (often O(n)), even though searching for the best `X` directly is hard.
- That feasibility check is **monotonic**: if `X` works, then all larger (or all smaller) values also work.

## General Recipe

1. Identify the answer range `[lo, hi]`.
2. Write a `feasible(mid)` predicate that returns whether `mid` is a valid answer.
3. Binary search for the boundary — the first (or last) `mid` where `feasible` flips.
4. Return that boundary value (not `mid`'s midpoint index).

## Complexity

For a search range of size `R` and an O(n) feasibility check, the total time is **O(n · log R)** and the space is **O(1)** (beyond the input). This turns problems whose brute-force answer scan would be O(n · R) into logarithmic-factor searches.

## Problems

| # | Problem | Difficulty | Summary |
|---|---------|------------|---------|
| 1 | [Sqrt(x)](problem-01-sqrt-x/PROBLEM.md) | Easy | Integer square root — search the value `k` with `k*k <= x`. |
| 2 | [Koko Eating Bananas](problem-02-koko-eating-bananas/PROBLEM.md) | Medium | Minimum eating speed to finish all bananas within `h` hours. |
| 3 | [Capacity To Ship Packages Within D Days](problem-03-capacity-to-ship-packages/PROBLEM.md) | Medium | Least ship capacity to deliver all packages in `days` days. |
| 4 | [Smallest Divisor Given a Threshold](problem-04-smallest-divisor/PROBLEM.md) | Medium | Smallest divisor so the sum of ceil-divisions stays under a threshold. |
| 5 | [Split Array Largest Sum](problem-05-split-array-largest-sum/PROBLEM.md) | Hard | Split into `k` subarrays minimizing the largest subarray sum. |
