# Selection Sort

**Selection Sort** is one of the simplest comparison-based sorting algorithms. It divides the
array into a **sorted prefix** (initially empty) and an **unsorted suffix** (initially the whole
array). On every pass it scans the unsorted suffix, finds the **minimum** element (or the maximum,
if sorting descending), and swaps it into the first slot of the suffix — thereby growing the sorted
prefix by one. After `n - 1` passes the array is fully sorted.

```
[ sorted prefix | unsorted suffix ]
                 ^ find the min of this region, swap it to the front of the region
```

## Why / when to reach for it

- **Teaching & intuition** — it is the most direct expression of "repeatedly take the smallest
  remaining item," which makes it a great first sorting algorithm.
- **Minimizing writes** — Selection Sort performs at most `n - 1` swaps (exactly one write of the
  chosen element per pass), far fewer than Bubble/Insertion sort. This matters when a *write* is
  vastly more expensive than a *comparison* (e.g. wearing out flash memory / EEPROM).
- **Partial sorting / selection** — if you only need the `k` smallest (or largest) elements, you can
  stop after `k` passes, giving an `O(n·k)` selection algorithm without sorting the whole array.
- **Tiny inputs** — for very small `n` its simplicity and lack of overhead can be perfectly fine.

Do **not** reach for it on large inputs where you actually need speed — its `O(n²)` comparison
count is dominated by `O(n log n)` sorts (merge/heap/quick sort).

## Complexity

| Metric              | Value                                                        |
|---------------------|--------------------------------------------------------------|
| Time (best)         | `O(n²)` — the min-scan runs regardless of existing order     |
| Time (average)      | `O(n²)`                                                       |
| Time (worst)        | `O(n²)`                                                       |
| Extra space         | `O(1)` — sorts in place                                      |
| Swaps / writes      | `O(n)` — at most `n - 1` swaps total                         |
| Stable?             | No (the standard in-place swap version is **not** stable)    |

## Core invariant

After the `i`-th pass, `arr[0 .. i]` holds the `i + 1` smallest elements of the array in sorted
order, and every element in `arr[0 .. i]` is `<=` every element in `arr[i+1 .. n-1]`.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Sort an Array](problem-01-sort-an-array/PROBLEM.md) | Sort an integer array ascending by implementing Selection Sort directly. | Easy |
| 2 | [Sort the People](problem-02-sort-the-people/PROBLEM.md) | Reorder names by their heights (descending) using selection sort over parallel arrays. | Easy |
| 3 | [Sort Characters By Frequency](problem-03-sort-characters-by-frequency/PROBLEM.md) | Rebuild a string with characters ordered by descending frequency (selection by a derived key). | Medium |
| 4 | [Kth Largest Element in an Array](problem-04-kth-largest-element/PROBLEM.md) | Return the k-th largest element using only `k` partial selection-sort passes. | Medium |
| 5 | [The K Weakest Rows in a Matrix](problem-05-k-weakest-rows/PROBLEM.md) | Return the indices of the k weakest rows via partial selection sort on a composite `(strength, index)` key. | Medium |

Each problem folder contains:

- `PROBLEM.md` — the full statement, constraints, and worked examples.
- `solution.py` — an **empty template** for you to implement.
- `SOLUTION.md` — the answer key with brute-force vs. Selection-Sort approaches and edge cases.
