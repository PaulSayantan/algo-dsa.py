# Solution - 3Sum

## Brute Force

Check every triple of indices and collect those summing to zero, de-duplicating
with a set of sorted tuples.

```python
result = set()
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if nums[i] + nums[j] + nums[k] == 0:
                result.add(tuple(sorted((nums[i], nums[j], nums[k]))))
return [list(t) for t in result]
```

- **Time:** `O(n^3)`.
- **Space:** `O(number of triplets)` for the dedup set.

Far too slow for `n` up to `3000` (`~2.7 * 10^10` triples).

## Optimal Approach (Sort + Two Pointers)

1. **Sort** `nums` ascending. Now equal values are adjacent, which both enables
   the two-pointer inner scan and makes duplicate-skipping easy.
2. **Fix** the first element with index `i`, iterating `i` from `0` upward. The
   target for the remaining pair is `-nums[i]`.
3. **Two-pointer** the subarray to the right of `i`: set `left = i + 1`,
   `right = n - 1`. Let `s = nums[i] + nums[left] + nums[right]`.
   - If `s == 0`, record the triplet, then move **both** pointers inward,
     skipping over any values equal to the ones just used.
   - If `s < 0`, increase the sum with `left += 1`.
   - If `s > 0`, decrease the sum with `right -= 1`.
4. **Skip duplicates for `i`:** if `nums[i] == nums[i - 1]`, continue, so each
   distinct anchor value is used once.
5. **Early exit:** once `nums[i] > 0`, no triplet with a positive smallest
   element can sum to zero, so stop.

### Why it is correct

After sorting, for each anchor `i` the inner routine is exactly Two Sum II on
`nums[i+1:]` looking for target `-nums[i]`; by the same converging-pointer
argument (see Problem 1) it finds every qualifying pair. Ranging `i` over all
anchors covers every triplet at least once. Duplicate triplets are avoided by
three skips: (a) skipping repeated anchor values, and (b, c) skipping repeated
`left`/`right` values after a hit — so each distinct value-combination is emitted
exactly once even when values repeat in the input.

### Step-by-step (nums = [-1, 0, 1, 2, -1, -4])

Sorted: `[-4, -1, -1, 0, 1, 2]`.

- `i = 0` (`-4`), target `4`, scan `[-1,-1,0,1,2]`: max pair sum `1 + 2 = 3 < 4`,
  never reaches 4 → no triplet.
- `i = 1` (`-1`), target `1`, scan `[-1,0,1,2]`:
  - left=`-1`, right=`2`: sum `1` → hit `[-1,-1,2]`; move inward, skip dups.
  - left=`0`, right=`1`: sum `1` → hit `[-1,0,1]`; move inward → pointers cross.
- `i = 2` (`-1`): equals `nums[1]`, **skip** (avoids duplicate `[-1,0,1]`).
- `i = 3` (`0`): `0 > 0`? no. target `0`, scan `[1,2]`: sum `3 > 0` → right--,
  pointers cross → no triplet.
- `i = 4` (`1`): `1 > 0` → early exit.

Result: `[[-1, -1, 2], [-1, 0, 1]]`.

### Reference implementation

```python
def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    result: List[List[int]] = []
    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1
    return result
```

- **Time:** `O(n^2)` — `O(n log n)` sort plus, for each of `n` anchors, a linear
  two-pointer scan.
- **Space:** `O(1)` extra beyond the output (or `O(n)` if the sort is not in
  place).

## Key Insights & Edge Cases

- **Sorting is the enabler.** It turns the inner search into Two Sum II and makes
  duplicates adjacent so they are cheap to skip.
- **Three separate skip guards** are needed: one for the anchor `i`, and one each
  for `left` and `right` after a successful hit. Forgetting any of them yields
  duplicate triplets (e.g. `[-1, 0, 1]` twice in Example 1).
- **All zeros** (`[0, 0, 0]`): anchor `0`, pair `0 + 0` hits target `0`, and the
  anchor-skip prevents a second emission → `[[0, 0, 0]]` (Example 3).
- **No solution** (`[0, 1, 1]`): the only triple sums to `2`, so the result is
  empty (Example 2).
- **Early break on `nums[i] > 0`** is a valid optimization because a sorted array
  with a positive smallest chosen element cannot sum to zero.
