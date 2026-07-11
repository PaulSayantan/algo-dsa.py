# Solution — Search Insert Position

## Brute Force

Scan left to right and return the first index `i` where `nums[i] >= target`. If no such index
exists, return `len(nums)`.

```python
def searchInsert(nums, target):
    for i, v in enumerate(nums):
        if v >= target:
            return i
    return len(nums)
```

- **Time:** `O(n)` — a full linear scan in the worst case.
- **Space:** `O(1)`.

This ignores the fact that the array is sorted, and violates the required `O(log n)` bound.

## Optimal Approach — Lower Bound (bisect)

The insertion index is, by definition, the **first position whose value is `>= target`**. That is
precisely the **lower bound**. Binary search for it:

```python
def searchInsert(nums, target):
    lo, hi = 0, len(nums)          # hi is exclusive; answer lives in [0, n]
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:     # mid is strictly below target -> discard mid and everything left
            lo = mid + 1
        else:                      # nums[mid] >= target -> mid is a candidate; keep it, look left
            hi = mid
    return lo
```

### Why it is correct

**Invariant:** at every iteration, every index in `[0, lo)` has a value `< target`, and every
index in `[hi, n)` has a value `>= target`. Each step preserves this:

- If `nums[mid] < target`, then indices `0..mid` are all `< target` (sortedness), so `lo = mid + 1`.
- Otherwise `nums[mid] >= target`, so `mid` (and everything to its right) is `>= target`, so `hi = mid`.

The window `[lo, hi)` strictly shrinks, so the loop terminates with `lo == hi`. At that point `lo`
is the first index with value `>= target` — the insertion point. If `target` is present (distinct
values), `nums[lo] == target`, so the same value doubles as "found" and "insert" answers.

### Step-by-step on `nums = [1,3,5,6], target = 2`

| lo | hi | mid | nums[mid] | comparison | action |
|----|----|-----|-----------|------------|--------|
| 0  | 4  | 2   | 5         | `5 >= 2`   | hi = 2 |
| 0  | 2  | 1   | 3         | `3 >= 2`   | hi = 1 |
| 0  | 1  | 0   | 1         | `1 < 2`    | lo = 1 |
| 1  | 1  | —   | —         | loop ends  | return `1` |

- **Time:** `O(log n)`.
- **Space:** `O(1)`.

Equivalent one-liner with the standard library: `bisect.bisect_left(nums, target)`.

## Key Insights & Edge Cases

- **Use exclusive `hi = len(nums)`**, not `len(nums) - 1`. The answer can be `n` (target larger
  than everything), and an exclusive upper index makes that fall out naturally.
- The comparison is `nums[mid] < target` → move right; `>=` → move left. Using `<=` here would
  compute the *upper* bound instead, which for present targets returns the index *after* the match.
- **Empty search space:** the loop condition `lo < hi` handles a zero-length array gracefully
  (returns `0`), though the constraints guarantee at least one element.
- **Target smaller than all** → returns `0`; **target larger than all** → returns `n`.
- Because values are distinct, lower and upper bound differ by at most 1 for a present target;
  the distinction matters much more once duplicates appear (see Problem 3).
