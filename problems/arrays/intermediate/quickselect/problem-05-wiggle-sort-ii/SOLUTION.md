# Solution — Wiggle Sort II

## Brute Force

Sort the array, split it into a **lower half** and an **upper half**, then interleave them
so large and small values alternate. To avoid adjacent equal values (the duplicates cluster
at the median), fill the **odd** indices from the largest of the upper half downward and the
**even** indices from the largest of the lower half downward — i.e. read both halves from
their high end.

```python
def wiggleSort(self, nums):
    s = sorted(nums)
    n = len(nums)
    mid = (n + 1) // 2            # lower half gets the extra element when odd
    lo = s[:mid][::-1]           # smaller half, reversed
    hi = s[mid:][::-1]           # larger half, reversed
    nums[0::2] = lo              # even indices <- smaller half
    nums[1::2] = hi              # odd indices  <- larger half
```

- **Time:** `O(n log n)` for the sort.
- **Space:** `O(n)` for the halves.

Reading each half from its **high end** is what keeps the two medians apart: the two copies
of the median end up at the far end of the even block and the far end of the odd block, never
adjacent.

## Optimal Approach (Quickselect + three-way partition)

Replace the `O(n log n)` sort with an expected `O(n)` **median selection** via Quickselect,
then place values relative to the median using **virtual indexing** and a Dutch-national-flag
(three-way) partition — no second buffer needed for the placement step.

### Step 1 — find the median with Quickselect

The median is the element at sorted index `(n - 1) // 2` (the lower of the two middles for
even `n`). Quickselect returns it in expected `O(n)`.

### Step 2 — place with virtual indexing

Conceptually we want:

- values **greater** than the median on the **odd** indices `1, 3, 5, ...`,
- values **less** than the median on the **even** indices `0, 2, 4, ...`,
- the medians themselves squeezed into whatever slots remain, kept apart.

Define a virtual-index map that lays odd indices first, then even indices:

```
A(i) = (1 + 2 * i) % (n | 1)
```

Iterating `i = 0, 1, 2, ...` visits real indices `1, 3, 5, ..., 0, 2, 4, ...`. Running a
three-way partition (`> median` to the front, `< median` to the back, `== median` in the
middle) **over these virtual indices** places big values on odd slots and small values on
even slots, so equal medians can never become neighbors.

### Why it is correct

- After Quickselect, we know the median value `m`. In a valid wiggle arrangement, the upper
  half (`> m`) must occupy the "peak" (odd) positions and the lower half (`< m`) the "valley"
  (even) positions.
- The virtual map `A(i)` enumerates all peak positions before all valley positions. A
  three-way partition that pushes `> m` toward the start of this virtual order fills the peaks
  with the largest values and the valleys with the smallest, while the `== m` block sits at the
  transition — which corresponds to the *ends* of the odd block and *start* of the even block in
  real indices, keeping the two median copies maximally separated.
- The problem guarantees a valid answer exists, which means the count of the most frequent
  value is at most `ceil(n / 2)`; that is exactly the condition under which this separation
  succeeds.

### Reference implementation

```python
import random
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)

        # --- Step 1: median via Quickselect (sorted index (n-1)//2) ---
        median = self._select(nums, (n - 1) // 2)

        # --- Step 2: three-way partition over virtual indices ---
        def A(i: int) -> int:
            return (1 + 2 * i) % (n | 1)

        left, i, right = 0, 0, n - 1
        while i <= right:
            if nums[A(i)] > median:
                nums[A(i)], nums[A(left)] = nums[A(left)], nums[A(i)]
                left += 1
                i += 1
            elif nums[A(i)] < median:
                nums[A(i)], nums[A(right)] = nums[A(right)], nums[A(i)]
                right -= 1
            else:
                i += 1

    def _select(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            p = self._partition(nums, lo, hi)
            if p == target:
                return nums[p]
            elif p < target:
                lo = p + 1
            else:
                hi = p - 1
        return nums[lo]

    def _partition(self, nums: List[int], lo: int, hi: int) -> int:
        rand = random.randint(lo, hi)
        nums[rand], nums[hi] = nums[hi], nums[rand]
        pivot = nums[hi]
        i = lo
        for j in range(lo, hi):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[hi] = nums[hi], nums[i]
        return i
```

- **Time:** expected `O(n)` for Quickselect + `O(n)` for the single-pass three-way partition
  = expected `O(n)`.
- **Space:** `O(1)` extra — the virtual-index trick partitions in place, achieving the
  `O(n)` time / `O(1)` space follow-up.

### A simpler-to-reason variant

If the `O(1)`-space virtual indexing is hard to get right under pressure, a cleaner
Quickselect-based version keeps the `O(n)` median but uses an `O(n)` buffer for placement:

```python
def wiggleSort(self, nums):
    n = len(nums)
    median = self._select(nums[:], (n - 1) // 2)   # select on a copy
    s = sorted(nums)                                # or keep the buffer approach
    mid = (n + 1) // 2
    lo, hi = s[:mid][::-1], s[mid:][::-1]
    nums[0::2], nums[1::2] = lo, hi
```

The virtual-indexing version is the one that fully answers the follow-up; the buffer version is
easier to implement correctly and still uses Quickselect for the median.

## Key Insights & Edge Cases

- **Why simple wiggle fails:** the easy "swap adjacent out-of-order pairs" trick works only for
  *non-strict* wiggle. With duplicates at the median (e.g. `[1,1,2,2]`) strictness forces the
  median-based split.
- **Which median index:** use `(n - 1) // 2` (lower median). Pairing it with reading both halves
  from their **high ends** is what guarantees the two medians never touch.
- **Feasibility:** a valid arrangement exists iff no value appears more than `ceil(n / 2)` times.
  The problem guarantees this; otherwise no algorithm could satisfy strict inequalities.
- **Virtual index formula `(1 + 2*i) % (n | 1)`:** `n | 1` rounds the modulus up to the next odd
  number so the mapping is a bijection for both odd and even `n` — a frequent source of off-by-one
  bugs.
- **Small inputs:** `n = 1` is already a valid wiggle (no neighbors); the loop simply does nothing.
- **Randomize the pivot** in Quickselect to keep the median search expected-linear on sorted input.
