# Kth Largest Element in an Array — Solution

## Brute Force

Sort the array in ascending order and index from the end:

```python
def findKthLargest(self, nums, k):
    nums.sort()
    return nums[len(nums) - k]   # k-th largest = index n-k after ascending sort
```

- **Time:** O(n log n) for the sort. **Space:** O(1) or O(n) depending on the sort.
- Simple and correct, but does more work than needed: we fully order all `n` elements when we
  only need the single element of rank `k`.

A heap-based improvement keeps a min-heap of the `k` largest seen so far: push each element,
and pop when the heap exceeds size `k`; the heap root is the answer. That is **O(n log k)**
time and **O(k)** space — better when `k` is small, but still not linear.

## Optimal Approach (Randomization: quickselect with a random pivot)

The k-th largest element is the element of **index `n - k`** in ascending sorted order (0-based).
Quickselect finds the element of a target index without sorting everything.

Partition the array around a pivot: after partitioning, the pivot sits at its final sorted
position `p`, with all smaller elements to its left and all larger to its right. Then:

- If `p == target`, the pivot *is* the answer.
- If `p < target`, recurse (or loop) on the right subarray.
- If `p > target`, recurse on the left subarray.

Only **one** side is explored, unlike quicksort which recurses into both.

```python
import random

def findKthLargest(self, nums, k):
    target = len(nums) - k          # 0-based index in ascending order
    lo, hi = 0, len(nums) - 1
    while True:
        p = self._partition(nums, lo, hi)
        if p == target:
            return nums[p]
        elif p < target:
            lo = p + 1
        else:
            hi = p - 1

def _partition(self, nums, lo, hi):
    # Randomly choose a pivot and swap it to the end -> defeats adversarial inputs.
    r = random.randint(lo, hi)
    nums[r], nums[hi] = nums[hi], nums[r]
    pivot = nums[hi]
    i = lo                          # boundary: nums[lo..i-1] are < pivot
    for j in range(lo, hi):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[hi] = nums[hi], nums[i]   # place pivot at its final spot
    return i
```

### Why the random pivot matters

With a *fixed* pivot choice (e.g., always the last element), an adversary — or simply an
already-sorted or reverse-sorted input — forces every partition to peel off just one element,
producing subproblems of size `n-1, n-2, ...` and **O(n^2)** total work. This is a real,
easily-triggered worst case, and LeetCode 215 includes such tests.

Choosing the pivot **uniformly at random** makes the split sizes independent of the input
order. No fixed input can reliably produce bad pivots, so the expected work per level shrinks
geometrically.

### Why it is O(n) expected

Each partition is O(size). With a random pivot, the expected position of the pivot splits the
range into two parts whose *expected* larger side is a constant fraction (about 3/4) of the
current size. Summing the expected partition costs gives

```
E[T(n)] = O(n + (3/4)n + (3/4)^2 n + ...) = O(n * 1/(1 - 3/4)) = O(n).
```

So the expected running time is **linear**. The worst case remains O(n^2), but its
probability is astronomically small and cannot be forced by the input.

### Complexity

- **Time:** O(n) expected; O(n^2) worst case (probability negligible with a random pivot).
- **Space:** O(1) extra with the iterative loop above (in-place partition). A recursive
  formulation uses O(log n) expected stack depth.

## Key Insights & Edge Cases

- **Rank conversion:** the k-th *largest* equals ascending index `n - k`. Getting this
  off-by-one right is the crux; verify with `k = 1` (largest -> index `n-1`) and `k = n`
  (smallest -> index `0`).
- **Random pivot per partition, not once.** Re-randomize the pivot at every partition call.
  A single up-front shuffle also works, but a fresh random pivot each call is the standard,
  robust choice.
- **Duplicates are fine.** Quickselect targets an *index*, not a distinct value, which is
  exactly what the problem asks (duplicates counted). Equal elements go to one side
  consistently; the partition invariant still holds.
- **Single element / k = 1 on length 1:** `target = 0`, the first partition returns index 0,
  and the loop returns immediately.
- **Iterative loop avoids stack issues** on large `n` (up to `10^5`) and keeps extra space
  O(1). If you recurse, tail-recurse into the needed side only.
- **Las Vegas guarantee:** the answer is always correct; only the running time is random.
