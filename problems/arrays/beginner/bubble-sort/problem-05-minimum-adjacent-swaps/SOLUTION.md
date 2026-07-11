# Solution — Minimum Adjacent Swaps to Sort

## Brute Force

Count inversions directly with two nested loops: for every pair `(i, j)` with `i < j`,
increment a counter when `arr[i] > arr[j]`.

```python
def minAdjacentSwaps(self, arr: List[int]) -> int:
    n = len(arr)
    inv = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv += 1
    return inv
```

- Time: `O(n^2)`
- Space: `O(1)`

Correct and simple. It does not mutate the array and directly encodes the definition of the
answer.

## Optimal Approach (Bubble Sort, counting swaps)

Run bubble sort and count each adjacent exchange. The final count is the minimum number of
adjacent swaps.

```python
def minAdjacentSwaps(self, arr: List[int]) -> int:
    a = list(arr)                 # copy so we can mutate freely
    n = len(a)
    swaps = 0
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return swaps
```

**Why the minimum equals the inversion count.**

1. *A swap changes inversions by at most one.* Swapping two **adjacent** elements only affects
   the relative order of that one pair; every other pair keeps the same two elements on the
   same sides. So each adjacent swap changes the inversion count by exactly `+1` or `-1`.
2. *You must remove every inversion.* A sorted array has `0` inversions. Since each swap
   removes at most one inversion, you need **at least** `inversions` swaps — this is the lower
   bound.
3. *Bubble sort achieves it.* Bubble sort swaps **only** adjacent pairs that are out of order,
   and each such swap removes exactly one inversion (never creates one). Therefore it reaches
   the sorted array in exactly `inversions` swaps, meeting the lower bound. Hence the minimum
   is the inversion count, and bubble sort is optimal in *number of adjacent swaps*.

- Time: `O(n^2)` worst/average. With `n <= 2000` that is up to ~4M operations — fine.
- Space: `O(1)` (or `O(n)` if you copy the input to avoid mutating it).

**Scaling beyond this problem.** For large `n`, count inversions in `O(n log n)` using a
modified **merge sort** (add up the "cross" inversions during each merge) or a **Fenwick /
BIT** over compressed values. Both give the same number bubble sort would, just faster. Bubble
sort remains the conceptual bridge that explains *why* the answer is the inversion count.

## Key Insights & Edge Cases

- **Minimum, not just a count.** The lower-bound argument (each adjacent swap fixes at most one
  inversion) is what makes "inversion count" the *minimum*, not merely one achievable number.
- **Duplicates.** Equal elements are not inversions of each other (strict `>`), so `[3,2,3,1]`
  has 4 inversions, not 5 — the two `3`s do not count against each other.
- **Already sorted** → `0`. **Reverse sorted** length `n` → the maximum `n*(n-1)/2`.
- **Adjacent-only constraint is essential.** If arbitrary swaps were allowed, the minimum would
  instead be `n - (number of cycles)` in the permutation — a different problem. This problem's
  answer is the inversion count precisely because swaps are restricted to neighbors.
- **Overflow.** In languages with fixed-width integers, the count can reach ~2·10^6 here (fits
  in 32-bit), but for larger `n` use 64-bit. Python integers are unbounded, so no concern.
