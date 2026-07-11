# Solution — Find First and Last Position of Element in Sorted Array

## Brute Force

Linear scan: record the first index where `nums[i] == target` and the last such index.

```python
def searchRange(nums, target):
    first = last = -1
    for i, v in enumerate(nums):
        if v == target:
            if first == -1:
                first = i
            last = i
    return [first, last]
```

- **Time:** `O(n)`.
- **Space:** `O(1)`.

Correct but linear, violating the required `O(log n)`.

## Optimal Approach — Lower Bound + Upper Bound

The equal-valued block occupied by `target` is bracketed by two boundaries:

- **first index** of `target` = **lower bound** `lb = lb(target)` (first index with value `>= target`).
- **last index** of `target` = **upper bound** minus one = `ub(target) - 1` (upper bound is the first
  index with value `> target`, so one step left is the last index equal to `target`).

`target` is present **iff** `lb < n` and `nums[lb] == target`.

```python
def searchRange(nums, target):
    def lower_bound(x):            # first index i with nums[i] >= x
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def upper_bound(x):            # first index i with nums[i] > x
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] <= x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    lb = lower_bound(target)
    if lb == len(nums) or nums[lb] != target:
        return [-1, -1]           # target not present
    return [lb, upper_bound(target) - 1]
```

### Why it is correct

- `lower_bound(target)` returns the leftmost index with value `>= target`. If that value is exactly
  `target`, it is the **first** occurrence; if it is `> target` (or out of range), `target` is absent.
- `upper_bound(target)` returns the leftmost index with value `> target`, i.e. one past the **last**
  occurrence. Subtracting 1 lands on the last index equal to `target`. Since we only reach this line
  after confirming `target` exists, `upper_bound - 1 >= lb`, so the range is valid.
- The two searches differ **only** in `<` vs `<=`; that single character controls whether equal
  elements are pushed left or right.

### Step-by-step on `nums = [5,7,7,8,8,10], target = 8`

Lower bound of 8:

| lo | hi | mid | nums[mid] | `< 8`? | action |
|----|----|-----|-----------|--------|--------|
| 0  | 6  | 3   | 8         | no     | hi = 3 |
| 0  | 3  | 1   | 7         | yes    | lo = 2 |
| 2  | 3  | 2   | 7         | yes    | lo = 3 |
| 3  | 3  | —   | —         | end    | `lb = 3` |

`nums[3] == 8` ✓. Upper bound of 8:

| lo | hi | mid | nums[mid] | `<= 8`? | action |
|----|----|-----|-----------|---------|--------|
| 0  | 6  | 3   | 8         | yes     | lo = 4 |
| 4  | 6  | 5   | 10        | no      | hi = 5 |
| 4  | 5  | 4   | 8         | yes     | lo = 5 |
| 5  | 5  | —   | —         | end     | `ub = 5` |

Answer: `[3, 5 - 1] = [3, 4]`. ✓

- **Time:** `O(log n)` — two independent binary searches.
- **Space:** `O(1)`.

Standard library equivalent: `lb = bisect_left(nums, target)`, `ub = bisect_right(nums, target)`;
return `[lb, ub - 1]` if `lb < ub` else `[-1, -1]`.

## Key Insights & Edge Cases

- **Count of `target`** falls out for free: `ub - lb`. Here `5 - 3 = 2` occurrences.
- **Empty array** (Example 3): both bounds are `0`, `lb == len(nums)` is true, so return `[-1, -1]`.
- **Target between values but absent** (Example 2, target 6): `lb` points at the `7`, `nums[lb] != 6`,
  return `[-1, -1]`. The presence check `nums[lb] != target` is essential — lower bound alone never
  tells you whether the value is actually there.
- **Target smaller than all** → `lb = 0`, check `nums[0] != target` catches absence.
  **Target larger than all** → `lb = n`, the `lb == len(nums)` guard catches it before indexing.
- Do **not** compute `ub - 1` before verifying presence: for an absent target `ub` could equal `lb`,
  and `ub - 1` could even be `-1`, producing a garbage range.
