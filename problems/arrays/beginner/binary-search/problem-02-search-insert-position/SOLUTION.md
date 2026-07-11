# Solution — Search Insert Position

## Brute Force

Walk left to right and return the first index whose value is `>= target`. If no
such element exists, the target belongs at the end, so return `len(nums)`.

```python
for i, v in enumerate(nums):
    if v >= target:
        return i
return len(nums)
```

- **Time:** O(n).
- **Space:** O(1).

Correct, but linear — it does not meet the required `O(log n)`.

## Optimal Approach (Binary Search — Lower Bound)

The insertion index is exactly the **lower bound**: the first position `i` such
that `nums[i] >= target`. Note the elegant unification — when the target *is*
present, the lower bound is its own index; when it is absent, the lower bound is
where it should be inserted. So a single lower-bound search answers both cases.

Use the **half-open** interval `[lo, hi)` template. `hi` starts at `len(nums)`
(not `len(nums) - 1`) so the answer can legitimately be "past the end".

1. `lo = 0`, `hi = len(nums)`.
2. While `lo < hi`:
   - `mid = lo + (hi - lo) // 2`.
   - If `nums[mid] < target`, then `mid` and everything left of it are too
     small — the answer is strictly to the right: `lo = mid + 1`.
   - Else (`nums[mid] >= target`), `mid` is a *candidate*; keep it but look for
     something even earlier: `hi = mid`.
3. Return `lo`.

```python
def searchInsert(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

**Why it is correct.** The predicate `nums[mid] >= target` is **monotonic**:
once it becomes true scanning left to right, it stays true (the array is
sorted). Binary search finds the boundary between the "false" prefix and the
"true" suffix. The invariant is that every index `< lo` fails the predicate and
every index `>= hi` satisfies it; when `lo == hi` the boundary is pinned exactly.

- **Time:** O(log n).
- **Space:** O(1).

## Key Insights & Edge Cases

- **`hi = len(nums)`, not `len(nums) - 1`.** The valid answers range over
  `[0, len(nums)]`; the insertion point can be *one past the last element*.
  This is the whole reason the half-open template is used here.
- **Do not exit early on equality.** Writing `hi = mid` (rather than returning
  when `nums[mid] == target`) still lands on the correct index and keeps the
  code uniform — though for distinct values you *could* return early.
- **Target larger than all elements** (`[1,3,5,6]`, target `7`): predicate is
  false everywhere, `lo` climbs to `len(nums) == 4`.
- **Target smaller than all elements** (`[1,3,5,6]`, target `0`): predicate is
  true at index 0, answer is 0.
- **Loop uses `lo < hi`** (strict) to match the half-open interval; `hi = mid`
  never revisits `mid`, and `lo = mid + 1` always advances, so termination is
  guaranteed.
