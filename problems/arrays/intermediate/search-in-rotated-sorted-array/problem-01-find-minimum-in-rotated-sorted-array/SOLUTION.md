# Solution — Find Minimum in Rotated Sorted Array

## Brute Force

Scan every element and track the smallest, or simply call `min(nums)`.

```python
def findMin(nums):
    return min(nums)
```

- **Time:** `O(n)` — every element is inspected.
- **Space:** `O(1)`.

This ignores the sorted-and-rotated structure and violates the required
`O(log n)` bound, so it is only a correctness baseline.

## Optimal Approach (Search in Rotated Sorted Array)

The minimum is the single "drop" point where a larger value is immediately
followed by a smaller one (the pivot). A rotated sorted array of distinct values
splits into two ascending runs; the minimum is the first element of the second
run. We binary-search for it.

Keep a window `[lo, hi]`. Compare `nums[mid]` with `nums[hi]` (the right
endpoint):

- If `nums[mid] > nums[hi]`, then `mid` is in the **left (higher) run** and the
  pivot must be strictly to the right of `mid`. Discard the left half:
  `lo = mid + 1`.
- Otherwise `nums[mid] <= nums[hi]`, so the right half from `mid` to `hi` is
  sorted and the minimum is at `mid` or to its left. Keep `mid` as a candidate:
  `hi = mid`.

Loop while `lo < hi`. Because we never discard `mid` when it could be the
answer (we set `hi = mid`, not `hi = mid - 1`), the window converges to the
single minimum. When `lo == hi`, that index holds the minimum.

```python
def findMin(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1        # min is strictly right of mid
        else:
            hi = mid            # min is mid or to its left
    return nums[lo]
```

**Why compare against `nums[hi]` and not `nums[lo]`?** Comparing with `nums[hi]`
gives an unambiguous answer for both the rotated and the fully-sorted case. If
the array is not rotated at all (already ascending), every `nums[mid]` is
`<= nums[hi]`, so `hi` keeps moving left until it lands on index 0 — the correct
minimum. Comparing with `nums[lo]` needs an extra "is this half rotated at all?"
check.

**Why `hi = mid` (not `mid - 1`)?** When `nums[mid] <= nums[hi]`, `mid` itself
might be the minimum, so it must stay inside the window. Using `mid - 1` could
skip over the answer. Pairing `hi = mid` with `lo = mid + 1` still guarantees
progress because `mid < hi` whenever `lo < hi`.

- **Time:** `O(log n)` — the window halves each iteration.
- **Space:** `O(1)`.

### Step-by-step on `nums = [4,5,6,7,0,1,2]`

| lo | hi | mid | nums[mid] | nums[hi] | action |
|----|----|-----|-----------|----------|--------|
| 0  | 6  | 3   | 7         | 2        | `nums[mid] > nums[hi]` -> lo = 4 |
| 4  | 6  | 5   | 1         | 2        | `nums[mid] <= nums[hi]` -> hi = 5 |
| 4  | 5  | 4   | 0         | 1        | `nums[mid] <= nums[hi]` -> hi = 4 |

Now `lo == hi == 4`, and `nums[4] = 0` is the minimum.

## Key Insights & Edge Cases

- **Single element (`n == 1`):** `lo == hi` immediately, loop body never runs,
  and `nums[0]` is returned. Correct.
- **Not rotated / rotated n times (fully sorted):** every `nums[mid] <=
  nums[hi]`, so `hi` marches down to index 0 and the answer is `nums[0]`.
- **Invariant:** the minimum is always inside `[lo, hi]`. The `hi = mid` branch
  keeps a possible answer; the `lo = mid + 1` branch only drops elements that
  are provably larger than `nums[hi]`.
- **Distinct elements matter:** with duplicates, `nums[mid] == nums[hi]` becomes
  ambiguous. That variant (LeetCode 154) is Problem 5 in this set and can degrade
  to `O(n)`.
- **Don't use `nums[mid] < nums[lo]`-style tests without care** — mixing an
  endpoint you don't consistently shrink toward is the most common source of
  off-by-one bugs here.
