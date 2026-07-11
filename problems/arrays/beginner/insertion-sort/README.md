# Insertion Sort

**Insertion Sort** builds a sorted region one element at a time. It keeps the left part of the
array sorted (initially just the first element) and, for each new element, "inserts" it into
its correct place within that sorted prefix by shifting the larger elements one slot to the
right. It is exactly how most people sort a hand of playing cards.

```
for i in 1 .. n-1:
    key = a[i]
    j = i - 1
    while j >= 0 and a[j] > key:   # shift bigger elements right
        a[j+1] = a[j]
        j -= 1
    a[j+1] = key                   # drop key into the gap
```

## When to reach for it

- **Small inputs.** Low overhead and no recursion make it faster than fancy `O(n log n)`
  sorts for tiny arrays (many library sorts fall back to insertion sort below ~16 elements).
- **Nearly-sorted / almost-sorted data.** This is insertion sort's superpower. If every
  element is at most `k` positions from its final spot, insertion sort runs in `O(n*k)` —
  close to linear when `k` is small. The inner `while` loop stops the instant it finds a
  smaller element, so already-ordered runs cost almost nothing.
- **Online / streaming sorting.** You can feed elements in one at a time and keep the prefix
  sorted at all times, without needing the whole input up front.
- **Stable sorting in place.** Uses `O(1)` extra memory and preserves the relative order of
  equal keys.

In production you would still call your language's built-in sort (Timsort, introsort, ...),
but Timsort itself *uses* insertion sort for its small runs — so this is not just a toy.

## Complexity

| Case    | Time      | Notes                                                        |
|---------|-----------|--------------------------------------------------------------|
| Best    | `O(n)`    | Already sorted: the inner loop never shifts, one pass total  |
| Average | `O(n^2)`  | Random order                                                 |
| Worst   | `O(n^2)`  | Reverse sorted: every element shifts all the way to the left |
| Space   | `O(1)`    | In-place, only a constant amount of extra memory             |

Insertion sort is **stable**: the inner loop shifts only on a strict `a[j] > key` comparison,
so an equal element never jumps in front of one that came before it. A useful side fact used
below: **the total number of shifts insertion sort performs equals the number of inversions**
in the input.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Sort an Array](problem-01-sort-an-array/PROBLEM.md) | Sort integers ascending with the classic insert-into-prefix loop | Easy |
| 2 | [Insertion Sort List](problem-02-insertion-sort-list/PROBLEM.md) | Run insertion sort on a singly linked list (LeetCode 147) | Medium |
| 3 | [Sort a K-Sorted Array](problem-03-sort-k-sorted-array/PROBLEM.md) | Sort a nearly-sorted array where each element is ≤ k from its place | Medium |
| 4 | [Binary Insertion Sort](problem-04-binary-insertion-sort/PROBLEM.md) | Use binary search to find each insertion point, cutting comparisons | Medium |
| 5 | [Insertion Sort Shift Count](problem-05-insertion-sort-shift-count/PROBLEM.md) | Count the total shifts insertion sort makes = inversion count | Hard |
