# Solution - 3Sum Closest

## Brute Force

Compute every triplet sum and keep the one nearest `target`.

```python
best = None
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            s = nums[i] + nums[j] + nums[k]
            if best is None or abs(s - target) < abs(best - target):
                best = s
return best
```

- **Time:** O(n^3).
- **Space:** O(1).

## Optimal Approach (Two-Pointer on Sorted Sums)

Sort `nums`. Fix `nums[i]`, then two-pointer sweep the suffix. This is the
*closest-value* variant: rather than needing `s == target`, we minimize
`abs(s - target)`.

### The invariant

Maintain `best`, the closest triplet sum found so far. For a fixed `i`, with
`s = nums[i] + nums[lo] + nums[hi]`:

- Update `best` if `abs(s - target) < abs(best - target)`.
- If `s < target`, we want a larger sum -> `lo += 1`.
- If `s > target`, we want a smaller sum -> `hi -= 1`.
- If `s == target`, distance is 0 — this is optimal, return `target` immediately.

Because the suffix is sorted, moving `lo` right is the *only* way to increase the
sum (with `hi` fixed) and moving `hi` left the only way to decrease it, so the
sweep always steps toward `target`.

### Reference implementation

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = nums[0] + nums[1] + nums[2]   # any valid triplet to seed
        for i in range(n - 2):
            lo, hi = i + 1, n - 1
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                if abs(s - target) < abs(best - target):
                    best = s
                if s < target:
                    lo += 1
                elif s > target:
                    hi -= 1
                else:
                    return s                 # exact match; cannot do better
        return best
```

### Worked trace (Example 1)

`nums = [-1, 2, 1, -4]` sorted -> `[-4, -1, 1, 2]`, `target = 1`.
Seed `best = -4 + -1 + 1 = -4`.

- `i=0` (-4): `lo=1(-1), hi=3(2)` -> `s=-3`, |−3−1|=4 < |−4−1|=5, `best=-3`; `-3<1`
  -> `lo=2`. `lo=2(1), hi=3(2)` -> `s=-1`, |−1−1|=2 < 4, `best=-1`; `-1<1` -> `lo=3`. meet.
- `i=1` (-1): `lo=2(1), hi=3(2)` -> `s=2`, |2−1|=1 < |−1−1|=2, `best=2`; `2>1`
  -> `hi=2`. meet.

Result **2**.

### Why it is correct

For each anchor `i`, the two-pointer scan visits a monotone sequence of sums and
never skips past the closest achievable value: whenever `s < target` the only way to
approach `target` is to raise `s` (advance `lo`), and symmetrically for `s > target`.
Every anchor is tried, so the global closest sum is captured in `best`.

- **Time:** O(n^2) — O(n) scan per anchor, dominating the sort.
- **Space:** O(1) beyond the sort.

## Key Insights & Edge Cases

- **Seed `best` with a real triplet** (e.g. the first three sorted values), not `0`
  or `inf`, so the distance comparison is valid from the start.
- **Early return on exact match** (`s == target`) — distance 0 can never be beaten.
- **Compare distances, not raw sums.** Track `abs(s - target)`; the sign of the sum
  relative to the target only decides which pointer to move.
- **Overshoot below the target is possible** (Example 3): when even the maximum
  triplet sum stays below `target`, the closest is simply the largest reachable sum.
- **Duplicates need no special handling** here — we report a sum, not a set of
  triplets, so skipping equal neighbors is optional (a minor speed-up at most).
