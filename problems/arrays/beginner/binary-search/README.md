# Binary Search

**Binary Search** is a divide-and-conquer search technique that finds a target
value inside a **sorted** search space by repeatedly halving the range of
candidates. On each step it inspects the middle element, decides whether the
answer lies in the left half or the right half, and discards the other half.
Because the search space shrinks by a constant factor (½) every iteration, it
runs in **O(log n)** time.

## When to reach for it

- The data is **sorted** (or can be sorted / is monotonic in some property).
- You can answer, in O(1) or cheap time, the question *"is the answer at or to
  one side of this midpoint?"* — i.e. there is a **monotonic predicate**.
- You need a value, an index, a boundary (first/last occurrence), or the
  smallest/largest value satisfying a condition.

The last point is the powerful generalization: **"binary search on the answer"**.
Even when the input array itself is not the thing being searched, if a candidate
answer `x` has a monotonic yes/no property (`feasible(x)` is false, false, ...,
true, true), you can binary search over the range of possible answers.

## Complexity

| Aspect | Cost |
| --- | --- |
| Time | **O(log n)** for a plain array search; **O(n log(range))** for "binary search on answer" where each feasibility check is O(n) |
| Space | **O(1)** iterative; O(log n) if written recursively (call stack) |

## The two canonical templates

```text
# 1) Exact-match search on [lo, hi] (inclusive)
lo, hi = 0, n - 1
while lo <= hi:
    mid = lo + (hi - lo) // 2
    if a[mid] == target: return mid
    if a[mid] < target:  lo = mid + 1
    else:                hi = mid - 1
return -1

# 2) Boundary / "lower_bound" search on [lo, hi) (half-open)
lo, hi = 0, n
while lo < hi:
    mid = lo + (hi - lo) // 2
    if feasible(mid): hi = mid       # keep mid, search left
    else:             lo = mid + 1   # discard mid, search right
return lo   # first index where feasible is true
```

The two biggest sources of bugs are (1) the loop condition (`<=` vs `<`) not
matching the interval convention (inclusive vs half-open), and (2) an update
that fails to shrink the interval, causing an infinite loop. Pick one template
and stay consistent.

## Problems

| # | Problem | Summary | Difficulty |
| --- | --- | --- | --- |
| 1 | [Binary Search](problem-01-binary-search/PROBLEM.md) | Return the index of a target in a sorted array, else -1 | Easy |
| 2 | [Search Insert Position](problem-02-search-insert-position/PROBLEM.md) | Find where a target is, or where it would be inserted | Easy |
| 3 | [First and Last Position](problem-03-first-and-last-position/PROBLEM.md) | Find the start and end indices of a target with duplicates | Medium |
| 4 | [Find Peak Element](problem-04-find-peak-element/PROBLEM.md) | Locate any peak in O(log n) using a monotonic slope test | Medium |
| 5 | [Search in Rotated Sorted Array](problem-05-search-rotated-sorted-array/PROBLEM.md) | Search a sorted array that was rotated at an unknown pivot | Medium |
| 6 | [Koko Eating Bananas](problem-06-koko-eating-bananas/PROBLEM.md) | Binary search on the answer to find the minimum feasible speed | Medium |
