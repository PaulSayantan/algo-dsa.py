# Solution — Binary Search

## Brute Force

Scan the array from left to right and return the first index whose value equals
the target; return -1 if you reach the end.

```python
for i, v in enumerate(nums):
    if v == target:
        return i
return -1
```

- **Time:** O(n) — every element may be inspected.
- **Space:** O(1).

This ignores the fact that the array is sorted and violates the required
`O(log n)` bound.

## Optimal Approach (Binary Search)

Maintain an **inclusive** candidate range `[lo, hi]`. The target, if present,
always lies within this range — that is the loop invariant. Repeatedly examine
the middle element and shrink the range:

1. Set `lo = 0`, `hi = len(nums) - 1`.
2. While `lo <= hi`:
   - `mid = lo + (hi - lo) // 2` (this form avoids potential overflow in
     fixed-width integer languages; in Python `(lo + hi) // 2` is also fine).
   - If `nums[mid] == target`, return `mid`.
   - If `nums[mid] < target`, the target must be to the right, so `lo = mid + 1`.
   - Otherwise the target is to the left, so `hi = mid - 1`.
3. If the loop exits, the target is not present — return -1.

```python
def search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

**Why it is correct.** Because the array is sorted, comparing `nums[mid]` to the
target tells us which half the target can be in; the other half is provably
free of the target and is discarded. Each iteration strictly shrinks `hi - lo`
(either `lo` increases past `mid` or `hi` decreases below `mid`), so the loop
always terminates. When it exits, `lo > hi`, meaning the range is empty and the
target does not exist.

- **Time:** O(log n) — the range roughly halves each iteration.
- **Space:** O(1) — only a few index variables.

## Key Insights & Edge Cases

- **Loop condition matches interval.** With an *inclusive* `hi`, the condition
  must be `lo <= hi`. Using `<` would skip checking the final single-element
  range and miss valid answers.
- **Always move a boundary past `mid`.** Using `lo = mid + 1` / `hi = mid - 1`
  (not `lo = mid` / `hi = mid`) guarantees progress and prevents infinite loops.
- **Single element** (`[5]`, target `5`): `lo == hi == 0`, `mid = 0`, matches
  immediately — returns 0.
- **Target smaller than all / larger than all:** boundaries cross without a
  match and the function returns -1.
- **Overflow-safe midpoint:** `lo + (hi - lo) // 2` matters in languages with
  fixed-width integers; harmless in Python.
