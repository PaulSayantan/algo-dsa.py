# Heap / Priority Queue

**Category:** paradigms / paradigm

**One-line:** Retrieve the min or max element efficiently for top-k, scheduling, and merging problems.

## What is it?

A **heap** is a complete binary tree stored compactly in an array that maintains
the **heap property**: in a *min-heap* every parent is `<=` its children (so the
smallest element sits at the root); in a *max-heap* every parent is `>=` its
children (so the largest sits at the root). A **priority queue** is the abstract
data type "give me the highest-priority item next" — a heap is its standard,
fast implementation.

The magic is that a heap keeps *just enough* order to answer one question
instantly — "what is the current min/max?" — without paying the full cost of
sorting everything. Insertions and removals only fix a single root-to-leaf path,
so they cost `O(log n)` instead of `O(n)`.

In Python the `heapq` module gives you a **min-heap** over a plain list:
`heapq.heappush`, `heapq.heappop`, `heapq.heapify` (build in `O(n)`), and
`heapq.heappushpop` / `heapq.heapreplace` (one-shot push+pop). To get a
**max-heap**, push negated values (`-x`) or wrap items in a comparison key.

## When to reach for it

Look for these signals:

- **"Top k", "k largest/smallest", "k closest", "k most frequent"** — keep a
  heap of size `k` and stream everything through it.
- **"Kth largest/smallest"** — the boundary element of that size-`k` heap.
- **Repeatedly take the current best/worst** — scheduling, simulations like
  "smash the two heaviest stones", Huffman coding, Dijkstra / Prim.
- **Merging `k` sorted sequences** — a heap holds the current front of each
  sequence, always yielding the global minimum next.
- **Running median / two-ended balance** — two heaps (a max-heap for the low
  half, a min-heap for the high half) straddling the middle.

> Rule of thumb: if you find yourself wanting to *sort repeatedly* or *re-scan
> for the min/max* inside a loop, a heap usually turns that inner `O(n)` work
> into `O(log n)`.

## Typical complexity

| Operation | Cost |
|---|---|
| Peek min/max (`heap[0]`) | `O(1)` |
| Push | `O(log n)` |
| Pop min/max | `O(log n)` |
| Build heap from `n` items (`heapify`) | `O(n)` |
| Top-k of `n` items (size-`k` heap) | `O(n log k)` time, `O(k)` space |
| `k`-way merge of `n` total items | `O(n log k)` time, `O(k)` space |

A heap does **not** support fast search for an arbitrary element or ordered
traversal — for that reach for a balanced BST / sorted structure instead.

## Problems

| # | Problem | Technique | Difficulty |
|---|---------|-----------|------------|
| 1 | [Kth Largest Element in a Stream](problem-01-kth-largest-in-stream/PROBLEM.md) | Size-`k` min-heap tracks the running kth largest | Easy |
| 2 | [Last Stone Weight](problem-02-last-stone-weight/PROBLEM.md) | Max-heap simulation: repeatedly smash the two heaviest | Easy |
| 3 | [K Closest Points to Origin](problem-03-k-closest-points/PROBLEM.md) | Size-`k` max-heap keeps the `k` nearest points | Medium |
| 4 | [Top K Frequent Elements](problem-04-top-k-frequent-elements/PROBLEM.md) | Count, then heap-select the `k` most frequent | Medium |
| 5 | [Merge k Sorted Lists](problem-05-merge-k-sorted-lists/PROBLEM.md) | Min-heap over the `k` list heads for a `k`-way merge | Hard |
| 6 | [Find Median from Data Stream](problem-06-find-median-from-data-stream/PROBLEM.md) | Two balanced heaps straddling the middle | Hard |
