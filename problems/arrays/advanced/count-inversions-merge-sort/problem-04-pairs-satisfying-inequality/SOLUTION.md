# Solution — Number of Pairs Satisfying Inequality

## Brute Force

Form `d[k] = nums1[k] - nums2[k]`, then test every pair.

```python
def numberOfPairs_brute(nums1, nums2, diff):
    n = len(nums1)
    d = [nums1[k] - nums2[k] for k in range(n)]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if d[i] <= d[j] + diff:
                count += 1
    return count
```

- **Time:** `O(n^2)`.
- **Space:** `O(n)` for `d`.

Too slow for `n = 10^5`.

## Optimal Approach — Count Inversions (Merge Sort)

**Step 1 — reduce to one array.** The condition
`nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff` rearranges (all terms with
index `i` on the left, index `j` on the right) to

```
(nums1[i] - nums2[i]) <= (nums1[j] - nums2[j]) + diff
```

so with `d[k] = nums1[k] - nums2[k]` we must count pairs `i < j` with
`d[i] <= d[j] + diff`. This is a "cross-pair" count on a single array — the
merge-sort inversion pattern, just with a `<=`/`+diff` predicate instead of `>`.

**Step 2 — count cross pairs during merge.** Run merge sort on `d`. In a merge,
the left block `d[lo:mid]` holds the smaller original indices and the right block
`d[mid:hi]` the larger ones — so a left element is always a valid `i` and a right
element a valid `j`. Both blocks are sorted ascending. For each right element
`d[j]`, the qualifying left elements are exactly those with `d[i] <= d[j] + diff`,
which form a **prefix** of the sorted left block. Sweep a left pointer `p`
forward: as `d[j]` increases, the threshold `d[j] + diff` increases, so `p` only
moves forward — a monotone two-pointer. Add `p`'s position (count of qualifying
left elements) for each right element. Then perform the ordinary merge to keep
`d` sorted for the parent.

### Why it is correct

Left block = indices `< mid`, right block = indices `>= mid`, so `i < j` is
automatically satisfied for every cross pair we count — no pair is double-counted
or missed across the `i < j` boundary. For a fixed right index `j`, the number of
left indices with `d[i] <= d[j] + diff` is precisely the length of the sorted
prefix `p`, because the left block is sorted ascending. Pairs within a single
block are handled by recursion; the three groups (left-only, right-only, cross)
partition all pairs `i < j`.

### Step-by-step on `d = [1, 0, 4]`, `diff = 1`

- Split `[1]` and `[0, 4]` (indices `{0}` and `{1,2}`).
- Right recursion on `[0, 4]`: merge blocks `[0]`(idx1) and `[4]`(idx2). Count
  pairs with left idx 1, right idx 2: `d[1]=0 <= d[2]+1 = 5` → `+1`. Sorted `[0,4]`.
- Top merge: left `[1]` (idx0), right `[0, 4]` (idx1, idx2), sorted ascending.
  - right elem `0` (idx1): qualifying left with `d[i] <= 0+1 = 1`: `d[0]=1 <= 1`
    → prefix length `1` → `+1`.
  - right elem `4` (idx2): qualifying left with `d[i] <= 4+1 = 5`: still `1` →
    `+1`.
  - cross count here = `2`.
- Total = `1 + 2 = 3`. ✓

### Reference implementation

```python
from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        d = [a - b for a, b in zip(nums1, nums2)]

        def sort_count(arr: List[int]) -> int:
            n = len(arr)
            if n <= 1:
                return 0
            mid = n // 2
            left, right = arr[:mid], arr[mid:]
            cnt = sort_count(left) + sort_count(right)

            # counting phase: for each right value, count left values <= right + diff
            p = 0
            for rv in right:
                while p < len(left) and left[p] <= rv + diff:
                    p += 1
                cnt += p

            # merge phase
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]; i += 1
                else:
                    arr[k] = right[j]; j += 1
                k += 1
            while i < len(left):
                arr[k] = left[i]; i += 1; k += 1
            while j < len(right):
                arr[k] = right[j]; j += 1; k += 1
            return cnt

        return sort_count(d)
```

- **Time:** `O(n log n)`.
- **Space:** `O(n)` for `d` and the temporary halves, plus `O(log n)` stack.

## Key Insights & Edge Cases

- **Algebra first.** The single most important step is collapsing two arrays into
  `d[k] = nums1[k] - nums2[k]`; after that it is a standard cross-pair count.
- **Inclusive comparison.** The predicate is `<=`, so count using `<=` in the
  counting sweep. Using `<` would drop the boundary pairs (see Example 1, pair
  `(0,1)` where `1 <= 1`).
- **Monotone pointer.** Since we iterate right values in ascending order and the
  left block is sorted, the left prefix pointer only advances — resetting it per
  right element would be `O(n^2)`.
- **Negative diff.** `diff` may be negative (Example 2); the same logic works
  because `rv + diff` can be less than every left value, giving prefix length 0.
- **Value range.** `d` ranges in `[-2*10^4, 2*10^4]` and the count up to
  `~5*10^9`; use 64-bit accumulators outside Python.
