# Solution - 4Sum

## Brute Force

Enumerate all quadruplets with four nested loops and de-duplicate via a set of
sorted tuples.

```python
seen = set()
for a in range(n):
    for b in range(a + 1, n):
        for c in range(b + 1, n):
            for d in range(c + 1, n):
                if nums[a] + nums[b] + nums[c] + nums[d] == target:
                    seen.add(tuple(sorted((nums[a], nums[b], nums[c], nums[d]))))
return [list(t) for t in seen]
```

- **Time:** O(n^4).
- **Space:** O(number of quadruplets).

## Optimal Approach (Two-Pointer on Sorted Sums)

4Sum is the k = 4 instance of the general reduction: **fix the outer `k - 2` = 2
indices** with nested loops, then solve the remaining **2-Sum to
`target - nums[i] - nums[j]`** on the sorted suffix with two pointers.

### Structure

1. Sort `nums`.
2. Outer loop `i` from `0`; second loop `j` from `i + 1`.
3. Inner two-pointer scan with `lo = j + 1`, `hi = n - 1` looking for
   `nums[lo] + nums[hi] == target - nums[i] - nums[j]`.
4. **Skip duplicates at every level:** for `i` (when `nums[i] == nums[i-1]`), for `j`
   (when `nums[j] == nums[j-1]`), and for `lo`/`hi` after recording a hit.

### Reference implementation

```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                lo, hi = j + 1, n - 1
                need = target - nums[i] - nums[j]
                while lo < hi:
                    s = nums[lo] + nums[hi]
                    if s < need:
                        lo += 1
                    elif s > need:
                        hi -= 1
                    else:
                        res.append([nums[i], nums[j], nums[lo], nums[hi]])
                        lo += 1
                        hi -= 1
                        while lo < hi and nums[lo] == nums[lo - 1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi + 1]:
                            hi -= 1
        return res
```

### Worked trace (Example 1)

`nums = [1, 0, -1, 0, -2, 2]` sorted -> `[-2, -1, 0, 0, 1, 2]`, `target = 0`.

- `i=0 (-2), j=1 (-1)`: need `0 - (-2) - (-1) = 3`. Scan `[0,0,1,2]`: `0+2=2<3` lo++,
  `0+2=2<3` lo++, `1+2=3` hit -> `[-2,-1,1,2]`. -> quadruplet 1.
- `i=0 (-2), j=2 (0)`: need `2`. Scan `[0,1,2]`: `0+2=2` hit -> `[-2,0,0,2]`.
  -> quadruplet 2.
- `i=0 (-2), j=3 (0)`: `nums[3]==nums[2]` -> skipped (dedup on `j`).
- `i=1 (-1), j=2 (0)`: need `1`. Scan `[0,1,2]`: `0+2=2>1` hi--, `0+1=1` hit
  -> `[-1,0,0,1]`. -> quadruplet 3.
- Remaining anchors yield nothing new.

Result: `[[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]`.

### Why it is correct

Fixing `(i, j)` reduces the problem to the proven 2-Sum-on-sorted scan, which finds
every valid pair in the suffix. Iterating `(i, j)` over all ordered pairs covers all
quadruplets, and the per-level duplicate skips ensure each *distinct value multiset*
is output exactly once.

- **Time:** O(n^3) — two nested loops (O(n^2)) times an O(n) inner scan. This is the
  general k-Sum bound O(n^(k-1)) at k = 4.
- **Space:** O(1) auxiliary beyond the output and sort.

## Key Insights & Edge Cases

- **Watch for integer overflow in other languages.** With values up to 10^9, four of
  them can exceed 32-bit range; use 64-bit sums (Python integers are unbounded, so
  this is only a concern when porting).
- **De-dup at all four positions** (`i`, `j`, `lo`, `hi`). Missing the `j`-level skip
  is the classic bug that produces duplicate quadruplets like two copies of `[-2,0,0,2]`.
- **The `j > i + 1` guard** (not `j > 0`) ensures we only skip a duplicate `j`
  *within the same `i`*, never the first `j` of a fresh anchor.
- **All-equal arrays** (`[2,2,2,2,2]`) collapse to a single quadruplet thanks to the
  skips.
- **Generalizes to any k.** Recurse: peel outer indices until 2 remain, then run the
  two-pointer scan — the same template powers 5Sum, 6Sum, and beyond.
