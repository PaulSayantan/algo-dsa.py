# Wiggle Sort II — Solution

## Brute Force

**Sort, then interleave the two halves.** Sort ascending, split into a smaller half and
a larger half, and fill even indices from the smaller half and odd indices from the
larger half — each half traversed **backwards** so equal values near the median are
pushed apart.

```python
s = sorted(nums)
n = len(nums)
half = (n + 1) // 2
small = s[:half][::-1]     # smaller half, reversed
large = s[half:][::-1]     # larger half, reversed
nums[0::2] = small
nums[1::2] = large
```

- **Time:** O(n log n) for the sort.
- **Space:** O(n) for the sorted copy and halves.

This is correct and easy to reason about; the reversal is what handles duplicates. The
optimal version replaces the full sort with Quickselect.

## Optimal Approach (Quickselect median + 3-way partition)

The strict inequalities mean the danger is equal values landing adjacent. The key fact:
if you place the **larger half** on the odd indices and the **smaller half** on the even
indices, the only values that can appear on both sides of the split are copies of the
**median**. If we push those medians as far apart as possible, no two equal medians end
up adjacent (guaranteed whenever an answer exists).

**Steps:**

1. **Quickselect the median.** Find the element that belongs at index `n // 2` in
   ascending order — this is the (upper) median — in average O(n).
2. **3-way partition around the median**, but through a *virtual index map* so that,
   as sorted rank increases, we fill positions `1, 3, 5, ..., 0, 2, 4, ...`. Larger-
   than-median values flow to the front (odd slots), smaller-than-median values flow to
   the back (even slots), and medians settle in the middle — spread across the two
   halves so equal medians are not adjacent.

The index map for an array of length `n` is:

```
A(i) = (1 + 2 * i) % (n | 1)
```

This lists all odd indices first, then all even indices, exactly matching "big values
first, small values last". We then run the Dutch-National-Flag 3-way partition using
`A(...)` in place of raw indices.

### Why it is correct

- Quickselect places the true median value at the split point of ranks, in O(n)
  average.
- The mapped 3-way partition arranges values so that everything `> median` sits on odd
  positions, everything `< median` on even positions, and the `== median` block bridges
  the two. Because the odd positions are filled from the top of the value range and the
  even positions from the bottom, an odd index always holds a value `>=` its even-index
  neighbors; strictness is preserved for medians because the interleaving separates
  duplicate medians by at least one slot — which is always possible when a valid answer
  exists (the median's multiplicity never exceeds `(n + 1) // 2`).

### Reference implementation

```python
import random
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)

        # Quickselect: value that belongs at ascending index k.
        def kth(k: int) -> int:
            lo, hi = 0, n - 1
            while True:
                r = random.randint(lo, hi)
                nums[r], nums[hi] = nums[hi], nums[r]
                pivot = nums[hi]
                i = lo
                for j in range(lo, hi):
                    if nums[j] < pivot:
                        nums[i], nums[j] = nums[j], nums[i]
                        i += 1
                nums[i], nums[hi] = nums[hi], nums[i]
                if i == k:
                    return nums[i]
                elif i < k:
                    lo = i + 1
                else:
                    hi = i - 1

        mid = kth(n // 2)

        # Virtual index: odd slots first (1,3,5,...), then even slots (0,2,...).
        def A(i: int) -> int:
            return (1 + 2 * i) % (n | 1)

        # 3-way partition (Dutch National Flag) over the mapped indices.
        i = j = 0
        k = n - 1
        while j <= k:
            if nums[A(j)] > mid:
                nums[A(i)], nums[A(j)] = nums[A(j)], nums[A(i)]
                i += 1
                j += 1
            elif nums[A(j)] < mid:
                nums[A(j)], nums[A(k)] = nums[A(k)], nums[A(j)]
                k -= 1
            else:
                j += 1
```

### Complexity

- **Time:** O(n) expected (Quickselect) + O(n) (single-pass partition) = **O(n)**
  average. Worst case O(n^2) from Quickselect, mitigated by the random pivot.
- **Space:** O(1) — the median selection and the mapped partition are both in place.
  (The simpler brute force uses O(n); this version is the true O(1)-space answer.)

## Key Insights & Edge Cases

- **Strict inequalities + duplicates** are the entire difficulty. Just sorting and
  alternating fails on inputs like `[4, 5, 5, 6]`; the reverse-interleave (brute force)
  or median-then-mapped-partition (optimal) is what separates equal medians.
- **The index map `(1 + 2*i) % (n | 1)`** is the clever piece: `n | 1` rounds the
  modulus up to the next odd number so odd and even slots enumerate cleanly for both
  even and odd `n`.
- **Upper median (`k = n // 2`)** is the right choice so the larger half (which fills
  the more numerous / leading odd slots for odd `n`) is at least as big as the smaller
  half.
- **Guaranteed feasible:** the problem promises a valid answer, i.e. no value appears
  more than `(n + 1) // 2` times, which is exactly the condition under which this
  placement avoids adjacent equal medians.
- **Tiny inputs** (`n == 1`, `n == 2`) already satisfy the pattern or need at most the
  single comparison `nums[0] < nums[1]`, and the algorithm handles them without special
  casing.
