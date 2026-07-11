# 3Sum — Solution

## Brute Force

Examine every triple of indices `(i, j, k)` with three nested loops, check whether the
three values sum to zero, and deduplicate the results (e.g. by sorting each triplet and
inserting into a set).

- **Time:** `O(n^3)` for the triple loop.
- **Space:** `O(n)`–`O(m)` for the set of unique triplets (`m` = number found).

At `n = 3000`, `n^3 ~ 2.7 * 10^10` — far too slow. Deduping via a set works but adds
overhead and hashing of small lists.

## Optimal Approach (Sorting as Preprocessing)

**Idea:** Sort `nums` ascending. Fix the first element `nums[i]`; the problem reduces to
**2Sum on the sorted suffix** with target `-nums[i]`, which a two-pointer scan solves in
one linear pass. Sorting also makes duplicate skipping trivial: equal values are adjacent,
so you can advance past them.

**Why it is correct:** In a sorted array, for a fixed `i` you want two later elements
summing to `target = -nums[i]`. Place `lo = i+1`, `hi = n-1`. The sum `nums[lo]+nums[hi]`
is monotone in each pointer: if it's too small, only moving `lo` right can increase it;
if it's too large, only moving `hi` left can decrease it. So each pointer moves in one
direction and every valid pair is found without missing any — an `O(n)` sweep per `i`.
Because the array is sorted, all instances of a value are contiguous, so skipping equal
neighbors at each of the three positions guarantees each *value*-triplet is emitted once.

**Step by step:**

1. Sort `nums`.
2. For `i` from `0` to `n-3`:
   - If `nums[i] > 0`, break — no way for three ascending values starting positive to sum
     to 0.
   - If `i > 0` and `nums[i] == nums[i-1]`, skip (avoid duplicate first element).
   - Set `lo = i+1`, `hi = n-1`, `target = -nums[i]`.
   - While `lo < hi`:
     - `s = nums[lo] + nums[hi]`.
     - If `s < target`: `lo += 1`. If `s > target`: `hi -= 1`.
     - If `s == target`: record `[nums[i], nums[lo], nums[hi]]`, then advance both
       pointers past any duplicates.
3. Return the collected triplets.

```python
def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        lo, hi, target = i + 1, n - 1, -nums[i]
        while lo < hi:
            s = nums[lo] + nums[hi]
            if s < target:
                lo += 1
            elif s > target:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
                while lo < hi and nums[hi] == nums[hi + 1]:
                    hi -= 1
    return res
```

- **Time:** `O(n log n)` for the sort plus `O(n^2)` for the outer loop times the inner
  two-pointer sweep, so `O(n^2)` overall.
- **Space:** `O(1)` auxiliary beyond the output (ignoring sort internals).

## Key Insights & Edge Cases

- **Sorting does double duty:** it enables the monotone two-pointer scan *and* makes
  duplicate elimination a matter of skipping adjacent equal values — no hash set needed.
- **Early `break` when `nums[i] > 0`:** since the array is sorted, once the fixed element
  is positive the two larger elements are also positive and can't sum to zero.
- **Skip duplicates at all three positions:** the outer `i` skip prevents repeated first
  elements; the two inner `while` loops prevent repeated pairs after a hit.
- **All zeros** (`[0,0,0,0]`): yields exactly one `[0,0,0]` thanks to the dedup skips.
- **Fewer than 3 elements** can't occur under the constraints (`n >= 3`), but the loop
  bound `range(n-2)` handles small `n` safely regardless.
- **Advance both pointers on a hit:** moving only one would immediately re-hit the same
  target with the other pointer stuck, so both must move.
