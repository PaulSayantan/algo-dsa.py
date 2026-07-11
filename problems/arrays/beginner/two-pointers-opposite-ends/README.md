# Two Pointers (Opposite Ends)

## What it is

The **opposite-ends two-pointer** technique keeps two indices — one starting at
the **left** end of a sequence and one at the **right** end — and repeatedly
moves them **toward each other** until they meet (or cross). At every step you
inspect the pair `(arr[left], arr[right])` and use a simple rule to decide which
pointer to advance. Because each pointer only ever moves inward, the whole
sequence is scanned in a **single linear pass**.

This pattern turns many problems that look like they need a nested `O(n^2)`
double loop into an `O(n)` sweep. It shines when the data has some **monotonic
structure** you can exploit — most commonly a **sorted array** — because the
sortedness tells you *unambiguously* which end to move.

## When to reach for it

Reach for opposite-ends two pointers when you see any of these signals:

- The array is **sorted** (or can be sorted cheaply) and you need to find a
  **pair / triplet** meeting a sum or difference condition.
- You must compare or process an element from the **front against one from the
  back** — e.g. checking a **palindrome**, reversing in place.
- You want to **merge from both ends** toward the middle (e.g. sorting squares
  of a signed sorted array).
- You are computing an **area / width between two boundaries** and a greedy
  "move the limiting side" argument applies (Container With Most Water,
  Trapping Rain Water).

The core decision rule usually looks like: *if the current pair overshoots the
target, move `right` in; if it undershoots, move `left` in; if it matches,
record it.* The correctness always rests on an **invariant**: whatever you skip
by moving a pointer could never have produced a better/valid answer.

## Typical complexity

| Aspect | Cost |
|---|---|
| Time  | `O(n)` for a single pass (`O(n log n)` if you must sort first) |
| Space | `O(1)` extra (an output array, when required, is separate) |

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Valid Palindrome](problem-01-valid-palindrome/PROBLEM.md) | Compare front vs. back characters, skipping non-alphanumerics | Easy |
| 2 | [Two Sum II — Input Array Is Sorted](problem-02-two-sum-ii-input-array-is-sorted/PROBLEM.md) | Pair sum in a sorted array by shrinking the window | Easy |
| 3 | [Squares of a Sorted Array](problem-03-squares-of-a-sorted-array/PROBLEM.md) | Merge largest magnitudes from both ends into result | Easy |
| 4 | [Container With Most Water](problem-04-container-with-most-water/PROBLEM.md) | Greedily move the shorter wall to maximize area | Medium |
| 5 | [3Sum](problem-05-3sum/PROBLEM.md) | Sort, fix one element, two-pointer the rest | Medium |
| 6 | [Trapping Rain Water](problem-06-trapping-rain-water/PROBLEM.md) | Converge with running left/right maxima | Hard |
