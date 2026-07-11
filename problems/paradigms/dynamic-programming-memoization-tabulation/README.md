# Dynamic Programming (Memoization / Tabulation)

## What it is

**Dynamic Programming (DP)** is an algorithm-design paradigm for problems that can be
broken into **overlapping subproblems** with **optimal substructure**. Instead of
recomputing the same subproblem again and again (as naive recursion does), DP solves
each distinct subproblem **once** and reuses the cached result.

There are two complementary styles:

- **Memoization (top-down):** Write the natural recursion, but store each subproblem's
  answer in a cache (dict/array) keyed by its arguments. Before computing, check the
  cache. This is recursion + a lookup table.
- **Tabulation (bottom-up):** Identify the order in which subproblems depend on one
  another, then fill a table iteratively from the base cases up to the final answer.
  No recursion, so no stack-depth limits and usually a smaller constant factor.

## When to reach for it

Reach for DP when **all** of these hold:

1. **Optimal substructure** — the optimal answer to the whole problem is built from
   optimal answers to smaller instances.
2. **Overlapping subproblems** — the same smaller instances recur many times (this is
   what separates DP from plain divide-and-conquer like merge sort).
3. You are asked for a **count**, an **optimum** (min/max), a **yes/no feasibility**, or
   an **enumeration** over choices made in stages.

A reliable recipe:

1. Define the **state** (what parameters uniquely identify a subproblem).
2. Write the **recurrence** (transition) relating a state to smaller states.
3. Nail the **base cases**.
4. Choose memoization or tabulation and, if possible, **compress the space**.

## Typical complexity

For a DP with `S` distinct states and `T` work per transition, the time is `O(S * T)`
and the space is `O(S)` (often reducible to `O(1)` or one row when a state depends only
on a bounded window of previous states). This turns many exponential brute-force
recursions into polynomial-time solutions.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Fibonacci Number](problem-01-fibonacci-number/PROBLEM.md) | Canonical 1D DP; memo vs. table vs. rolling variables | Easy |
| 2 | [Climbing Stairs](problem-02-climbing-stairs/PROBLEM.md) | Counting paths with a Fibonacci-style recurrence | Easy |
| 3 | [House Robber](problem-03-house-robber/PROBLEM.md) | 1D DP with a take/skip decision per element | Medium |
| 4 | [Coin Change](problem-04-coin-change/PROBLEM.md) | Min-cost unbounded knapsack DP | Medium |
| 5 | [Longest Common Subsequence](problem-05-longest-common-subsequence/PROBLEM.md) | 2D grid DP over two sequences | Medium |
| 6 | [Edit Distance](problem-06-edit-distance/PROBLEM.md) | 2D DP with three transitions (insert/delete/replace) | Hard |
