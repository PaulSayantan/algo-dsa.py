# Solution — Exponential Search in a Sorted Array

## Brute Force

Linear scan: walk the array and compare each element with `target`.

```python
def exponential_search(nums, target):
    for i, x in enumerate(nums):
        if x == target:
            return i
    return -1
```

- **Time:** `O(n)` — every element may be inspected.
- **Space:** `O(1)`.

Correct but throws away the sorted structure. A plain binary search would fix
the time to `O(log n)`; exponential search improves that further to `O(log p)`
where `p` is the position of the answer.

## Optimal Approach (Exponential / Galloping Search)

**Phase 1 — find a bounding window by doubling.** Start with `bound = 1`. While
`bound` is still inside the array and `nums[bound] < target`, double it:
`bound *= 2`. The loop advances only past elements strictly less than `target`,
so the moment it stops:

- either `bound` ran off the end (`bound >= n`), or
- `nums[bound] >= target`.

Either way, if `target` exists it must lie in the index range
`[bound // 2, min(bound, n - 1)]`: everything below `bound // 2` was already
confirmed `< target` on the previous doubling step, and `bound` is the first
index we know reaches or exceeds `target`.

**Phase 2 — binary search the window.** Run a standard binary search over that
narrow `[lo, hi]` range.

Handle the trivial front cases first: an empty array returns `-1`, and
`nums[0] == target` returns `0` (this also keeps the doubling loop, which starts
at index `1`, from ever needing to look at index `0`).

```python
def exponential_search(nums, target):
    n = len(nums)
    if n == 0:
        return -1
    if nums[0] == target:
        return 0

    # Phase 1: gallop until we pass target or the end of the array.
    bound = 1
    while bound < n and nums[bound] < target:
        bound *= 2

    # Phase 2: binary search in [bound // 2, min(bound, n - 1)].
    lo, hi = bound // 2, min(bound, n - 1)
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

**Why is it correct?** The doubling loop's invariant is "every index `< bound`
holds a value `< target`." So the answer can never be to the left of
`bound // 2` (the previous `bound`), and it can never be to the right of
`bound` because `nums[bound] >= target` (or the array ended). The binary search
then decides presence exactly.

**Why `O(log p)`?** If the answer sits at index `p`, doubling stops when
`bound` first reaches or exceeds `p`, i.e. after `ceil(log2(p))` steps, so
`bound < 2p`. The window handed to binary search has size at most `bound - bound/2
= bound/2 < p`, so the binary search is another `O(log p)`. Total: `O(log p)`,
which is `<= O(log n)`.

- **Time:** `O(log p)` (`p` = index of the answer, or of the end of the array
  if the target is larger than everything).
- **Space:** `O(1)`.

### Step-by-step on `nums = [2,3,4,10,40], target = 10`

| step | bound | nums[bound] | action |
|------|-------|-------------|--------|
| init | 1 | 3 | `3 < 10` -> double |
| 1 | 2 | 4 | `4 < 10` -> double |
| 2 | 4 | 40 | `40 >= 10` -> stop |

Window = `[bound // 2, min(bound, n-1)] = [2, 4]`. Binary search: `mid = 3`,
`nums[3] = 10 == target` -> return `3`.

## Key Insights & Edge Cases

- **Empty array:** guard with `if n == 0: return -1` before touching `nums[0]`.
- **Target at index 0:** the explicit `nums[0] == target` check returns `0`.
  Without it, `bound = 1` might immediately satisfy `nums[1] >= target` and the
  window would still be `[0, ...]`, so binary search would also find it — but
  the early check makes intent clear and avoids reasoning about `bound // 2 = 0`.
- **Target larger than every element:** the doubling loop runs until
  `bound >= n`; the window is `[bound // 2, n - 1]` and binary search returns
  `-1`. No out-of-bounds read because the loop condition checks `bound < n`
  *before* indexing.
- **Clamp `hi` with `min(bound, n - 1)`:** `bound` can overshoot the array
  length after the final doubling; forgetting the clamp causes an index error.
- **Duplicates:** this version returns *some* matching index, not necessarily
  the first. To get the leftmost/rightmost occurrence, replace Phase 2 with a
  lower-bound / upper-bound binary search (see Problem 4).
