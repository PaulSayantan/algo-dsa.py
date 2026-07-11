# Solution — Sort a K-Sorted (Nearly Sorted) Array

## Brute Force

Ignore the `k`-sorted property and run any general comparison sort (e.g. Python's built-in
`sorted`, or plain insertion sort treating the array as arbitrary). This is correct but throws
away the structure that makes the problem easy.

- Time: `O(n log n)` with a library sort, or `O(n^2)` if the input happens to force full
  shifts in a naive sort.
- Space: `O(n)` for a library sort's temporary buffer (Timsort), or `O(1)` in place.

*(Note: the textbook heap-based solution using a min-heap of size `k+1` runs in
`O(n log k)`. That is asymptotically better for large `k`, but insertion sort wins in
constant factors and code simplicity when `k` is small, which is the point of this drill.)*

## Optimal Approach (Adaptive Insertion Sort)

Run ordinary insertion sort. The key observation is **why it is fast here**:

- In a `k`-sorted array, when we reach index `i`, the element `nums[i]` belongs somewhere in
  the window `[i-k, i]` of the already-sorted prefix (it started at most `k` slots from its
  final position).
- Therefore the inner `while` loop shifts `nums[i]` **at most `k` times** before finding its
  slot — the loop condition `nums[j] > key` fails within `k` steps.

So each of the `n` elements does `O(k)` work, for a total of `O(n * k)`.

```python
def sortKSortedArray(self, nums, k):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:   # runs at most k times on a k-sorted array
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums
```

**Why it is correct.** This is exactly insertion sort, whose correctness does not depend on
`k` at all: the loop invariant "`nums[0..i-1]` is sorted" holds after every iteration, so the
final array is fully sorted for *any* input. The `k`-sorted guarantee only bounds the running
time; it never affects correctness.

- Time: `O(n * k)` given the `k`-sorted guarantee (`O(n)` when `k` is a small constant).
  Degrades to `O(n^2)` if the guarantee is violated, but never becomes incorrect.
- Space: `O(1)` — in place.

## Key Insights & Edge Cases

- **Adaptive means "does less work on ordered input."** Insertion sort's inner loop halts the
  instant the element is in place; nearly-sorted input triggers almost no shifting. That
  property is what this problem is testing.
- **`k = 0`** means the array is already sorted: the inner loop never runs, one linear pass.
- **You don't need to know `k` to run the sort** — plain insertion sort already achieves
  `O(n*k)`. `k` is given so you can *reason about* the complexity (and choose insertion sort
  over a heap for small `k`).
- **Large `k` (close to `n`)** makes this `O(n^2)`; prefer the `O(n log k)` min-heap approach
  then. For small `k`, insertion sort's tiny constant factor usually wins.
- **Duplicates and negatives** need no special handling; the comparison logic is unchanged and
  the sort stays stable.
