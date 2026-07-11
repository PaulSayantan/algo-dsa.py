# Solution — Find All Numbers Disappeared in an Array

## Brute Force

Build a `set` of the values in `nums`, then walk `1..n` and collect every value
that is not in the set.

```python
def findDisappearedNumbers(nums):
    present = set(nums)
    return [v for v in range(1, len(nums) + 1) if v not in present]
```

- **Time:** `O(n)` — one pass to build the set, one pass over the range.
- **Space:** `O(n)` — the auxiliary set can hold up to `n` values.

This is perfectly correct, but it defeats the follow-up requirement of `O(1)`
extra space. That is where in-place marking comes in.

## Optimal Approach (In-Place Sign Marking)

**Key observation:** every legal value `v` satisfies `1 <= v <= n`, so `v - 1`
is always a valid index into the array. We can therefore let the array double
as a "seen" table.

### Step by step

1. **Mark pass.** For each element, take its magnitude `v = abs(nums[i])`
   (magnitude, because an earlier iteration may already have negated this slot).
   Compute the target index `idx = v - 1`. If `nums[idx]` is still positive,
   negate it: `nums[idx] = -nums[idx]`. A negative sign at index `idx` now means
   "the value `idx + 1` was seen at least once."
2. **Collect pass.** Walk the array again. Every index `i` whose value is still
   **positive** was never marked, which means `i + 1` never appeared. Add
   `i + 1` to the answer.

```python
def findDisappearedNumbers(nums):
    for i in range(len(nums)):
        idx = abs(nums[i]) - 1
        if nums[idx] > 0:
            nums[idx] = -nums[idx]
    return [i + 1 for i in range(len(nums)) if nums[i] > 0]
```

### Why it is correct

- Using `abs()` when reading guarantees we recover the original value even if
  the slot we are reading was itself flipped by a previous step, so the mapping
  `value -> index` is never corrupted.
- The `if nums[idx] > 0` guard means a value that appears twice simply tries to
  negate an already-negative slot; we skip the second flip, keeping the sign
  stable. Whether a value appears once or twice, its target index ends up
  negative exactly when the value is present.
- After the mark pass, positivity of `nums[i]` is a perfect indicator of "value
  `i + 1` is missing," because only present values ever caused a negation.

### Complexity

- **Time:** `O(n)` — two linear passes.
- **Space:** `O(1)` extra — the output list is required by the problem and does
  not count against the in-place budget.

## Key Insights & Edge Cases

- **Read magnitude, write sign.** The single most common bug is reading
  `nums[i]` directly instead of `abs(nums[i])`; once you have negated some
  slots, a raw read produces a negative index or the wrong index.
- **Idempotent marking.** The `> 0` check keeps duplicates from flipping a slot
  back to positive. Without it, a value appearing twice would toggle its slot
  and be misreported as missing.
- **All present:** `[1,2,3,4]` -> every slot gets negated -> empty result.
- **All duplicates of one value:** `[1,1]` -> only index 0 gets negated; index 1
  stays positive -> `[2]`.
- **Restoring the array:** if the caller needs `nums` unchanged afterward, do a
  third pass taking `abs()` of every element. Not required by this problem.
