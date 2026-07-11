# Sort an Array (3-way Quicksort) — Solution

## Brute Force

**Classic 2-way quicksort (Lomuto partition).** Choose a pivot, move smaller elements left
and larger right, recurse on both halves.

```python
def quicksort(a, lo, hi):
    if lo >= hi:
        return
    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    quicksort(a, lo, i - 1)
    quicksort(a, i + 1, hi)
```

- **Average time:** O(n log n).
- **Worst time:** O(n^2) — e.g. already-sorted input with a bad pivot, or **an array of all
  equal keys**, where 2-way partitioning still recurses one element at a time.
- **Space:** O(log n) average recursion depth, O(n) worst case.

The killer weakness for this problem is **duplicates**: `[3,3,...,3]` degrades to O(n^2).

## Optimal Approach — Quicksort with Dutch National Flag Partition

Partition the current subarray `a[lo..hi]` into three regions around a pivot value `p`:
`< p`, `== p`, `> p`. Then recurse only on the `< p` and `> p` regions — everything equal to
the pivot is already final.

```python
import random

def sortArray(nums):
    def qsort(lo, hi):
        if lo >= hi:
            return
        # random pivot value to avoid adversarial O(n^2) inputs
        p = nums[random.randint(lo, hi)]
        lt, i, gt = lo, lo, hi          # DNF pointers over a[lo..hi]
        while i <= gt:
            if nums[i] < p:
                nums[lt], nums[i] = nums[i], nums[lt]
                lt += 1
                i += 1
            elif nums[i] > p:
                nums[i], nums[gt] = nums[gt], nums[i]
                gt -= 1
            else:                        # nums[i] == p
                i += 1
        # a[lo..lt-1] < p, a[lt..gt] == p, a[gt+1..hi] > p
        qsort(lo, lt - 1)
        qsort(gt + 1, hi)

    qsort(0, len(nums) - 1)
    return nums
```

### Why it is correct

Within one call, the DNF invariants guarantee that after the `while` loop `a[lo..lt-1] < p`,
`a[lt..gt] == p`, and `a[gt+1..hi] > p`. The equal block is in its final sorted position
(all keys equal to `p`, and everything smaller is to its left, everything larger to its
right). Recursing on the two outer regions sorts them independently, and since those regions
contain only values `< p` and `> p` respectively, concatenation yields a fully sorted array.
Each recursive call operates on a strictly smaller region, so recursion terminates.

### Why it beats 2-way on duplicates

The equal-to-pivot block is removed from the problem in a single pass. For `[3,3,3]` the very
first call places all three in the `== p` region, leaving empty `< p` and `> p` subproblems —
**O(n)** total instead of O(n^2). More generally, if the array has only `k` distinct values,
3-way quicksort runs in **O(n log k)** time (this is the classic "entropy-optimal" result for
quicksort by Bentley and McIlroy / Sedgewick).

### Random pivot

Choosing the pivot value at random (or median-of-three) makes the expected running time
**O(n log n)** regardless of the input ordering, sidestepping the worst case that a fixed
first/last pivot suffers on sorted or reverse-sorted data.

- **Time:** O(n log n) expected; O(n log k) with only k distinct keys.
- **Space:** O(log n) expected recursion depth.

## Key Insights & Edge Cases

- Pivot must be a **value**, not just an index, because after swaps the pivot element moves.
  Capture `p = nums[...]` before the loop.
- The three DNF pointers here are named `lt` (less-than boundary), `i` (scanner), and `gt`
  (greater-than boundary) but behave exactly like `low / mid / high`.
- **Recurse on `[lo, lt-1]` and `[gt+1, hi]` only** — never on the equal block, or you get
  infinite recursion / wasted work.
- LeetCode's largest cases include arrays that are all identical or nearly sorted; a fixed
  pivot times out, so use randomization.
- Base case `lo >= hi` covers empty and single-element regions.
- Deep recursion can be avoided by recursing on the smaller side first and looping on the
  larger side (tail-call elimination) to bound stack depth at O(log n).
