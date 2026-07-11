# Heap Sort

**Heap Sort** is a comparison-based, in-place sorting algorithm built on the
**binary heap** data structure. The idea is two-phase:

1. **Build a heap** — rearrange the array so it satisfies the *max-heap*
   property (every parent `>=` its children). This is done bottom-up in
   `O(n)` time.
2. **Repeatedly extract the max** — the largest element sits at the root
   (index `0`). Swap it with the last element, shrink the heap by one, and
   *sift down* the new root to restore the heap property. Each extraction
   places one element into its final sorted position. After `n - 1`
   extractions the array is sorted ascending.

The heap lives inside the same array using implicit indexing: the children of
node `i` are at `2i + 1` and `2i + 2`, and the parent of node `i` is at
`(i - 1) // 2`. No extra arrays or pointers are needed.

## Why reach for Heap Sort (and heaps)?

- You need a **guaranteed `O(n log n)`** sort with **`O(1)` auxiliary space** —
  heap sort never degrades to `O(n^2)` (unlike naive quicksort) and needs no
  linear scratch buffer (unlike merge sort).
- You only need the **top / bottom `k`** elements, or the **k-th** element — a
  size-`k` heap answers these in `O(n log k)` without fully sorting.
- You need a **streaming priority structure** — insert and extract-min/max in
  `O(log n)` as data arrives (task schedulers, Dijkstra, event simulation,
  running medians).
- You need to **merge many sorted sequences** — a min-heap over the `k` current
  fronts repeatedly emits the global minimum.

The core primitives of heap sort — **`build_heap`** and **`sift_down`
(heapify)** — are exactly the operations every one of the problems below leans
on, whether you write the heap by hand or reach for `heapq`.

## Complexity

| Metric | Value |
|--------|-------|
| Time — build heap | `O(n)` |
| Time — full sort (best / average / worst) | `O(n log n)` |
| Space | `O(1)` auxiliary (in-place) |
| Stable? | No |
| In-place? | Yes |

`sift_down` costs `O(log n)` because a node can fall at most the height of the
tree. Building the heap is `O(n)` (a tighter bound than `n * log n` because most
nodes are near the bottom and barely move). The extraction phase does `n`
sift-downs, giving the `O(n log n)` total.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Sort an Array](problem-01-sort-an-array/PROBLEM.md) | Sort an integer array from scratch — full in-place heap sort | Medium |
| 2 | [Kth Largest Element in an Array](problem-02-kth-largest-element/PROBLEM.md) | Find the k-th largest value — partial heap sort with a size-`k` heap | Medium |
| 3 | [Top K Frequent Elements](problem-03-top-k-frequent-elements/PROBLEM.md) | Return the `k` most frequent values — heap keyed on frequency | Medium |
| 4 | [K Closest Points to Origin](problem-04-k-closest-points-to-origin/PROBLEM.md) | Return the `k` points nearest the origin — heap keyed on distance | Medium |
| 5 | [Merge k Sorted Lists](problem-05-merge-k-sorted-lists/PROBLEM.md) | Merge `k` sorted linked lists — min-heap over the current fronts | Hard |
| 6 | [Find Median from Data Stream](problem-06-find-median-from-data-stream/PROBLEM.md) | Maintain a running median — two balanced heaps | Hard |
