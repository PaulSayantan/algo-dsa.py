# Solution — Optimized Bubble Sort Passes

## Brute Force

Run **plain** bubble sort without the early-exit flag: always perform exactly `n - 1` passes,
then return `n - 1`. This "sorts" correctly but ignores the whole point of the problem — it
reports `n - 1` even for an already-sorted array, so it does not match the required pass count
for nearly-sorted inputs. It is `O(n^2)` time, `O(1)` space, and gives the wrong answer for the
examples (e.g., it would return `3` for `[1,2,3,4]` instead of `1`).

Use it only to see *why* the early-exit flag matters.

## Optimal Approach (Bubble Sort with early exit)

Maintain a `swapped` flag per pass. Count each pass you *start*, and stop only when a pass
completes with no swaps — that zero-swap pass is the "confirming" pass and it is counted too.

```python
def countPasses(self, arr: List[int]) -> int:
    n = len(arr)
    if n <= 1:
        return 1                 # one confirming pass over a trivially sorted array
    passes = 0
    while True:
        passes += 1
        swapped = False
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:          # a full pass with no swaps -> sorted, stop
            break
    return passes
```

**Why it is correct.**

- Correct sorting follows from the standard bubble-sort invariant: after pass `i`, the last `i`
  elements are the `i` largest, in place.
- **Termination / early exit.** If a full pass performs no swaps, then `arr[j] <= arr[j+1]` for
  every adjacent pair, which means the array is sorted — so stopping is safe. And since every
  swap-performing pass fixes at least one inversion, the number of such passes is finite, so the
  loop always reaches a zero-swap pass and terminates.
- **Pass counting.** We increment `passes` at the *start* of each sweep, so the final zero-swap
  sweep (the one that detects sortedness) is included, matching the problem's definition. On an
  already-sorted array the first pass finds nothing to swap and we stop after counting it → `1`.
  For `[4,3,2,1]` there are 3 swap-performing passes plus the 4th confirming pass → `4`.

**Note on the shrinking-bounds optimization.** A faster variant scans only `range(n - 1 - i)`
on pass `i`, since the last `i` elements are already in place. That is a valid *sorting*
optimization, but be careful: with shrinking bounds a reverse-sorted array is fully sorted
after the `(n-1)`-th swap-performing pass, and a separate confirming pass may not run. If you
use shrinking bounds and still want to count the confirming pass, keep an explicit final "no
swap detected" check. The full-width `while True` version above sidesteps that subtlety, which
is why it is used as the reference here.

- Time: `O(n^2)` worst/average; `O(n)` best case (already sorted → one pass).
- Space: `O(1)`.

## Key Insights & Edge Cases

- **Definition matters.** The tricky part is agreeing on whether the zero-swap detection pass
  counts. This problem says yes, so an already-sorted array returns `1`, and a length-1 array
  returns `1`.
- **Best case `O(n)`.** The early-exit flag is exactly what gives bubble sort its `O(n)`
  best-case time on sorted / nearly-sorted data.
- **Reverse-sorted** is the worst case: it requires the full number of swapping passes.
- **Careful with off-by-one** in the outer loop if you want the confirming pass counted; the
  `while True` form above makes the stopping condition explicit.
- Passes performed is `O(D)` where `D` is the largest distance any element must travel *left*;
  each pass moves an element at most one position left, which is another lens on why nearly-
  sorted data finishes quickly.
