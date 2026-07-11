# Quickselect

**Quickselect** is a selection algorithm that finds the k-th smallest (or largest)
element of an unordered list. It is the selection cousin of Quicksort: it uses the
same *partition* step, but after partitioning it only recurses into the **one** side
that must contain the answer, instead of both. This one-sided recursion is what turns
Quicksort's `O(n log n)` into Quickselect's **average `O(n)`**.

## The core idea

1. Pick a **pivot** and partition the array so that everything `<= pivot` sits to its
   left and everything `> pivot` sits to its right. After partitioning, the pivot is in
   its **final sorted position** `p`.
2. If `p` equals the target index `k`, you are done — `nums[p]` is the answer.
3. If `p > k`, the answer lies to the **left** of the pivot; recurse (or loop) on the
   left part only.
4. If `p < k`, the answer lies to the **right**; recurse on the right part only.

Because each step discards a chunk of the array and never revisits it, the expected
work is `n + n/2 + n/4 + ... ≈ 2n = O(n)`.

## When to reach for it

- You need the **k-th smallest / k-th largest** element, the **median**, or the
  **top-k / k-closest** items of an *unsorted* array.
- A full sort (`O(n log n)`) is more than you need, and you do **not** need the k items
  themselves to be sorted.
- You are allowed to **mutate / reorder** the input (Quickselect rearranges it in place).

If you need the answer in sorted order, need a streaming/online solution, or must avoid
worst-case blowups on adversarial input, a heap (`O(n log k)`) or
median-of-medians pivoting is often a better fit.

## Complexity

| Metric | Value |
|--------|-------|
| Time (average / expected) | `O(n)` |
| Time (worst case, bad pivots) | `O(n^2)` |
| Space (in-place, iterative) | `O(1)` |
| Space (recursive stack) | `O(log n)` expected |

The `O(n^2)` worst case (e.g. an already-sorted array with a naive last-element pivot)
is avoided in practice by choosing a **random pivot** (or median-of-three). With a
random pivot the expected time is `O(n)` regardless of input order.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Kth Largest Element in an Array](problem-01-kth-largest-element/PROBLEM.md) | Find the k-th largest value in an unsorted array. | Medium |
| 2 | [Median of an Unsorted Array](problem-02-median-of-unsorted-array/PROBLEM.md) | Compute the median without fully sorting the array. | Medium |
| 3 | [K Closest Points to Origin](problem-03-k-closest-points-to-origin/PROBLEM.md) | Return the k points nearest to the origin by Euclidean distance. | Medium |
| 4 | [Top K Frequent Elements](problem-04-top-k-frequent-elements/PROBLEM.md) | Return the k most frequently occurring elements. | Medium |
| 5 | [Wiggle Sort II](problem-05-wiggle-sort-ii/PROBLEM.md) | Reorder so that `nums[0] < nums[1] > nums[2] < ...` using the median. | Hard |
