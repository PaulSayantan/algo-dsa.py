# Quick Sort

**Quick Sort** is a divide-and-conquer sorting algorithm. It picks an element as a
**pivot** and **partitions** the array so that every element smaller than the pivot
ends up to its left and every element larger ends up to its right. The pivot is now
in its final sorted position. The algorithm then recurses on the left and right
sub-arrays.

The heart of Quick Sort is the **partition** subroutine, and that subroutine — not
the full sort — is what most interview problems in this folder actually exercise:

- **Sorting**: run partition recursively on both halves (classic Quick Sort).
- **Selection (Quickselect)**: recurse on only *one* side to find the k-th
  smallest/largest element in **average O(n)** time.
- **3-way partition (Dutch National Flag)**: split into `< pivot`, `== pivot`,
  `> pivot` to handle many duplicate keys efficiently.

## When to reach for it

- You need an **in-place**, cache-friendly comparison sort with no extra array.
- You need only the **k-th order statistic** or the **top-k** elements — Quickselect
  beats a full sort (O(n) average vs O(n log n)).
- You need to rearrange around a threshold (partition) rather than fully sort.

Prefer Merge Sort or a heap when you need **guaranteed** O(n log n) or **stability**;
Quick Sort is not stable and its naive form degrades to O(n^2) on adversarial input.

## Complexity

| Aspect              | Quick Sort            | Quickselect          |
|---------------------|-----------------------|----------------------|
| Time (average)      | O(n log n)            | O(n)                 |
| Time (worst case)   | O(n^2)                | O(n^2)               |
| Space (auxiliary)   | O(log n) stack avg    | O(1) iterative / O(log n) |
| Stable?             | No                    | N/A                  |
| In-place?           | Yes                   | Yes                  |

The worst case (already-sorted input with a fixed end pivot) is avoided in practice
by choosing a **random** or **median-of-three** pivot.

## Problems

| # | Problem | Technique | Difficulty |
|---|---------|-----------|------------|
| 1 | [Sort an Array](problem-01-sort-an-array/PROBLEM.md) | Classic recursive Quick Sort | Medium |
| 2 | [Sort Colors](problem-02-sort-colors/PROBLEM.md) | 3-way partition (Dutch National Flag) | Medium |
| 3 | [Kth Largest Element in an Array](problem-03-kth-largest-element/PROBLEM.md) | Quickselect | Medium |
| 4 | [K Closest Points to Origin](problem-04-k-closest-points-to-origin/PROBLEM.md) | Quickselect on distance | Medium |
| 5 | [Top K Frequent Elements](problem-05-top-k-frequent-elements/PROBLEM.md) | Quickselect on frequency | Medium |
| 6 | [Wiggle Sort II](problem-06-wiggle-sort-ii/PROBLEM.md) | Quickselect (median) + 3-way partition | Hard |
