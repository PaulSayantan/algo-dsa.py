# Solution: Intersection of Two Arrays II

## Brute Force

For each element of `nums1`, scan `nums2` for a match; when found, add it to the
result and mark that `nums2` position as used so it is not matched again.

```python
def intersect(nums1, nums2):
    nums2 = list(nums2)  # mutable copy
    result = []
    for v in nums1:
        for j in range(len(nums2)):
            if nums2[j] == v:
                result.append(v)
                nums2[j] = None  # consume this occurrence
                break
    return result
```

- **Time:** `O(m * n)` — for each of `m` elements we may scan all `n` of the
  other array.
- **Space:** `O(1)` extra (ignoring the output and the copy).

Correct, but the nested scan is wasteful.

## Optimal Approach (Frequency Counting)

Count the values of one array, then walk the other array and emit a value while
its remaining count is positive.

**Why it is correct:** The number of times a value should appear in the result
is `min(count_in_nums1, count_in_nums2)`. If we store the counts of `nums1` in a
map and then, for each value in `nums2`, output it only while its stored count is
positive (decrementing as we go), we output it exactly `min` times: we can emit
at most `count_in_nums1` copies (the map runs out) and at most
`count_in_nums2` copies (that is how many times we encounter it in `nums2`).

**Step by step:**
1. Build `counts = Counter(nums1)` (ideally count the smaller array).
2. Initialize an empty `result` list.
3. For each value `v` in `nums2`: if `counts[v] > 0`, append `v` to `result` and
   decrement `counts[v]`.
4. Return `result`.

```python
from collections import Counter

def intersect(nums1, nums2):
    # Count the smaller array to minimize extra space.
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    counts = Counter(nums1)
    result = []
    for v in nums2:
        if counts[v] > 0:
            result.append(v)
            counts[v] -= 1
    return result
```

- **Time:** `O(m + n)` — one pass to count, one pass to match.
- **Space:** `O(min(m, n))` — store counts for the smaller array.

## Key Insights & Edge Cases

- **Multiplicity via `min`:** Emitting only while the count is positive naturally
  produces `min(count1, count2)` copies without computing the min explicitly.
- **Count the smaller array:** Swapping so the hash map holds the smaller array
  reduces memory usage.
- **No common elements:** Returns `[]`.
- **Order is unspecified:** Any ordering of the correct multiset is accepted.
- **Follow-ups:**
  - If the arrays are already **sorted**, use a two-pointer merge for `O(1)`
    extra space instead of a hash map.
  - If `nums2` is huge and streamed from disk, counting `nums1` (kept in memory)
    and streaming `nums2` chunk by chunk is ideal — the hash-map approach
    handles this gracefully.
