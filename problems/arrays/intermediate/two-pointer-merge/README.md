# Two-Pointer Merge

## What it is

The **Two-Pointer Merge** is the linear-time procedure that combines two (or more)
*already sorted* sequences into a single sorted sequence. It is the "conquer" step
of merge sort, but it shows up on its own in a large family of problems.

The core idea: keep one index (pointer) into each input sequence. Repeatedly compare
the two elements the pointers currently reference, emit the smaller one, and advance
only the pointer that produced it. When one sequence is exhausted, flush whatever
remains in the other. Because every comparison advances at least one pointer and each
pointer only moves forward, the whole scan is `O(m + n)`.

```
i -> A: [1, 3, 5]
j -> B: [2, 4, 6]
compare A[i] vs B[j], take the smaller, advance that pointer, repeat.
```

## When to reach for it

- You have **two or more inputs that are already sorted** (arrays, linked lists,
  interval lists) and want to combine, intersect, or diff them.
- You want to avoid the `O(n log n)` cost of concatenate-then-sort by exploiting the
  existing order.
- A variant: two pointers walking **inward from both ends** of one sorted array, which
  is itself a merge of the array's "negative half" and "positive half" (e.g. squaring a
  sorted array).

## Complexity

| Aspect | Cost |
| --- | --- |
| Time  | `O(m + n)` for two inputs (`O(N log k)` when merging `k` inputs pairwise / with a heap) |
| Space | `O(1)` extra when merging in place; `O(m + n)` when a fresh output buffer is required |

The merge is **stable**: on ties you can break toward the first input to preserve
relative order, which matters when merge sort must stay stable.

## Problems

| # | Problem | Technique focus | Difficulty |
| --- | --- | --- | --- |
| 1 | [Merge Sorted Array](problem-01-merge-sorted-array/PROBLEM.md) | Canonical in-place merge, filling from the back | Easy |
| 2 | [Merge Two Sorted Lists](problem-02-merge-two-sorted-lists/PROBLEM.md) | Same merge on linked lists using a dummy head | Easy |
| 3 | [Squares of a Sorted Array](problem-03-squares-of-a-sorted-array/PROBLEM.md) | Two pointers inward from both ends | Easy |
| 4 | [Intersection of Two Arrays II](problem-04-intersection-of-two-arrays-ii/PROBLEM.md) | Merge walk that emits only matches | Easy |
| 5 | [Interval List Intersections](problem-05-interval-list-intersections/PROBLEM.md) | Merge two sorted interval lists, advancing the one that ends first | Medium |
| 6 | [Merge k Sorted Lists](problem-06-merge-k-sorted-lists/PROBLEM.md) | Repeated / divide-and-conquer pairwise merge | Hard |
