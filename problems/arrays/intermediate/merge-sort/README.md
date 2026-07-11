# Merge Sort

**Merge Sort** is a classic *divide-and-conquer* sorting algorithm. It works by
recursively splitting an array into two halves, sorting each half, and then
**merging** the two sorted halves back into one sorted sequence.

The merge step is the heart of the algorithm: given two already-sorted lists, it
walks a pointer through each and repeatedly emits the smaller front element,
producing a combined sorted list in linear time.

## Why reach for Merge Sort?

- You need a **guaranteed** `O(n log n)` sort regardless of the input
  distribution (unlike quicksort's `O(n^2)` worst case).
- You need a **stable** sort (equal elements keep their original relative order).
- You are sorting a **linked list** — merge sort needs no random access and is
  the natural choice (`O(1)` extra space for the list variant).
- You need to sort data that does not fit in memory (**external sort**) — merge
  sort streams sequentially and merges runs from disk.
- The merge routine itself is a reusable primitive: it powers algorithms that
  **count inversions**, count "smaller elements to the right", and find
  "reverse pairs" while sorting.

## Complexity

| Metric | Value |
|--------|-------|
| Time (best / average / worst) | `O(n log n)` |
| Space (array version) | `O(n)` auxiliary |
| Space (linked-list version) | `O(1)` auxiliary (+ `O(log n)` recursion) |
| Stable? | Yes |
| In-place? | No (standard array version) |

The recurrence is `T(n) = 2 T(n/2) + O(n)`, which by the Master Theorem solves to
`O(n log n)`: there are `log n` levels of recursion and each level does `O(n)`
total merging work.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Merge Sorted Array](problem-01-merge-sorted-array/PROBLEM.md) | Merge two sorted arrays in place — the merge subroutine itself | Easy |
| 2 | [Sort an Array](problem-02-sort-an-array/PROBLEM.md) | Sort an integer array from scratch — full merge sort | Medium |
| 3 | [Sort List](problem-03-sort-list/PROBLEM.md) | Sort a singly linked list in `O(n log n)` / `O(1)` space | Medium |
| 4 | [Count Inversions](problem-04-count-inversions/PROBLEM.md) | Count pairs out of order — piggyback on the merge step | Medium |
| 5 | [Count of Smaller Numbers After Self](problem-05-count-smaller-after-self/PROBLEM.md) | For each element, count smaller elements to its right | Hard |
| 6 | [Reverse Pairs](problem-06-reverse-pairs/PROBLEM.md) | Count pairs where `nums[i] > 2 * nums[j]` and `i < j` | Hard |
