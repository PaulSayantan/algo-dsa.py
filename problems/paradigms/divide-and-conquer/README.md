# Divide and Conquer

**Category:** paradigms / paradigm

**One-line:** Split into subproblems, solve recursively, combine.

## What is it?

**Divide and Conquer (D&C)** solves a problem by breaking it into smaller,
*independent* instances of the same problem, solving those recursively, and then
**combining** their answers into a solution for the original. Three phases:

1. **Divide** — split the input into two or more subproblems (usually halves).
2. **Conquer** — solve each subproblem recursively; the base case is a piece small
   enough to answer directly.
3. **Combine** — merge the sub-answers into the answer for the whole.

The paradigm powers merge sort, quicksort/quickselect, binary search, FFT, Karatsuba
multiplication, closest-pair-of-points, and many geometry and counting algorithms.
The *art* is almost always in the **combine** step: dividing is trivial, but merging
sub-answers correctly and cheaply is what makes the algorithm fast (or even possible).

## When to reach for it

Look for these signals:

- The problem is naturally **self-similar**: the answer for a range can be built from
  the answers for its left and right halves.
- Subproblems are **independent** (no shared mutable state between them). When
  subproblems *overlap* and get recomputed, you want dynamic programming instead.
- A cheap **combine** exists — you can stitch two sub-answers together in linear (or
  better) time. Merge sort's `O(n)` merge is the archetype.
- You need to beat a quadratic brute force and the input has a **linear/geometric
  ordering** (an array to split, a set of points to partition by a median line).

## How to analyze the running time

D&C recurrences fit the pattern `T(n) = a·T(n/b) + f(n)` — `a` subproblems, each of
size `n/b`, plus `f(n)` to divide and combine. The **Master Theorem** reads off the
answer by comparing `f(n)` to `n^(log_b a)`:

- Merge sort: `T(n) = 2T(n/2) + O(n)` → `O(n log n)`.
- Binary search: `T(n) = T(n/2) + O(1)` → `O(log n)`.
- Karatsuba: `T(n) = 3T(n/2) + O(n)` → `O(n^1.585)`.

## Typical complexity

- **Time:** frequently `O(n log n)` (balanced split + linear combine), but ranges
  from `O(log n)` (binary search) to `O(n^2)`/worse when the combine or the split is
  expensive. Average-case quickselect is `O(n)`.
- **Space:** `O(log n)` recursion stack for a balanced split, plus whatever the
  combine buffers need (merge sort uses `O(n)` scratch space).

> Watch out: an *unbalanced* split can degrade the recurrence (quicksort's `O(n^2)`
> worst case). And D&C only helps when subproblems don't overlap — otherwise reach for
> DP so you don't recompute the same subproblem exponentially many times.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Majority Element](problem-01-majority-element/PROBLEM.md) | Majority of a range from majorities of its halves | Easy |
| 2 | [Sort an Array](problem-02-sort-an-array/PROBLEM.md) | Merge sort: split, sort halves, linear merge | Medium |
| 3 | [Maximum Subarray](problem-03-maximum-subarray/PROBLEM.md) | Best subarray is left, right, or crosses the midpoint | Medium |
| 4 | [Kth Largest Element in an Array](problem-04-kth-largest-element/PROBLEM.md) | Quickselect: partition and recurse into one side | Medium |
| 5 | [Count of Smaller Numbers After Self](problem-05-count-smaller-after-self/PROBLEM.md) | Count inversions during a merge-sort merge | Hard |
| 6 | [The Skyline Problem](problem-06-the-skyline-problem/PROBLEM.md) | Recursively build and merge two half-skylines | Hard |
