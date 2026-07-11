# Solution — Median of an Unsorted Array

## Brute Force

Sort the array, then read the middle element(s).

```python
def find_median(nums):
    nums.sort()
    n = len(nums)
    if n % 2 == 1:
        return nums[n // 2]
    return (nums[n // 2 - 1] + nums[n // 2]) / 2
```

- **Time:** `O(n log n)`.
- **Space:** `O(1)` to `O(n)` depending on the sort.

This is simple and often perfectly acceptable. Quickselect beats it asymptotically when
you truly need only the median and want expected linear time.

## Optimal Approach (Quickselect)

The median lives at fixed sorted index/indices:

- Odd `n`: index `n // 2`.
- Even `n`: indices `n // 2 - 1` and `n // 2`, averaged.

Quickselect returns the element at a requested sorted index in expected `O(n)`, so we
call it once (odd) or twice (even).

### Why it is correct

Quickselect's partition places a pivot at its final sorted position `p` with all smaller
elements to the left and all larger to the right, then recurses only into the side holding
the target index. When the pivot lands on the target index, that slot holds precisely the
element that a full sort would place there — which is exactly what the median definition asks for.

### Handling the even case efficiently

After `select(nums, n // 2)` runs, the array is **partially partitioned**: every element
at index `< n // 2` is `<=` `nums[n // 2]`. So the second middle value (`nums[n//2 - 1]`)
is simply the **maximum of the left part** `nums[0 .. n//2 - 1]`, which you can grab in a
single `max(...)` scan instead of a second full Quickselect. (A second `select` call also
works and keeps the code uniform; both are `O(n)`.)

### Reference implementation

```python
import random
from typing import List


def _partition(nums: List[int], lo: int, hi: int) -> int:
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


def _select(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        p = _partition(nums, lo, hi)
        if p == target:
            return nums[p]
        elif p < target:
            lo = p + 1
        else:
            hi = p - 1
    return nums[lo]


def find_median(nums: List[int]) -> float:
    n = len(nums)
    mid = n // 2
    upper = _select(nums, mid)
    if n % 2 == 1:
        return upper
    # After selecting index `mid`, everything left of `mid` is <= upper,
    # so the lower-middle element is the max of the left partition.
    lower = max(nums[:mid])
    return (lower + upper) / 2
```

- **Time:** expected `O(n)` (one or two linear selection passes plus one linear `max`).
- **Space:** `O(1)` (the `nums[:mid]` slice can be replaced by an in-place scan to keep it
  strictly `O(1)`).

## Key Insights & Edge Cases

- **Even vs. odd index math:** for even `n` the two middle indices are `n//2 - 1` and
  `n//2`; forgetting the `-1` (or averaging the wrong pair) is the classic bug.
- **Return type:** the average of two integers can be fractional — return a float
  (`2.5`), not an integer-truncated value.
- **Reusing partition work:** don't run a full second Quickselect for the even case if you
  can grab the left-partition maximum; it is already isolated.
- **Single element:** `n = 1` returns that element directly (odd branch, index `0`).
- **Duplicates / negatives:** handled naturally; `<=` in partition keeps equal elements
  stable relative to the pivot boundary and negatives compare normally.
- **Randomize the pivot** to keep the expected-linear guarantee on sorted/adversarial input.
