# Solution — Find Peak Element

## Brute Force

Scan for the first index whose value is greater than the next value; that index
must be a peak (or, if no such index exists, the array is strictly increasing
and the last element is the peak).

```python
for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        return i
return len(nums) - 1
```

- **Time:** O(n).
- **Space:** O(1).

Correct, but linear — the problem explicitly demands `O(log n)`.

## Optimal Approach (Binary Search on the Slope)

The array is **not** globally sorted, yet binary search still works because of
a monotonicity argument on the *local slope*.

Look at `mid` and its right neighbor `mid + 1`:

- If `nums[mid] < nums[mid + 1]` — we are on an **uphill** slope. Since the
  array ends with a virtual `-∞`, walking right must eventually turn downward,
  so a peak is guaranteed somewhere in `(mid, n)`. Move `lo = mid + 1`.
- If `nums[mid] > nums[mid + 1]` — we are on a **downhill** slope (or at a
  peak). Because the left virtual boundary is also `-∞`, a peak is guaranteed at
  `mid` or to its left. Move `hi = mid`.

Use the half-open template with `hi = n - 1` (we compare `mid` against
`mid + 1`, so `mid` never reaches the last index and `mid + 1` stays in bounds).

```python
def findPeakElement(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] < nums[mid + 1]:
            lo = mid + 1      # peak is to the right
        else:
            hi = mid          # peak is at mid or to the left
    return lo                 # lo == hi points at a peak
```

**Why it is correct.** Maintain the invariant that the search range always
contains a peak, given the `-∞` sentinels at both ends. Each step keeps whichever
half is guaranteed to still contain a peak (the uphill direction always leads to
one because the sequence must eventually descend). When `lo == hi`, the range
has collapsed to a single index that the invariant guarantees is a peak.

- **Time:** O(log n) — the range halves each iteration.
- **Space:** O(1).

## Key Insights & Edge Cases

- **No global sort required.** The trick is that a *monotonic decision*
  (uphill/downhill) suffices; you never need the whole array to be sorted, only
  a reliable "which way is up" test.
- **Compare with the right neighbor.** Using `hi = len(nums) - 1` keeps
  `mid + 1` in bounds because `mid < hi` inside the loop.
- **Always keep `mid` on the downhill branch** (`hi = mid`, not `mid - 1`):
  `mid` itself may be the peak, so it must remain in the range.
- **Single element** (`[1]`): loop body never runs, returns 0.
- **Strictly increasing** (`[1,2,3,4]`): always takes the uphill branch, `lo`
  rises to the last index — the peak.
- **Strictly decreasing** (`[4,3,2,1]`): always takes the downhill branch,
  returns 0.
- **Any valid peak is acceptable**, so the specific tie-broken index the search
  lands on does not matter.
