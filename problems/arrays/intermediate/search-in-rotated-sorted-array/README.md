# Search in Rotated Sorted Array

**Category:** arrays / intermediate

## What it is

A *rotated sorted array* is an array that was originally sorted in ascending
order and then rotated at some unknown pivot index `k`. For example the sorted
array `[0,1,2,4,5,6,7]` rotated 4 times becomes `[4,5,6,7,0,1,2]`. The array is
no longer globally sorted, but it is composed of **two sorted runs** joined at
the pivot (the location of the minimum element).

"Search in Rotated Sorted Array" is a family of techniques built on a single
idea: even though the array is rotated, at every step of a binary search **at
least one of the two halves `[lo..mid]` and `[mid..hi]` is still perfectly
sorted**. By comparing `nums[mid]` with an endpoint (`nums[lo]` or `nums[hi]`)
you can tell which half is sorted, then decide in `O(1)` whether the value you
want lies inside that sorted half or in the other half — and discard half the
array each iteration.

## When to reach for it

- The input is (or was) sorted, but shifted/rotated by an unknown amount.
- You need `O(log n)` lookup, minimum, or pivot detection and a plain
  `bisect` won't work because the array isn't monotonic end-to-end.
- Signals in the prompt: "rotated at an unknown pivot", "sorted and then
  rotated", "find the minimum / the number of rotations", "search for a target
  in `O(log n)`".

## Typical complexity

| Case | Time | Space |
|------|------|-------|
| Distinct elements | `O(log n)` | `O(1)` |
| Elements may repeat | `O(log n)` average, `O(n)` worst case | `O(1)` |

Duplicates break the "which half is sorted" test when `nums[lo] == nums[mid] ==
nums[hi]`; the only safe recovery is to shrink the window by one, which degrades
the worst case to linear.

## Core invariant

Maintain a window `[lo, hi]` that is guaranteed to still contain the answer.
Each step:

1. `mid = (lo + hi) // 2`.
2. Determine which side of `mid` is sorted using an endpoint comparison.
3. If the target/answer is provably inside the sorted side, keep that side;
   otherwise keep the other side.

The window shrinks every iteration, so the loop runs `O(log n)` times when all
elements are distinct.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Find Minimum in Rotated Sorted Array](problem-01-find-minimum-in-rotated-sorted-array/PROBLEM.md) | Locate the pivot (minimum value) of a rotated array of distinct numbers | Medium |
| 2 | [Search in Rotated Sorted Array](problem-02-search-in-rotated-sorted-array/PROBLEM.md) | Return the index of a target (or -1) in one modified binary search | Medium |
| 3 | [Find Rotation Count](problem-03-find-rotation-count/PROBLEM.md) | Count how many times a sorted array was rotated (index of the minimum) | Medium |
| 4 | [Search in Rotated Sorted Array II](problem-04-search-in-rotated-sorted-array-with-duplicates/PROBLEM.md) | Decide if a target exists when duplicates are allowed | Medium |
| 5 | [Find Minimum in Rotated Sorted Array II](problem-05-find-minimum-in-rotated-sorted-array-with-duplicates/PROBLEM.md) | Find the minimum when duplicates are allowed (worst case O(n)) | Hard |
