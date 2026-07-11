# Intersection of Two Arrays II — Solution

## Brute Force

Count occurrences in one array with a hash map, then walk the other array decrementing
counts and emitting matches.

```python
from collections import Counter

def intersect(nums1, nums2):
    counts = Counter(nums1)
    out = []
    for x in nums2:
        if counts[x] > 0:
            out.append(x)
            counts[x] -= 1
    return out
```

- **Time:** `O(m + n)`.
- **Space:** `O(min(m, n))` for the hash map.

This is optimal in time and is the best choice for **unsorted** input. But it needs
extra hash-map space, and if the arrays are already sorted (the follow-up), we can do
better on space.

## Optimal Approach (Two-Pointer Merge)

Sort both arrays (skip this if they are already sorted), then merge-walk them with one
pointer each:

- If `nums1[i] < nums2[j]`, the smaller value cannot match anything later in `nums2`
  (it is sorted), so advance `i`.
- If `nums1[i] > nums2[j]`, advance `j` for the symmetric reason.
- If equal, it is a shared element — emit it and advance **both** pointers so each copy
  is matched at most once (giving `min` multiplicity automatically).

```python
def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()
    i = j = 0
    out = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            out.append(nums1[i])
            i += 1
            j += 1
    return out
```

**Why it is correct.** Both arrays are sorted, so whenever `nums1[i] < nums2[j]`, no
element at `nums2[j..]` equals `nums1[i]`, and advancing `i` discards nothing real.
Equal values are consumed in lockstep, so a value shared `a` times in `nums1` and `b`
times in `nums2` is matched exactly `min(a, b)` times.

**Step-by-step** on sorted `nums1 = [1,1,2,2]`, `nums2 = [2,2]`:

| i / j | Compare | Action | out |
| --- | --- | --- | --- |
| i=0(1), j=0(2) | `1 < 2` | i++ | `[]` |
| i=1(1), j=0(2) | `1 < 2` | i++ | `[]` |
| i=2(2), j=0(2) | equal   | emit 2, i++, j++ | `[2]` |
| i=3(2), j=1(2) | equal   | emit 2, i++, j++ | `[2,2]` |
| i=4 -> stop     |         |        | `[2,2]` |

- **Time:** `O(m log m + n log n)` if sorting is needed; `O(m + n)` if inputs are
  already sorted.
- **Space:** `O(1)` auxiliary (beyond the output and any in-place sort).

## Key Insights & Edge Cases

- On a **match, advance both pointers** — that is what yields `min` multiplicity for
  duplicates.
- Sorted inputs make the merge two-pointer walk possible with `O(1)` extra space; this
  is the intended answer to the follow-up.
- If the arrays are unequal in size and one is much smaller / stored on disk, the sorted
  two-pointer merge streams both inputs without loading either fully — a real advantage
  over the hash-map approach.
- No intersection (Example 3): pointers never both point at an equal value, so the
  result is empty.
- Empty result is returned as-is; no special casing required.
