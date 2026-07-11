# Two Pointers

## What it is

The **Two Pointers** technique uses two index variables that move over a data
structure (usually an array or string) in a coordinated way. By letting the two
indices carry information about the region between them, you can often replace a
nested `O(n^2)` scan with a single `O(n)` sweep.

There are three common flavors:

1. **Opposite ends (converging).** Start one pointer at the far left and one at
   the far right, then move them toward each other. Works best on **sorted**
   data or on problems with a monotonic trade-off (Two Sum II, Container With
   Most Water, Valid Palindrome, 3Sum's inner loop).
2. **Same direction (fast / slow).** Both pointers start near the front; a
   `write`/`slow` pointer trails a `read`/`fast` pointer. Great for in-place
   filtering and de-duplication (Remove Duplicates from Sorted Array). The
   sliding-window pattern is a specialization of this.
3. **Two sequences.** One pointer per array, advanced independently (e.g.
   merging two sorted arrays).

## When to reach for it

- The array is **sorted** (or you can afford to sort it), and you need pairs /
  triples that satisfy a sum or difference condition.
- You must do an **in-place** transformation with `O(1)` extra space.
- A brute-force solution is `O(n^2)` because of a nested loop, but moving one
  boundary lets you *prove* that certain candidates can be skipped.
- You are checking a **symmetry** property (palindrome) or squeezing a region
  from both sides.

## Why it works

Each pointer moves in one direction and never backtracks, so together they take
at most `O(n)` steps. The key to correctness is an **invariant / exchange
argument**: whenever you advance a pointer you must be able to argue that no
optimal answer was discarded.

## Typical complexity

| Cost   | Value                                                    |
|--------|----------------------------------------------------------|
| Time   | `O(n)` after any required sort (`O(n log n)` with sort)  |
| Space  | `O(1)` extra (the pointers themselves)                   |

## Problems

| # | Problem | Pattern | Difficulty |
|---|---------|---------|------------|
| 1 | [Two Sum II - Input Array Is Sorted](problem-01-two-sum-ii-sorted/PROBLEM.md) | Find a pair summing to a target in a sorted array via converging ends | Medium |
| 2 | [Valid Palindrome](problem-02-valid-palindrome/PROBLEM.md) | Compare characters from both ends inward, skipping non-alphanumerics | Easy |
| 3 | [Remove Duplicates from Sorted Array](problem-03-remove-duplicates-sorted-array/PROBLEM.md) | Slow write pointer trails a fast read pointer for in-place compaction | Easy |
| 4 | [Container With Most Water](problem-04-container-with-most-water/PROBLEM.md) | Converging ends; always move the shorter wall inward | Medium |
| 5 | [3Sum](problem-05-3sum/PROBLEM.md) | Sort, fix one element, then two-pointer the remainder | Medium |
| 6 | [Trapping Rain Water](problem-06-trapping-rain-water/PROBLEM.md) | Converging ends driven by the smaller max-wall side | Hard |
