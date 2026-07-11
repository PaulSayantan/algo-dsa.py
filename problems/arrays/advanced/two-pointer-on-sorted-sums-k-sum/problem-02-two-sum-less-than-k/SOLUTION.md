# Solution - Two Sum Less Than K

## Brute Force

Examine every pair and keep the best sum that stays under `k`.

```python
best = -1
for i in range(n):
    for j in range(i + 1, n):
        s = nums[i] + nums[j]
        if s < k:
            best = max(best, s)
return best
```

- **Time:** O(n^2).
- **Space:** O(1).

## Optimal Approach (Two-Pointer on Sorted Sums)

This is a maximization-under-a-bound variant. **Sort** `nums`, then sweep two
pointers `lo` (start) and `hi` (end).

### The invariant

Let `s = nums[lo] + nums[hi]`.

- If `s < k`, this pair is **valid**. Record it (`best = max(best, s)`). To try for
  a *larger* valid sum, we need a bigger contribution, so move `lo += 1` — this is
  the only pointer whose move can increase the sum while `hi` stays put. Any pair
  using the old `lo` with a value smaller than `nums[hi]` would only be smaller, so
  nothing better is lost.
- If `s >= k`, the pair is too big (`k` is an exclusive bound). The smallest partner
  for `nums[hi]` is `nums[lo]`, and even that overshoots, so `nums[hi]` cannot be in
  any valid pair. Discard it: `hi -= 1`.

### Reference implementation

```python
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        lo, hi = 0, len(nums) - 1
        best = -1
        while lo < hi:
            s = nums[lo] + nums[hi]
            if s < k:
                best = max(best, s)
                lo += 1
            else:
                hi -= 1
        return best
```

### Worked trace (Example 1)

`nums = [34, 23, 1, 24, 75, 33, 54, 8]`, `k = 60`. Sorted:
`[1, 8, 23, 24, 33, 34, 54, 75]`.

| lo val | hi val | sum | action | best |
|--------|--------|-----|--------|------|
| 1  | 75 | 76 | >= 60 -> hi-- | -1 |
| 1  | 54 | 55 | < 60 -> record, lo++ | 55 |
| 8  | 54 | 62 | >= 60 -> hi-- | 55 |
| 8  | 34 | 42 | < 60 -> record, lo++ | 55 |
| 23 | 34 | 57 | < 60 -> record, lo++ | 57 |
| 24 | 34 | 58 | < 60 -> record, lo++ | 58 |
| 33 | 34 | 67 | >= 60 -> hi-- | 58 |

Pointers cross; answer is **58**.

### Why it is correct

Every value is either recorded (when its best-with-current-`hi` pairing is valid)
or discarded only when it provably cannot participate in a valid pair. Because each
iteration advances exactly one pointer, all "frontier" pairs that could be optimal
are considered, so `best` ends at the true maximum.

- **Time:** O(n log n) for the sort, then O(n) for the scan.
- **Space:** O(1) beyond the sort.

## Key Insights & Edge Cases

- **Strictly less than `k`.** Use `s < k`; a pair summing to exactly `k` is invalid,
  which is why Example 3 rejects `2 + 3 = 5`.
- **Initialize `best = -1`** so the "no valid pair" case (Example 2) returns `-1`
  naturally without a special check.
- **Advance `lo` on a hit, not `hi`.** Moving `lo` right is what searches for a
  larger-but-still-valid sum; moving `hi` would only ever shrink the sum.
- **Length 1** cannot form a pair; the `while lo < hi` guard returns `-1` immediately.
