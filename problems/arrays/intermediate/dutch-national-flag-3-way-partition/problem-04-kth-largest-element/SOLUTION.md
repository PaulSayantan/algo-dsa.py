# Kth Largest Element (3-way Quickselect) — Solution

## Brute Force

**Sort and index.** Sort ascending and return the element at position `n - k`.

```python
def findKthLargest(nums, k):
    nums.sort()
    return nums[len(nums) - k]
```

- **Time:** O(n log n).
- **Space:** O(1) to O(n) depending on the sort.

A min-heap of size `k` is a common alternative at **O(n log k)** time and **O(k)** space.
Both are fine, but neither hits the **expected O(n)** that quickselect achieves.

## Optimal Approach — Quickselect with Dutch National Flag Partition

The kth largest in ascending order sits at index `target = n - k`. Quickselect repeatedly
partitions and recurses only into the side that contains `target`, discarding the rest.

Using a **3-way (DNF)** partition around a pivot value `p`, after partitioning the current
range `[lo, hi]` we have:

- `a[lo .. lt-1] < p`
- `a[lt .. gt] == p`   (the equal block, final positions)
- `a[gt+1 .. hi] > p`

Then:

- If `target < lt`, the answer is in the `< p` region → recurse on `[lo, lt-1]`.
- If `target > gt`, the answer is in the `> p` region → recurse on `[gt+1, hi]`.
- Otherwise `lt <= target <= gt`, so `a[target] == p` and the answer is `p`.

```python
import random

def findKthLargest(nums, k):
    target = len(nums) - k          # index in ascending order
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        p = nums[random.randint(lo, hi)]
        lt, i, gt = lo, lo, hi
        while i <= gt:              # Dutch National Flag partition
            if nums[i] < p:
                nums[lt], nums[i] = nums[i], nums[lt]
                lt += 1
                i += 1
            elif nums[i] > p:
                nums[i], nums[gt] = nums[gt], nums[i]
                gt -= 1
            else:
                i += 1
        if target < lt:
            hi = lt - 1
        elif target > gt:
            lo = gt + 1
        else:
            return nums[target]     # target lands in the equal block
    return nums[target]             # safety net (single element / lo==hi)
```

### Why it is correct

The DNF partition guarantees the three-region ordering, and the equal block `[lt, gt]` holds
values that are in their **final sorted positions** (all equal to `p`, with strictly smaller
values to the left and strictly larger to the right). So:

- If `target` falls inside `[lt, gt]`, `nums[target] == p` is the true kth-largest value.
- Otherwise the target is strictly on one side, and we discard the other two regions and
  continue. Because the equal block is at least one element wide, every iteration strictly
  shrinks the search window (`hi - lo` decreases), guaranteeing termination.

### Why the 3-way partition helps

With ordinary 2-way quickselect, a range of equal keys can cause repeated unbalanced
partitions. The equal block here removes **all** copies of the pivot from consideration at
once, so inputs like Example 2 (with duplicate 5s) or an all-equal array resolve immediately
instead of degenerating.

### Worked trace on `nums = [3, 2, 1, 5, 6, 4]`, `k = 2`

`n = 6`, `target = 6 - 2 = 4`. Suppose the first pivot chosen is `p = 4`.

Partition `[3,2,1,5,6,4]` around `4` → `< 4`: `{3,2,1}`, `== 4`: `{4}`, `> 4`: `{5,6}`, e.g.
`[3,2,1,4,6,5]` with `lt = 3`, `gt = 3`. Since `target = 4 > gt = 3`, recurse on `[4,5]`
(`{6,5}`). Pivot `p = 5` there → `< 5`: `{}`... actually `{}`? values are `6,5`: `== 5`:
`{5}`, `> 5`: `{6}`, giving `lt = 4`, `gt = 4`. Now `target = 4` is in `[lt, gt]`, so the
answer is `nums[4] = 5`. Correct (2nd largest of the array is `5`).

- **Time:** O(n) expected (each round processes and discards a constant fraction on average);
  O(n^2) only under adversarial pivots, which random pivoting makes vanishingly unlikely.
- **Space:** O(1) — the loop-based version uses no recursion stack.

## Key Insights & Edge Cases

- **Translate the rank once:** kth largest ascending index is `n - k`. Off-by-one here is the
  most common mistake.
- Capture the pivot as a **value** before partitioning, since the pivot element moves.
- Use a **random pivot** (or median-of-three) to guarantee expected linear time on sorted,
  reverse-sorted, or adversarial inputs.
- The equal-block check `lt <= target <= gt` is what makes duplicates cheap — do not collapse
  it into a 2-way `target < pivotIndex` comparison.
- Single-element arrays (`k = 1`, `n = 1`) return immediately; the `while lo <= hi` guard and
  final return handle it.
- The array is reordered as a side effect; make a copy first if the caller needs the original
  ordering.
