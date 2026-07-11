# Solution — Bubble Sort Swap Count

## Brute Force

Define the answer directly as the **inversion count**: the number of index pairs `(i, j)` with
`i < j` and `arr[i] > arr[j]`. You can compute it with two nested loops that check every pair
and increment a counter. This does not even sort the array, but it produces the same number
that bubble sort would report.

- Time: `O(n^2)`
- Space: `O(1)`

This is a fine, correct baseline. The point of the problem, though, is to see that bubble
sort's swap count *is* this quantity.

## Optimal Approach (Bubble Sort)

Run bubble sort and increment a counter on every adjacent exchange.

```python
def countSwaps(self, arr: List[int]) -> int:
    n = len(arr)
    swaps = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return swaps
```

**Why the count equals the number of inversions.** A single adjacent swap exchanges two
neighbors that are out of order. That operation removes **exactly one** inversion (the pair
being swapped) and changes no other pair's relative order, because every other pair keeps the
same two elements on the same sides. A sorted array has zero inversions. Therefore the number
of swaps needed to reach the sorted array is exactly the initial inversion count — and bubble
sort only ever swaps out-of-order adjacent pairs, so it performs precisely that many swaps.

- Time: `O(n^2)`
- Space: `O(1)` — in place, plus one integer counter.

For much larger inputs you could count inversions in `O(n log n)` with a modified merge sort
or a Fenwick tree, but with `n <= 600` the direct bubble sort is more than fast enough and
matches the intent of the exercise.

## Key Insights & Edge Cases

- **Swap count is invariant** of *how* you bubble (left-to-right passes, shrinking bounds,
  early exit): any sequence of only-when-out-of-order adjacent swaps that sorts the array uses
  exactly `inversions` swaps.
- **Already sorted** input → `0` swaps.
- **Reverse sorted** input of length `n` → maximum swaps `n * (n - 1) / 2`.
- **Duplicates** contribute no inversion between themselves (we swap only on strict `>`), so
  equal elements are never counted against each other.
- Do not confuse *swaps* with *comparisons*: a full bubble sort always makes about
  `n^2 / 2` comparisons regardless of order; only the swap count varies.
