# Top-K / K-Way Merge

A priority queue drives two staples: selecting the k best elements (a size-k heap) and merging k sorted lists (a heap of the current heads). In both, the heap always surfaces the next element to emit, giving O(n log k).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Merge k Sorted Lists](problem-01-merge-k-sorted-lists/PROBLEM.md) | Heap of list heads | Hard |
| 2 | [Find K Pairs with Smallest Sums](problem-02-k-smallest-pairs/PROBLEM.md) | Heap-guided pair expansion | Medium |
