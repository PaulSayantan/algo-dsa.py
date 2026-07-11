# Solution - 3Sum

## Brute Force

Check every triplet and collect those summing to zero, de-duplicating with a set of
sorted tuples.

```python
seen = set()
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if nums[i] + nums[j] + nums[k] == 0:
                seen.add(tuple(sorted((nums[i], nums[j], nums[k]))))
return [list(t) for t in seen]
```

- **Time:** O(n^3).
- **Space:** O(number of triplets) for the de-dup set.

## Optimal Approach (Two-Pointer on Sorted Sums)

Sort `nums`. Fix the first element `nums[i]`; the remaining task is a **2-Sum to
target `-nums[i]`** on the sorted suffix `nums[i+1 ..]`, solved with two pointers.

### The core scan

For a fixed `i`, set `lo = i + 1`, `hi = n - 1`, and let `s = nums[i] + nums[lo] + nums[hi]`:

- `s == 0`: record `[nums[i], nums[lo], nums[hi]]`, then move **both** inward.
- `s < 0`: the sum is too small -> `lo += 1` (increase it).
- `s > 0`: the sum is too large -> `hi -= 1` (decrease it).

### De-duplication (the part that trips people up)

Sorting places equal values adjacently, so skip repeats at three points:

1. **Outer `i`:** if `nums[i] == nums[i-1]`, skip — this first value was already the
   anchor of a completed scan.
2. **After recording a hit, advance `lo` past equal values** and `hi` past equal
   values, so the same triplet is not emitted twice.

An early `break` when `nums[i] > 0` is a nice optimization: once the smallest of the
three is positive, no triplet can sum to zero.

### Reference implementation

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 2):
            if nums[i] > 0:
                break                       # smallest is positive -> impossible
            if i > 0 and nums[i] == nums[i - 1]:
                continue                    # skip duplicate anchor
            lo, hi = i + 1, n - 1
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                if s < 0:
                    lo += 1
                elif s > 0:
                    hi -= 1
                else:
                    res.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1             # skip duplicate second value
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1             # skip duplicate third value
        return res
```

### Worked trace (Example 1)

`nums = [-1, 0, 1, 2, -1, -4]` sorted -> `[-4, -1, -1, 0, 1, 2]`.

- `i=0` (-4): target 4 in suffix; pointers scan `[-1..2]`, max pair `-1 + 2 = 1 < 4`
  throughout, no hit.
- `i=1` (-1): `lo=2 (-1), hi=5 (2)` -> `-1 + -1 + 2 = 0` -> record `[-1,-1,2]`,
  advance to `lo=3 (0), hi=4 (1)` -> `-1 + 0 + 1 = 0` -> record `[-1,0,1]`. Pointers meet.
- `i=2` is also `-1` but equals `nums[1]` -> skipped (dedup).
- `i=3` (0) > ... continues but no further zero-sum triplets.

Result: `[[-1,-1,2], [-1,0,1]]`.

### Why it is correct

For each fixed smallest element, the two-pointer scan is an exhaustive, monotone
sweep that finds every pair summing to `-nums[i]` (same discard invariant as Two Sum
II). Skipping equal anchors and equal pointer values guarantees each *distinct*
triplet is emitted exactly once.

- **Time:** O(n^2) — an O(n) scan per anchor, dominating the O(n log n) sort.
- **Space:** O(1) auxiliary (excluding the output list and sort internals).

## Key Insights & Edge Cases

- **Skip duplicates in all three places** (anchor, `lo`, `hi`) or you will emit
  repeats such as two copies of `[-1, 0, 1]`.
- **Move both pointers after a hit.** Moving only one guarantees the next sum is off
  target, wasting work and risking a duplicate.
- **`nums[i] > 0` break** is safe only *after* sorting — it relies on all later
  elements being at least as large.
- **All zeros** (`[0,0,0]`) yields exactly one triplet thanks to the dedup skips.
- **Fewer than 3 elements** cannot form a triplet; `range(n - 2)` handles it.
