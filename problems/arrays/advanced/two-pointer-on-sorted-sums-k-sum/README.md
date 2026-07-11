# Two-Pointer on Sorted Sums (k-Sum)

## What it is

The **k-Sum two-pointer** family solves problems of the form *"find / count / optimize
k array elements whose sum equals (or is closest to, or stays under) a target."*

The core idea is a reduction:

1. **Sort** the array once.
2. Solve **2-Sum on a sorted array in O(n)** with two pointers `lo` and `hi`
   starting at the two ends. Because the array is sorted, the current sum
   `nums[lo] + nums[hi]` tells you exactly which way to move:
   - sum too small  -> move `lo` right (increase the sum),
   - sum too large  -> move `hi` left  (decrease the sum),
   - sum just right  -> record it, then step both inward.
3. Solve **k-Sum** by **fixing the outer `k - 2` indices with nested loops** and
   running the O(n) two-pointer scan on the remaining suffix. Sorting also makes
   **duplicate skipping** trivial (equal neighbors sit next to each other).

## When to reach for it

- The problem asks for **pairs / triplets / quadruplets** matching a numeric target.
- You need **all unique combinations**, a **count**, a **closest sum**, or a
  **best sum under a bound** — the sorted two-pointer scan handles all four shapes.
- Order of the output does **not** matter (you are free to sort), and you want to
  beat the naive O(n^k) brute force **without** the extra memory of a hash set,
  or you need de-duplication that hashing makes awkward.

If you must preserve original indices for a single pair and no de-duplication is
needed, a hash map (classic Two Sum) is often simpler; two-pointer shines once the
array is (or can be) sorted and k grows beyond 2.

## Typical complexity

- Sorting: **O(n log n)**.
- 2-Sum scan: **O(n)**.
- k-Sum: **O(n^(k-1))** time (the two-pointer scan removes one factor of `n`
  versus the O(n^k) brute force), and **O(1)** extra space beyond the output and
  the space used by sorting.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Two Sum II - Input Array Is Sorted](problem-01-two-sum-ii-sorted/PROBLEM.md) | Base 2-pointer scan on an already-sorted array | Medium |
| 2 | [Two Sum Less Than K](problem-02-two-sum-less-than-k/PROBLEM.md) | Two-pointer to maximize a sum under a bound | Easy |
| 3 | [3Sum Smaller](problem-03-three-sum-smaller/PROBLEM.md) | Fix one index + two-pointer **counting** | Medium |
| 4 | [3Sum](problem-04-three-sum/PROBLEM.md) | Fix one index + two-pointer with de-duplication | Medium |
| 5 | [3Sum Closest](problem-05-three-sum-closest/PROBLEM.md) | Fix one index + two-pointer tracking the closest sum | Medium |
| 6 | [4Sum](problem-06-four-sum/PROBLEM.md) | Fix two indices + two-pointer (general k-Sum) | Medium |
