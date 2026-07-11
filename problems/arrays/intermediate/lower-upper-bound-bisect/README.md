# Lower / Upper Bound (Bisect)

**Lower bound** and **upper bound** are two closely related binary-search primitives that
operate on a **sorted** array:

- **Lower bound** `lb(x)` = index of the **first** element that is `>= x`
  (equivalently, the leftmost position where `x` could be inserted while keeping the array sorted).
  This is Python's `bisect.bisect_left`.
- **Upper bound** `ub(x)` = index of the **first** element that is `> x`
  (the rightmost/last position where `x` could be inserted). This is Python's `bisect.bisect_right`.

Both return a value in the range `[0, n]` (an index one past the end means "no such element").

## Why they matter

Almost every "search a sorted array" question reduces to one of these two calls plus a tiny bit
of arithmetic:

| Query | Answer |
|-------|--------|
| Does `x` exist? | `lb(x) < n and a[lb(x)] == x` |
| First index `>= x` | `lb(x)` |
| First index `> x` | `ub(x)` |
| Last index `<= x` (floor) | `ub(x) - 1` |
| Last index `< x` (strict floor) | `lb(x) - 1` |
| Count of elements `== x` | `ub(x) - lb(x)` |
| Count of elements `< x` | `lb(x)` |
| Insertion point (keep sorted) | `lb(x)` or `ub(x)` |

## When to reach for it

- The data (or a monotonic transformation of it) is **sorted**.
- You need a **boundary**: "first thing that satisfies P", "how many are below the line",
  "closest value not exceeding t", counting duplicates, or an insertion index.
- You are maintaining a sorted structure incrementally (e.g. the `tails` array in the
  patience-sorting solution to Longest Increasing Subsequence).

## Complexity

- **Time:** `O(log n)` per query on an array of length `n`.
- **Space:** `O(1)` extra (iterative implementation).

## The canonical implementations

```python
def lower_bound(a, x):          # first index i with a[i] >= x
    lo, hi = 0, len(a)          # search space is [0, n], hi is exclusive
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:          # mid is too small -> answer is to the right
            lo = mid + 1
        else:                   # a[mid] >= x -> mid is a candidate, keep it
            hi = mid
    return lo

def upper_bound(a, x):          # first index i with a[i] > x
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] <= x:         # note the <= : the only difference from lower_bound
            lo = mid + 1
        else:
            hi = mid
    return lo
```

The **only** difference between the two is `<` vs `<=` in the comparison. Internalize the loop
invariant: everything in `[0, lo)` is strictly below the boundary and everything in `[hi, n)` is
at or above it; the loop shrinks `[lo, hi)` until it is empty, and `lo == hi` is the answer.

## Problems

| # | Problem | Technique | Difficulty |
|---|---------|-----------|------------|
| 1 | [Search Insert Position](problem-01-search-insert-position/PROBLEM.md) | Pure lower bound (insertion index) | Easy |
| 2 | [Find Smallest Letter Greater Than Target](problem-02-smallest-letter-greater-than-target/PROBLEM.md) | Pure upper bound with wraparound | Easy |
| 3 | [Find First and Last Position of Element](problem-03-first-and-last-position/PROBLEM.md) | Lower bound + upper bound together | Medium |
| 4 | [Time Based Key-Value Store](problem-04-time-based-key-value-store/PROBLEM.md) | Predecessor / floor query (`ub - 1`) | Medium |
| 5 | [Longest Increasing Subsequence](problem-05-longest-increasing-subsequence/PROBLEM.md) | Lower bound inside patience sorting | Medium |
