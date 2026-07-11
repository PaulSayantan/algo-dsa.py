# Solution — Find First and Last Position

## Brute Force

Linear scan: record the first index where `nums[i] == target` and the last
index where it occurs.

```python
first = last = -1
for i, v in enumerate(nums):
    if v == target:
        if first == -1:
            first = i
        last = i
return [first, last]
```

- **Time:** O(n).
- **Space:** O(1).

Correct but linear, failing the `O(log n)` requirement. With duplicates a plain
equality binary search would land on *some* occurrence, not necessarily the
first or last, so we need boundary searches.

## Optimal Approach (Two Boundary Binary Searches)

The key idea is **lower bound** and **upper bound**:

- `lower_bound(target)` = first index `i` with `nums[i] >= target`.
- `upper_bound(target)` = first index `i` with `nums[i] > target`.

Then:

- **first occurrence** = `lower_bound(target)`, *provided* that index is in
  range and `nums[index] == target`.
- **last occurrence** = `upper_bound(target) - 1`.

Both bounds use the standard half-open template and differ only in the
comparison operator.

```python
def searchRange(nums, target):
    def lower_bound(x):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    left = lower_bound(target)
    if left == len(nums) or nums[left] != target:
        return [-1, -1]
    # upper_bound(target) == lower_bound(target + 1) for integers,
    # but doing an explicit '>' search is clearer:
    right = lower_bound(target + 1) - 1
    return [left, right]
```

**Why it is correct.** Each boundary search locates the transition point of a
monotonic predicate over the sorted array. `lower_bound` finds where values stop
being `< target`; if the element there equals the target, that is the earliest
occurrence. Everything strictly greater than the target starts at
`upper_bound`, so the last target sits at `upper_bound - 1`. If the target never
appears, `lower_bound` points at a non-matching element (or past the end), which
we detect and return `[-1, -1]`.

- **Time:** O(log n) — two binary searches.
- **Space:** O(1).

## Key Insights & Edge Cases

- **Two searches, not one.** With duplicates a single equality search cannot
  distinguish the first from the last occurrence. Reframing as "find the
  boundary of a predicate" is the crux.
- **Guard the lower-bound result.** After `left = lower_bound(target)` you must
  check both `left < len(nums)` *and* `nums[left] == target` before trusting it;
  otherwise a missing target looks present.
- **`upper_bound(target) - 1`** correctly yields the last index; since we only
  reach that line when the target exists, `right >= left`.
- **Empty array** (`[]`): `lower_bound` returns 0, `0 == len(nums)` triggers the
  guard, output `[-1, -1]`.
- **Target present exactly once:** `first == last`, e.g. searching `10` in
  `[5,7,7,8,8,10]` gives `[5, 5]`.
- **All elements equal the target:** returns `[0, len(nums) - 1]`.
