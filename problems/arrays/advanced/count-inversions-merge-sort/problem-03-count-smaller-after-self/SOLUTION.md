# Solution — Count of Smaller Numbers After Self

## Brute Force

For each `i`, scan everything to its right and count strictly smaller values.

```python
def countSmaller_brute(nums):
    n = len(nums)
    counts = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] < nums[i]:
                counts[i] += 1
    return counts
```

- **Time:** `O(n^2)`.
- **Space:** `O(n)` for the output (or `O(1)` extra).

Too slow at `n = 10^5`.

## Optimal Approach — Count Inversions (Merge Sort)

This is inversion counting where each inversion must be **attributed to its left
endpoint** rather than tallied globally. To keep track of which answer slot to
credit after we start reordering values, we sort an array of **indices** by their
`nums` value instead of sorting the values directly.

Carry an index array `idx` (initially `0..n-1`) through merge sort, ordering it
by `nums[idx[...]]` ascending. During a merge of the left block `idx[lo:mid]` and
right block `idx[mid:hi]` (both already value-sorted):

- Keep a running counter `right_placed` of how many right-block elements have
  been emitted so far in this merge.
- When we emit a **right** element because it is strictly smaller than the
  current left element, increment `right_placed`.
- When we emit a **left** element (index `p = idx[i]`), add `right_placed` to
  `counts[p]`. Every right element emitted before it is strictly smaller **and**
  sits to its right in the original array (the whole right block does), so it is
  a valid "smaller-after-self" element for `p`.

Using strict `<` to decide "take from right" ensures equal values are not
counted (equal right elements are emitted *after* the left element).

### Why it is correct

At the instant we emit left index `p`, `right_placed` equals the number of
right-block elements with value strictly less than `nums[p]` — because in an
ascending merge every element smaller than `nums[p]` is emitted before `p`. Each
such right element is to the right of `p` in the original ordering. Summing over
all merge levels accumulates, for each `p`, the count of every strictly-smaller
element that lies to its right, since each right-of-`p`-and-smaller element ends
up in the right block relative to `p` at exactly one level of the recursion.

### Step-by-step on `nums = [5, 2, 6, 1]`

- Sort indices of `[5,2]`: emitting `1`(=2) before `0`(=5) credits
  `counts[0] += 1`. Block becomes indices `[1,0]`.
- Sort indices of `[6,1]`: emitting `3`(=1) before `2`(=6) credits
  `counts[2] += 1`. Block becomes `[3,2]`.
- Merge value-blocks `[2,5]` (idx `[1,0]`) and `[1,6]` (idx `[3,2]`):
  - emit `1` (right, value 1) → `right_placed = 1`
  - emit index `1` (value 2, left) → `counts[1] += 1`
  - emit index `0` (value 5, left) → `counts[0] += 1` (now `2`)
  - emit index `2` (value 6, right)
- Final `counts = [2, 1, 1, 0]`. ✓

### Reference implementation

```python
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * n
        idx = list(range(n))  # indices, reordered by value during merges

        def sort_count(lo: int, hi: int) -> None:
            if hi - lo <= 1:
                return
            mid = (lo + hi) // 2
            sort_count(lo, mid)
            sort_count(mid, hi)
            merged = []
            i, j = lo, mid
            right_placed = 0
            while i < mid and j < hi:
                if nums[idx[j]] < nums[idx[i]]:   # strict: right is smaller
                    right_placed += 1
                    merged.append(idx[j]); j += 1
                else:
                    counts[idx[i]] += right_placed
                    merged.append(idx[i]); i += 1
            while i < mid:
                counts[idx[i]] += right_placed
                merged.append(idx[i]); i += 1
            while j < hi:
                merged.append(idx[j]); j += 1
            idx[lo:hi] = merged

        sort_count(0, n)
        return counts
```

- **Time:** `O(n log n)`.
- **Space:** `O(n)` for the index array and merge buffer, plus `O(log n)` stack.

## Key Insights & Edge Cases

- **Sort indices, not values.** You must know which original position to credit,
  so the sortable unit is the index (with its value looked up on demand).
- **Credit the left element.** Unlike the plain total-count problem where you add
  when taking from the right, here you add the accumulated `right_placed` when
  emitting the *left* element — you're attributing the inversion to its left end.
- **Strict `<` for duplicates.** Equal values must not count; taking from the
  right only on strict `<` guarantees this.
- **Don't forget the tail.** When the right block empties first, the remaining
  left elements must still receive the full `right_placed` credit — handle it in
  the "drain left" loop.
- **Single element:** answer `[0]`. All-equal array: all zeros.
- An alternative is a Binary Indexed Tree over coordinate-compressed values;
  merge sort avoids the compression step and is equally `O(n log n)`.
