# Solution — Sort an Array

## Brute Force

The most naive "sort" is to repeatedly find the minimum of the *entire remaining* set by rescanning,
building a new output list one element at a time and marking used elements:

```python
def sort_naive(nums):
    used = [False] * len(nums)
    out = []
    for _ in range(len(nums)):
        best = -1
        for j in range(len(nums)):
            if not used[j] and (best == -1 or nums[j] < nums[best]):
                best = j
        used[best] = True
        out.append(nums[best])
    return out
```

- **Time:** `O(n²)` (an inner scan of `n` elements for each of `n` output slots).
- **Space:** `O(n)` for the `used` array and the output list.

This works but wastes `O(n)` extra memory. Selection Sort is essentially this idea done **in place**.

## Optimal Approach (Selection Sort)

Selection Sort keeps a growing **sorted prefix** at the front. For each index `i` from `0` to
`n - 2`, it finds the index of the minimum element in the suffix `nums[i .. n-1]` and swaps that
element into position `i`.

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            if min_idx != i:
                nums[i], nums[min_idx] = nums[min_idx], nums[i]
        return nums
```

### Why it is correct

**Loop invariant:** before iteration `i`, the subarray `nums[0 .. i-1]` contains the `i` smallest
elements of the array, already in sorted order, and all of them are `<=` every element in
`nums[i .. n-1]`.

- *Initialization:* before `i = 0` the prefix is empty, so the invariant holds vacuously.
- *Maintenance:* iteration `i` selects the true minimum of `nums[i .. n-1]` and places it at index
  `i`. Since that minimum is `>=` everything already in the prefix (by the invariant) and `<=`
  everything left behind, the prefix `nums[0 .. i]` remains sorted and stays a lower bound on the
  suffix.
- *Termination:* after `i = n - 2`, the prefix `nums[0 .. n-2]` is sorted and `<= nums[n-1]`, so the
  whole array is sorted.

### Step-by-step on `[5, 2, 3, 1]`

| i | suffix scanned | min found | array after swap |
|---|----------------|-----------|------------------|
| 0 | `[5,2,3,1]`    | `1` @3    | `[1,2,3,5]`      |
| 1 | `[2,3,5]`      | `2` @1    | `[1,2,3,5]`      |
| 2 | `[3,5]`        | `3` @2    | `[1,2,3,5]`      |

Result: `[1, 2, 3, 5]`.

### Complexity

- **Time:** `O(n²)` in **all** cases. The inner loop always runs `(n-1) + (n-2) + ... + 1 = n(n-1)/2`
  comparisons regardless of input order — there is no early exit even on already-sorted input.
- **Space:** `O(1)` — sorting is done in place.
- **Swaps:** at most `n - 1` (one per pass), a notable advantage when writes are costly.

## Key Insights & Edge Cases

- **Single element / empty:** with `n <= 1` the outer loop `range(n - 1)` runs zero times and the
  array is returned unchanged. No special-casing needed.
- **Already sorted:** still costs `O(n²)` comparisons — Selection Sort is *not* adaptive. The
  `if min_idx != i` guard merely skips no-op swaps; it does not reduce the comparison count.
- **Duplicates:** using strict `<` in the min search means the *first* occurrence of the minimum is
  chosen, and equal keys never trigger a swap. Note the in-place swap version is **not stable** — a
  later-appearing equal key can be swapped ahead of an earlier one across passes.
- **Negatives:** integer comparison handles negative numbers with no changes.
- **Off-by-one:** the inner loop starts at `i + 1` (index `i` is the current candidate) and the outer
  loop stops at `n - 2` because the last element is automatically in place once everything else is.
