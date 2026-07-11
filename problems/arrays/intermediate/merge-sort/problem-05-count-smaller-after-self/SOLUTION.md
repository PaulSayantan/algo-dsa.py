# Solution — Count of Smaller Numbers After Self

## Brute Force

For each `i`, scan all `j > i` and count how many satisfy `nums[j] < nums[i]`.

```python
counts = [0] * n
for i in range(n):
    for j in range(i + 1, n):
        if nums[j] < nums[i]:
            counts[i] += 1
```

- **Time:** `O(n^2)` — too slow at `n = 10^5`.
- **Space:** `O(1)` beyond the output.

## Optimal Approach (Merge Sort on index pairs)

This is "count inversions" but attributed **per element**. The trick: sort
`(value, original_index)` pairs with merge sort, and while merging, figure out how
many smaller elements land to the right of each left-half element.

Work with an array of original indices sorted by value. During a merge of a sorted
`left` and sorted `right` (both lists of original indices, sorted by their
values):

- Maintain a running counter `right_emitted` = how many right-half elements have
  already been appended to the merged output.
- When we take a **left** element (`nums[left[i]] <= nums[right[j]]`, break ties to
  the left), every right-half element already emitted came from a position to the
  **right** of this left element (right half = later original indices) and had a
  **smaller** value — so add `right_emitted` to `counts[left[i]]`.
- When we take a **right** element, increment `right_emitted`.

```python
def countSmaller(self, nums):
    n = len(nums)
    counts = [0] * n
    indices = list(range(n))          # indices sorted by value as we go

    def sort(lo, hi):                 # sort indices[lo:hi], stable by value
        if hi - lo <= 1:
            return
        mid = (lo + hi) // 2
        sort(lo, mid)
        sort(mid, hi)
        merged = []
        i, j = lo, mid
        right_emitted = 0
        while i < mid and j < hi:
            if nums[indices[i]] <= nums[indices[j]]:
                counts[indices[i]] += right_emitted
                merged.append(indices[i]); i += 1
            else:
                right_emitted += 1
                merged.append(indices[j]); j += 1
        while i < mid:                # flush remaining left
            counts[indices[i]] += right_emitted
            merged.append(indices[i]); i += 1
        while j < hi:
            merged.append(indices[j]); j += 1
        indices[lo:hi] = merged

    sort(0, n)
    return counts
```

**Why it is correct.** When comparing, the left segment holds smaller original
indices (earlier positions) and the right segment holds larger ones (later
positions). A right element is "consumed" (increments `right_emitted`) only when
it is **strictly smaller** than the current left front. So at the moment we place a
left element, `right_emitted` counts exactly the right-half (later-position)
elements that are strictly smaller than it — precisely the split contribution to
its "smaller-to-the-right" total. Recursion accumulates the within-half
contributions across all levels, and each smaller-to-the-right pair is counted
once, at the merge level where the two indices first land in different halves.
Using `<=` (take left on ties) guarantees equal values are not counted as smaller
(Examples 2 and 3).

**Complexity.**

- **Time:** `O(n log n)`.
- **Space:** `O(n)` for the index array and merge buffer, plus `O(log n)`
  recursion.

### Worked trace on `[5,2,6,1]` (indices with values)

Merging eventually compares the left group `{5,2}` against the right group
`{6,1}`. Value `1` (a later position) is strictly smaller than both `5` and `2`,
so it increments `right_emitted` before they are placed, crediting `+1` to each of
index-of-5 and index-of-2. Combined with the within-half counts, the totals come
out `[2,1,1,0]`.

## Key Insights & Edge Cases

- **Track original indices**, not just values — the answer is positional, so a
  plain value sort loses the mapping. Sorting an `indices` array keeps it.
- **Add the running right-count when emitting a LEFT element** (or equivalently
  when flushing leftover left elements at the end); this is the most common place
  to introduce a bug.
- **Ties use `<=`** so equal elements are not miscounted as "smaller" (Examples 2
  and 3 hinge on this).
- **Don't forget** to credit left elements that remain after the right half is
  exhausted — they still saw all `right_emitted` smaller elements.
- Alternative `O(n log n)` approaches: a Binary Indexed Tree / merge on a BST /
  order-statistics tree over coordinate-compressed values. Merge sort is the most
  self-contained.
