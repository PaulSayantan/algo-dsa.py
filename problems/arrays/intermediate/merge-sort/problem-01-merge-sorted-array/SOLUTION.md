# Solution — Merge Sorted Array

## Brute Force

Copy the first `m` elements of `nums1` and all `n` elements of `nums2` into a new
list, sort it, and write the result back into `nums1`.

```python
merged = nums1[:m] + nums2[:n]
merged.sort()
nums1[:] = merged
```

- **Time:** `O((m + n) log (m + n))` — dominated by the sort. We throw away the
  fact that both inputs are already sorted.
- **Space:** `O(m + n)` for the temporary list.

## Optimal Approach (Merge Sort's merge step, from the back)

Both inputs are already sorted, so we only need the **merge** half of merge sort:
a single linear pass that repeatedly takes the larger of the two front (here,
back) candidates.

The twist is that the output must live inside `nums1`, whose first `m` slots hold
real data. If we merged front-to-back we could clobber a `nums1` value we still
need. The trailing `n` slots, however, are free. So we fill `nums1` **from the
largest value down**, writing into the back:

- `i` points at the last valid element of `nums1` (starts at `m - 1`).
- `j` points at the last element of `nums2` (starts at `n - 1`).
- `k` points at the last slot of `nums1` (starts at `m + n - 1`).

At each step, place the larger of `nums1[i]` and `nums2[j]` at `nums1[k]` and move
that pointer plus `k` leftward.

```python
def merge(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:                       # nums2 not exhausted
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
```

**Why it is correct:** `k` always sits at or ahead of `i` (`k = i + j + 1 >= i`
while `j >= 0`), so we never overwrite a `nums1` element before reading it. Each
value written is the current maximum of the not-yet-placed elements, so the suffix
of `nums1` we build is sorted descending as we go and thus ascending overall. When
`nums2` is exhausted (`j < 0`), any remaining `nums1` elements are already in their
correct sorted positions, so we can stop.

- **Time:** `O(m + n)` — each element is touched once.
- **Space:** `O(1)` — fully in place.

## Key Insights & Edge Cases

- **Merge back-to-front** to reuse `nums1`'s free tail and avoid an auxiliary
  array. Front-to-back merging is fine too but requires a copy of `nums1`.
- The loop condition only needs `j >= 0`: once `nums2` is drained, the rest of
  `nums1` is already correct and untouched.
- **`n == 0`**: nothing to merge, `nums1` is already the answer.
- **`m == 0`**: every `nums1` slot is a placeholder; the whole of `nums2` is copied
  over.
- Watch the `i >= 0` guard: if you run out of `nums1` values first, you must keep
  pulling from `nums2` without indexing `nums1[-1]`.
- Duplicate values across the two arrays (e.g. the two `2`s in Example 1) are
  handled naturally and stably by the comparison.
