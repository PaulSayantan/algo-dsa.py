# Merge Sorted Array — Solution

## Brute Force

Copy `nums2`'s `n` elements into the tail of `nums1`, then sort the whole array.

```python
def merge(nums1, m, nums2, n):
    nums1[m:] = nums2[:n]
    nums1.sort()
```

- **Time:** `O((m + n) log (m + n))` — dominated by the sort.
- **Space:** `O(1)` extra (or `O(m + n)` depending on the sort implementation).

This throws away the fact that both inputs are already sorted, which is exactly the
information the merge exploits.

## Optimal Approach (Two-Pointer Merge)

The tricky part of an *in-place* merge is that if we filled `nums1` from the front, we
could overwrite an element of `nums1` we have not read yet. The fix is to fill **from
the back**, where the free space lives.

Keep three pointers:

- `i = m - 1` — last real element of `nums1`.
- `j = n - 1` — last element of `nums2`.
- `k = m + n - 1` — last slot of `nums1` (the current write position).

Repeatedly compare `nums1[i]` and `nums2[j]`, write the **larger** into `nums1[k]`, and
step the corresponding pointer plus `k` backward.

```python
def merge(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
```

**Why it is correct.** At each step `nums1[k]` receives the largest element not yet
placed, so the suffix `nums1[k..]` is always the correct sorted tail. The write pointer
`k` is always `>= i`, so it never clobbers an unread `nums1` element (there are exactly
as many remaining slots as remaining unmerged elements). The loop can stop once
`j < 0`: any elements still in `nums1` (`i >= 0`) are already in their correct
positions.

**Step-by-step** on `nums1=[1,2,3,0,0,0]`, `nums2=[2,5,6]`:

| Compare | Write | nums1 |
| --- | --- | --- |
| `3` vs `6` -> take 6 | k=5 | `[1,2,3,0,0,6]` |
| `3` vs `5` -> take 5 | k=4 | `[1,2,3,0,5,6]` |
| `3` vs `2` -> take 3 | k=3 | `[1,2,3,3,5,6]` |
| `2` vs `2` -> take 2 (from nums2) | k=2 | `[1,2,2,3,5,6]` |
| j = 0 -> stop; `[1,2]` already placed | | `[1,2,2,3,5,6]` |

- **Time:** `O(m + n)` — each element written exactly once.
- **Space:** `O(1)` — merge happens in place.

## Key Insights & Edge Cases

- **Fill from the back** to reuse the free tail without overwriting live data.
- Guard `i >= 0` in the comparison; when `nums1` is exhausted, all remaining writes must
  come from `nums2`.
- Loop on `j >= 0` (not on both): once `nums2` is drained, `nums1`'s leftover prefix is
  already sorted and in place, so no copying is needed.
- `m == 0`: every real slot comes from `nums2` — the placeholder zeros get overwritten.
- `n == 0`: the loop body never runs; `nums1` is untouched, which is correct.
- Ties: taking from `nums2` on `nums1[i] == nums2[j]` (as above) still yields a correct
  non-decreasing order; either choice works here since we only need sortedness.
