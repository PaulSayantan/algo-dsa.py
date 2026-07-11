# Solution - 3Sum Smaller

## Brute Force

Enumerate all triplets `i < j < k` and count those whose sum is below `target`.

```python
count = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if nums[i] + nums[j] + nums[k] < target:
                count += 1
return count
```

- **Time:** O(n^3).
- **Space:** O(1).

## Optimal Approach (Two-Pointer on Sorted Sums)

Sort `nums`. Fix the leftmost index `i`, then count qualifying **pairs** in the
suffix `nums[i+1 ..]` using two pointers `lo` and `hi`. This is the *counting*
flavor of the k-Sum family.

### The batch-counting trick

With the suffix sorted, look at `s = nums[i] + nums[lo] + nums[hi]`:

- If `s < target`, then the triplet with the largest partner already qualifies.
  Crucially, **every** `hi'` with `lo < hi' <= hi` gives an even smaller (or equal)
  sum, so all `hi - lo` pairs `(lo, lo+1), (lo, lo+2), ..., (lo, hi)` qualify at
  once. Add `hi - lo` to the count, then move `lo += 1` to explore larger left values.
- If `s >= target`, the sum is too big; even the smallest partner `nums[lo]` cannot
  help, so move `hi -= 1` to shrink the sum.

The `hi - lo` batch jump is what turns an O(n^2)-per-`i` count into O(n)-per-`i`.

### Reference implementation

```python
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n - 2):
            lo, hi = i + 1, n - 1
            while lo < hi:
                if nums[i] + nums[lo] + nums[hi] < target:
                    count += hi - lo   # all pairs (lo, lo+1..hi) qualify
                    lo += 1
                else:
                    hi -= 1
        return count
```

### Worked trace (Example 1)

`nums = [-2, 0, 1, 3]` (already sorted), `target = 2`.

- `i = 0` (value -2), `lo=1, hi=3`: `-2 + 0 + 3 = 1 < 2` -> add `hi - lo = 2`,
  `lo=2`. Now `-2 + 1 + 3 = 2`, not `< 2` -> `hi=2`. Pointers meet. Subtotal 2.
- `i = 1` (value 0), `lo=2, hi=3`: `0 + 1 + 3 = 4 >= 2` -> `hi=2`. Pointers meet.
  Subtotal 0.

Total = **2**, matching the two triplets `[-2,0,1]` and `[-2,0,3]`.

### Why it is correct

For a fixed `i`, each valid pair `(j, k)` in the suffix is counted exactly once: the
batch add `hi - lo` accounts for all pairs sharing the current `lo` and any partner
up to `hi`, and we then advance `lo` past them. No pair is double-counted because
`i < j < k` forces a strict ordering and each `lo` is processed once.

- **Time:** O(n^2) — an O(n) two-pointer scan for each of the `n` choices of `i`.
- **Space:** O(1) beyond the sort (O(log n) to O(n) for the sort's internals).

## Key Insights & Edge Cases

- **Count, don't move one at a time.** The `count += hi - lo` batch is the whole
  point; incrementing by 1 and then `lo += 1` would miss the pairs in between.
- **Strict `<`.** Example 1's `[-2, 1, 3]` sums to exactly `2` and is excluded.
- **Empty or tiny arrays.** With `n < 3` the `range(n - 2)` loop never runs (or the
  inner `while` never triggers), correctly returning `0` — Example 2 handled for free.
- **Duplicates are counted by index, not value.** `[0,0,0]` yields one triplet;
  unlike 3Sum we do *not* skip equal neighbors here because we want the index count.
