# Bubble Sort

**Bubble Sort** is one of the simplest comparison-based sorting algorithms. It repeatedly
walks through the list, compares each pair of **adjacent** elements, and swaps them if they
are in the wrong order. After each full pass the largest remaining element "bubbles up" to
its correct position at the end, so the sorted region grows by one on every pass.

```
for pass in 0 .. n-1:
    for j in 0 .. n-2-pass:
        if a[j] > a[j+1]:
            swap(a[j], a[j+1])
```

## When to reach for it

- **Teaching / learning.** It is the canonical first sorting algorithm because the invariant
  ("after pass `k`, the last `k` elements are the `k` largest, in place") is easy to see.
- **Tiny inputs** (a handful of elements) where code simplicity matters more than speed.
- **Nearly-sorted data** with the early-exit optimization: if a whole pass makes zero swaps,
  the array is already sorted and we can stop. This makes best-case behavior `O(n)`.
- **Counting adjacent swaps / inversions.** The number of swaps a plain bubble sort performs
  is exactly the number of inversions in the array — a fact several problems below exploit.

In real production code you would use your language's built-in sort (Timsort, introsort,
etc.). Bubble sort is almost never the right *practical* choice, but understanding it builds
intuition for stability, in-place sorting, and swap-counting.

## Complexity

| Case    | Time      | Notes                                            |
|---------|-----------|--------------------------------------------------|
| Best    | `O(n)`    | Already sorted, *with* the early-exit flag       |
| Average | `O(n^2)`  | Random order                                     |
| Worst   | `O(n^2)`  | Reverse sorted                                   |
| Space   | `O(1)`    | In-place, only a constant amount of extra memory |

Bubble sort is **stable**: equal elements keep their original relative order because we only
swap on a strict `>` comparison.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Sort an Array](problem-01-sort-an-array/PROBLEM.md) | Sort integers ascending with the plain bubble sort loop | Easy |
| 2 | [Bubble Sort Swap Count](problem-02-bubble-sort-swap-count/PROBLEM.md) | Count how many adjacent swaps a full bubble sort performs | Easy |
| 3 | [Optimized Bubble Sort Passes](problem-03-optimized-bubble-sort-passes/PROBLEM.md) | Use the early-exit flag; return the number of passes until sorted | Medium |
| 4 | [Sort the People](problem-04-sort-the-people/PROBLEM.md) | Sort names by height (descending) by bubbling paired keys | Medium |
| 5 | [Minimum Adjacent Swaps to Sort](problem-05-minimum-adjacent-swaps/PROBLEM.md) | Count minimum adjacent swaps to sort = inversion count | Hard |
