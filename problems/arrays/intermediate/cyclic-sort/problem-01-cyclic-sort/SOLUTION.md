# Solution — Cyclic Sort

## Brute Force

Just call a general-purpose sort (`nums.sort()` or merge/quick sort).

- **Time:** O(n log n) — comparison sort lower bound.
- **Space:** O(1) for an in-place sort like heapsort, O(n) for merge sort.

This works but ignores the special structure: the values are exactly `1..n`, so we
can do better than the comparison lower bound.

## Optimal Approach (Cyclic Sort)

Because the array is a permutation of `1..n`, value `v` has one and only one correct
home: index `v - 1`. Walk the array with a pointer `i`:

1. Compute the target index for the current element: `j = nums[i] - 1`.
2. If `nums[i]` is not already at its home (`nums[i] != nums[j]`), swap
   `nums[i]` and `nums[j]`. This sends `nums[i]` to its correct slot.
3. Otherwise the current slot is settled — advance `i`.

Note that we do **not** advance `i` after a swap: the value we just pulled into
position `i` may itself be out of place, so we re-examine it.

```python
def cyclic_sort(nums):
    i = 0
    n = len(nums)
    while i < n:
        j = nums[i] - 1          # correct index for value nums[i]
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return nums
```

### Why it is correct

Every swap places at least one element (`nums[i]`) permanently at its correct index,
and a settled element is never moved again. There are `n` elements, so at most `n`
"home-placing" swaps happen. When the loop finishes, every value `v` sits at index
`v - 1`, i.e. the array is sorted `1, 2, ..., n`.

### Step-by-step on `[3, 1, 5, 4, 2]`

```
i=0: nums[0]=3 -> home idx 2. nums[2]=5 != 3, swap -> [5, 1, 3, 4, 2]
i=0: nums[0]=5 -> home idx 4. nums[4]=2 != 5, swap -> [2, 1, 3, 4, 5]
i=0: nums[0]=2 -> home idx 1. nums[1]=1 != 2, swap -> [1, 2, 3, 4, 5]
i=0: nums[0]=1 -> home idx 0. nums[0]=1 == 1, advance i=1
i=1..4: each already home, advance
Result: [1, 2, 3, 4, 5]
```

### Complexity

- **Time:** O(n). The `while` executes at most `2n` times: each of the `n`
  iterations either advances `i` (at most `n` times) or performs a swap that
  finalizes one element (at most `n` times).
- **Space:** O(1) — everything happens in place.

## Key Insights & Edge Cases

- **Guard the swap with a value comparison, not an index comparison.** Comparing
  `nums[i] != nums[j]` (values) rather than `i != j` is what makes the general
  pattern robust when duplicates appear in sibling problems. Here values are
  unique, so either guard works, but building the habit pays off later.
- **Never advance `i` right after a swap** — recheck the element that just arrived.
- **Single element / already sorted arrays** are handled naturally with zero swaps.
- This exact skeleton is the foundation for Missing Number, Find All Duplicates,
  Set Mismatch, and First Missing Positive.
