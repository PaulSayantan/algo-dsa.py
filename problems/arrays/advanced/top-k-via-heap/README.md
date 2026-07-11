# Top-K via Heap

**Top-K** problems ask you to find the `k` "best" elements out of `n` — the `k` largest, `k` smallest, `k` most frequent, or `k` closest — **without fully sorting** the input.

## Core idea

To find the **k largest** elements, maintain a **min-heap of size k**:

1. Push elements one at a time.
2. Whenever the heap grows beyond size `k`, pop the **smallest** element.
3. After processing everything, the heap holds exactly the `k` largest elements, and its root is the `k`-th largest.

The trick is counter-intuitive: to keep the *largest* `k`, you use a **min**-heap so the current weakest survivor sits at the root and is the first to be evicted. Symmetrically, use a **max-heap of size k** for the *k smallest*.

For **frequency / distance / pair** variants you heapify on a key (a count, a squared distance, a pair sum) rather than the raw value.

## When to reach for it

- You need `k` extremes but `k << n`, so sorting all `n` is wasteful.
- The data is a **stream** and you cannot re-sort on every insert.
- You need "top / bottom / closest / most-frequent `k`" and the relative order among the other `n - k` elements does not matter.

## Complexity

| Approach | Time | Space |
|---|---|---|
| Sort everything | `O(n log n)` | `O(n)` (or `O(1)` in place) |
| **Size-k heap** | `O(n log k)` | `O(k)` |
| Quickselect (unordered k) | `O(n)` average, `O(n^2)` worst | `O(1)` extra |
| Bucket sort by frequency | `O(n)` | `O(n)` |

The size-`k` heap wins whenever `k` is much smaller than `n`, since `log k << log n`, and it uses only `O(k)` memory — essential for streams.

## Alternatives worth knowing

- **Quickselect** — an `O(n)`-average partition-based selection when you only need the `k` elements as an unordered set (not sorted) and have the whole array in memory.
- **Bucket sort** — an `O(n)` approach when the key (e.g. a frequency count) is bounded by `n`, so you can index directly into buckets.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Kth Largest Element in a Stream](problem-01-kth-largest-in-a-stream/PROBLEM.md) | Streaming size-k min-heap | Easy |
| 2 | [Kth Largest Element in an Array](problem-02-kth-largest-in-an-array/PROBLEM.md) | Size-k heap vs. Quickselect | Medium |
| 3 | [Top K Frequent Elements](problem-03-top-k-frequent-elements/PROBLEM.md) | Heap on frequency / bucket sort | Medium |
| 4 | [K Closest Points to Origin](problem-04-k-closest-points-to-origin/PROBLEM.md) | Max-heap on squared distance | Medium |
| 5 | [Top K Frequent Words](problem-05-top-k-frequent-words/PROBLEM.md) | Heap with custom tie-break | Medium |
| 6 | [Find K Pairs with Smallest Sums](problem-06-k-pairs-with-smallest-sums/PROBLEM.md) | Heap over a sorted-matrix frontier | Hard |
