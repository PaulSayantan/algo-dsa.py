# 3Sum — Solution

## Brute Force

Check every triple `(i, j, k)` with `i < j < k`, keep those summing to zero, and
deduplicate (e.g. by storing each sorted triplet in a set).

```python
seen = set()
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if nums[i] + nums[j] + nums[k] == 0:
                seen.add(tuple(sorted((nums[i], nums[j], nums[k]))))
return [list(t) for t in seen]
```

- **Time:** `O(n^3)` — all triples.
- **Space:** `O(m)` for the set of found triplets.

With `n = 3000` this is ~`2.7 * 10^10` operations — too slow. Sorting plus two
pointers reduces it to `O(n^2)`.

## Optimal Approach (Two Pointers, opposite ends)

Sort `nums`. Then, for each index `i`, reduce the problem to a **two-sum on the
sorted suffix**: find pairs in `nums[i+1..n-1]` that sum to `-nums[i]`, using the
opposite-ends technique.

1. Sort `nums` ascending.
2. For `i` from `0` to `n - 3`:
   - If `nums[i] > 0`, break — the smallest of the three is already positive, so
     no zero-sum triplet remains.
   - If `i > 0` and `nums[i] == nums[i-1]`, skip this `i` to avoid duplicate
     triplets rooted at the same value.
   - Set `left = i + 1`, `right = n - 1`, `target = -nums[i]`.
   - While `left < right`:
     - `s = nums[left] + nums[right]`.
     - If `s == target`: record `[nums[i], nums[left], nums[right]]`. Then move
       both pointers inward and **skip duplicates**: advance `left` past equal
       values and retreat `right` past equal values.
     - If `s < target`: `left += 1` (need a larger sum).
     - If `s > target`: `right -= 1` (need a smaller sum).

**Why it is correct.** After sorting, the inner search is exactly Two Sum II on a
sorted range, whose opposite-ends pointer logic is provably complete: at each
step the pair sum tells you unambiguously which side to discard. Fixing every
possible smallest element `i` and solving the remaining two-sum covers all
triplets. The duplicate-skipping (for `i`, and for `left`/`right` after a match)
guarantees each unique value-combination is emitted once.

```python
def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    res: List[List[int]] = []
    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        target = -nums[i]
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif s < target:
                left += 1
            else:
                right -= 1
    return res
```

- **Time:** `O(n^2)` — an `O(n)` two-pointer sweep for each of the `n` choices of
  `i`; the initial sort is `O(n log n)`.
- **Space:** `O(1)` auxiliary beyond the output (or `O(n)` if the sort is not
  in place); the result list is separate.

## Key Insights & Edge Cases

- **Sort first.** Sorting is what enables both the two-pointer sweep *and* easy
  duplicate skipping (equal values become adjacent).
- **Three levels of dedup:** skip repeated `i`; after recording a hit, skip
  repeated `left` and repeated `right`. Missing any of these produces duplicate
  triplets.
- **Early break** when `nums[i] > 0`: since the array is sorted, all later
  elements are also positive, so no triplet can sum to zero.
- **All zeros** (`[0, 0, 0, 0]`): produces exactly `[[0, 0, 0]]` thanks to the
  `i`-level and pointer-level skips.
- **Fewer than 3 elements** can't form a triplet; the loop range handles this
  naturally (it simply doesn't execute).
- Move **both** pointers after a match — advancing only one and re-testing wastes
  work and complicates dedup.
