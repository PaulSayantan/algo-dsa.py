# Sort an Array — Solution

## Brute Force

A quadratic comparison sort such as insertion sort or selection sort:

- Repeatedly find/insert the next element into its correct place.
- **Time:** O(n^2). **Space:** O(1).

Correct but far too slow for `n` up to `5 * 10^4` (about `2.5 * 10^9` operations in the worst
case). LeetCode 912 will time out on these.

A deterministic **fixed-pivot quicksort** (always pivot on the first/last element) is
O(n log n) on average but has a genuine **O(n^2)** worst case on sorted, reverse-sorted, or
all-equal inputs — precisely the adversarial cases the problem hints at.

## Optimal Approach (Randomization: quicksort with a random pivot)

Quicksort divides the array around a pivot so that everything left of the pivot is `<=` it and
everything right is `>=` it, then recursively sorts the two sides. The fix that makes it
robust is choosing the **pivot uniformly at random** on every call.

### Two-way partition version

```python
import random

def sortArray(self, nums):
    self._quicksort(nums, 0, len(nums) - 1)
    return nums

def _quicksort(self, a, lo, hi):
    while lo < hi:
        p = self._partition(a, lo, hi)
        # Recurse into the smaller side, loop on the larger -> O(log n) stack.
        if p - lo < hi - p:
            self._quicksort(a, lo, p - 1)
            lo = p + 1
        else:
            self._quicksort(a, p + 1, hi)
            hi = p - 1

def _partition(self, a, lo, hi):
    r = random.randint(lo, hi)          # random pivot
    a[r], a[hi] = a[hi], a[r]
    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    return i
```

### Three-way (Dutch national flag) version — best for many duplicates

With lots of equal keys (e.g. `[3, 3, 3]`), two-way partitioning still does redundant work.
Three-way partitioning groups elements into `< pivot`, `== pivot`, and `> pivot`, and recurses
only on the outer two groups — every element equal to the pivot is placed in one pass:

```python
def _quicksort3(self, a, lo, hi):
    if lo >= hi:
        return
    pivot = a[random.randint(lo, hi)]   # random pivot value
    lt, i, gt = lo, lo, hi
    while i <= gt:
        if a[i] < pivot:
            a[lt], a[i] = a[i], a[lt]; lt += 1; i += 1
        elif a[i] > pivot:
            a[i], a[gt] = a[gt], a[i]; gt -= 1
        else:
            i += 1
    self._quicksort3(a, lo, lt - 1)
    self._quicksort3(a, gt + 1, hi)
```

After the loop, `a[lt..gt]` all equal the pivot and are already in final position.

### Why the random pivot matters

A fixed pivot lets an adversary (or naturally sorted data) force maximally unbalanced splits
of sizes `n-1, n-2, ...`, giving O(n^2). Picking the pivot uniformly at random makes the
split independent of input order: the probability that any two specific elements are compared
is `2/(j - i + 1)` over their sorted-rank gap, and summing these expectations (linearity of
expectation) gives an expected comparison count of `2n ln n = O(n log n)` — regardless of the
input. No fixed input can reliably trigger the worst case.

### Complexity

- **Time:** O(n log n) expected; O(n^2) worst case with vanishingly small probability.
- **Space:** O(log n) expected recursion depth when you recurse into the smaller side and
  loop on the larger (as above). Naive recursion into both sides is O(n) stack in the worst
  case.
- Three-way partitioning additionally gives **O(n)** behavior on inputs with O(1) distinct
  keys (like all-equal), because equal elements are handled in a single partition pass.

## Key Insights & Edge Cases

- **Random pivot is the whole point.** Without it, sorted / reverse-sorted / all-equal inputs
  degrade to O(n^2). LeetCode 912 specifically stresses these; a fixed-pivot quicksort can TLE
  or blow the recursion limit.
- **Duplicates:** two-way partitioning is correct with duplicates but can be slow when they
  dominate; **three-way partitioning** is the idiomatic fix and makes `[3, 3, 3]` O(n).
- **Recursion depth:** recurse into the *smaller* partition and iterate on the larger to bound
  stack depth to O(log n). Python's default recursion limit (~1000) can otherwise be exceeded
  for `n = 5 * 10^4`.
- **Single element / empty range:** `lo >= hi` is the base case; a length-1 array returns
  immediately.
- **Alternative:** a **randomized shuffle followed by deterministic quicksort** gives the same
  expected guarantee — the randomness can live either in the pivot choice or in an initial
  Fisher-Yates shuffle. Merge sort (deterministic O(n log n) worst case, O(n) space) is a
  non-randomized alternative if worst-case guarantees are required.
- **Las Vegas:** the output is always correctly sorted; only the running time is random.
