# Kth Largest Element in an Array — Solution

## Brute Force

Sort the array descending and index element `k-1`.

- **Time:** `O(n log n)` for the sort.
- **Space:** `O(1)` to `O(n)` depending on the sort.

A min-heap of size `k` gives `O(n log k)` time — better when `k` is small. But we can
do better on average with Divide and Conquer.

## Optimal Approach (Divide and Conquer — Quickselect)

**Idea:** The k-th largest element is the element at index `n - k` in **ascending**
sorted order (0-based). Quickselect finds the value at a target index *without*
sorting the whole array.

1. **Divide (partition):** choose a pivot and rearrange the current range so that all
   elements `< pivot` come before it and all `>= pivot` come after; the pivot ends at
   its final sorted index `p`.
2. **Conquer:** compare `p` with the target index `n - k`:
   - if `p == target`, the pivot *is* the answer;
   - if `p < target`, recurse into the **right** part only;
   - if `p > target`, recurse into the **left** part only.
3. **Combine:** trivial — there is nothing to merge, because only one side can contain
   the answer. This one-sided recursion is what makes quickselect linear on average.

```python
import random

def findKthLargest(nums, k):
    target = len(nums) - k          # k-th largest == index (n-k) ascending

    def partition(lo, hi):
        # random pivot avoids O(n^2) on sorted / adversarial input
        r = random.randint(lo, hi)
        nums[r], nums[hi] = nums[hi], nums[r]
        pivot = nums[hi]
        i = lo
        for j in range(lo, hi):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[hi] = nums[hi], nums[i]
        return i

    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        p = partition(lo, hi)
        if p == target:
            return nums[p]
        elif p < target:
            lo = p + 1              # recurse right
        else:
            hi = p - 1              # recurse left
```

**Why it is correct:** after `partition`, the pivot sits at its true sorted position
`p`; everything left is smaller, everything right is larger-or-equal. So the element at
index `target` lies strictly on the side indicated by comparing `p` to `target`, and
we never need the other side.

**Recurrence:** with a good (e.g. random) pivot the expected subproblem size shrinks
geometrically: `T(n) = T(n/2) + O(n)` on average → `O(n)`. Worst case (consistently
terrible pivots) is `T(n) = T(n-1) + O(n) = O(n^2)`.

- **Time:** `O(n)` average, `O(n^2)` worst case (mitigated by a random pivot; the
  median-of-medians pivot guarantees `O(n)` worst case at higher constant cost).
- **Space:** `O(1)` extra — partitioning is in place; the loop replaces recursion.

## Key Insights & Edge Cases

- **Only recurse into one side.** This is the crucial difference from quicksort:
  quicksort recurses into *both* halves (`O(n log n)`), quickselect into *one*
  (`O(n)` average). Both share the same partition-based divide.
- **Convert the rank once:** "k-th largest" ⇒ ascending index `n - k`. Getting this
  off-by-one right is the most common bug.
- **Randomize the pivot** (or use median-of-three). A fixed pivot on already-sorted or
  all-equal input degrades to `O(n^2)`.
- **Duplicates are fine:** the problem counts them, and partitioning by value handles
  equal keys without special cases (though many equal keys can unbalance a naive
  Lomuto partition — a three-way/Dutch-flag partition fixes that).
- **Single element / `k == n`** (smallest) / `k == 1` (largest) all fall out of the
  index arithmetic without special handling.
