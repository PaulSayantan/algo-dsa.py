# Solution — Binary Insertion Sort

## Brute Force (plain insertion sort)

Ordinary insertion sort scans the sorted prefix right-to-left, comparing the key against each
element until it finds the slot, shifting as it goes. For element `i` this costs up to `i`
comparisons **and** up to `i` shifts.

- Comparisons: `O(n^2)` in the worst case.
- Shifts (data moves): `O(n^2)` in the worst case.
- Space: `O(1)`.

Correct and simple, but every insertion may do a linear number of comparisons even though the
prefix is already sorted — that is wasted work when comparisons are expensive.

## Optimal Approach (Binary Insertion Sort)

Because the prefix `nums[0..i-1]` is already sorted, we can find where `key = nums[i]` belongs
with **binary search** instead of a linear scan.

To keep the sort **stable**, we search for the **upper bound**: the first index `pos` in
`[0, i)` whose value is *strictly greater* than `key`. Any element equal to `key` therefore
stays to the left of `key`, preserving original order.

Steps for each `i` from `1` to `n-1`:

1. `key = nums[i]`.
2. Binary search in `nums[0..i-1]` for `pos`, the upper-bound index of `key`.
3. Shift `nums[pos..i-1]` one slot right (elements from `pos` up to `i-1` move to `pos+1..i`).
4. Place `key` at index `pos`.

```python
def binaryInsertionSort(self, nums):
    for i in range(1, len(nums)):
        key = nums[i]
        lo, hi = 0, i                 # search within the sorted prefix [0, i)
        while lo < hi:                # find upper bound of key -> keeps it stable
            mid = (lo + hi) // 2
            if nums[mid] <= key:
                lo = mid + 1
            else:
                hi = mid
        pos = lo
        # shift the tail of the prefix right, then drop key in
        for j in range(i, pos, -1):
            nums[j] = nums[j - 1]
        nums[pos] = key
    return nums
```

**Why it is correct.** Same loop invariant as insertion sort: `nums[0..i-1]` is sorted before
iteration `i`. Binary search returns the unique index `pos` such that everything in
`nums[0..pos-1]` is `<= key` and everything in `nums[pos..i-1]` is `> key`; shifting and
inserting there keeps `nums[0..i]` sorted. Using `<=` in the search (upper bound) makes the
insertion point land *after* equal elements, so the sort is stable.

- Comparisons: `O(n log n)` total — each of the `n` elements uses `O(log i)` comparisons.
- Data moves (shifts): still `O(n^2)` worst case — inserting near the front moves many
  elements. So overall running time stays `O(n^2)`; only the comparison count improves.
- Space: `O(1)` — in place.

## Key Insights & Edge Cases

- **It saves comparisons, not moves.** The array elements still have to physically shift, so
  the `O(n^2)` time bound is unchanged. The win is when comparisons are far more expensive
  than moves (long strings, complex objects, network/DB comparisons).
- **Upper bound = stability.** Searching for the first element `> key` (treating equals as
  "go right") places new equal keys after existing ones. Searching for the first element
  `>= key` would instead be lower bound and could break stability.
- **Already-sorted input** makes each binary search return `pos = i`, so no shifting happens —
  but each element still costs `O(log i)` comparisons, unlike plain insertion sort's `O(1)`
  best case. Plain insertion sort has the better best case; binary insertion sort has the
  better average comparison count.
- **Empty / single element** returns immediately (outer loop starts at `i = 1`).
- **Off-by-one in the shift loop.** Shift from `i` down to `pos+1`, copying `nums[j-1]` into
  `nums[j]`; then write `key` at `pos`. Getting the loop bound wrong overwrites `key`'s slot.
