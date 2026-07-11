# Count Inversions (Merge Sort)

An **inversion** in an array is a pair of indices `(i, j)` with `i < j` and
`a[i] > a[j]` — i.e., two elements that are "out of order." Counting inversions
measures how far an array is from being sorted (a sorted-ascending array has 0
inversions; a strictly descending array has the maximum `n*(n-1)/2`).

The naive way to count them is to compare every pair — `O(n^2)`. The key idea of
this technique is to **piggyback the count onto merge sort**: while merging two
already-sorted halves, whenever we pick an element from the *right* half before
some remaining elements in the *left* half, every one of those remaining left
elements forms an inversion with it. Because the halves are sorted, we can add
all of them at once instead of comparing individually. This brings the cost down
to the merge-sort recurrence.

## When to reach for it

Reach for merge-sort inversion counting whenever you must count pairs `(i, j)`,
`i < j`, that satisfy an **order relation** between `a[i]` and `a[j]`
(`a[i] > a[j]`, `a[i] > 2*a[j]`, `a[i] <= a[j] + diff`, a prefix-sum falling in a
range, etc.). The family generalizes far beyond plain inversions: transform the
condition into a comparison on a derived array, then count "cross pairs" during
the merge. A Binary Indexed Tree / merge of a BST are alternative tools, but the
merge-sort approach is clean, cache-friendly, and needs no coordinate handling.

## Complexity

- **Time:** `O(n log n)` — the standard merge-sort recurrence `T(n) = 2T(n/2) + O(n)`.
- **Space:** `O(n)` for the temporary merge buffer (plus `O(log n)` recursion stack).

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Count Inversions in an Array](problem-01-count-inversions-in-an-array/PROBLEM.md) | Count all pairs `i<j` with `a[i]>a[j]` — the canonical inversion count | Medium |
| 2 | [Reverse Pairs](problem-02-reverse-pairs/PROBLEM.md) | Count pairs `i<j` with `a[i] > 2*a[j]` (LeetCode 493) | Hard |
| 3 | [Count of Smaller Numbers After Self](problem-03-count-smaller-after-self/PROBLEM.md) | For each element, count smaller elements to its right (LeetCode 315) | Hard |
| 4 | [Number of Pairs Satisfying Inequality](problem-04-pairs-satisfying-inequality/PROBLEM.md) | Count pairs where `d[i] <= d[j] + diff` on a derived array (LeetCode 2426) | Hard |
| 5 | [Count of Range Sum](problem-05-count-of-range-sum/PROBLEM.md) | Count subarray sums lying in `[lower, upper]` via prefix sums + merge (LeetCode 327) | Hard |
