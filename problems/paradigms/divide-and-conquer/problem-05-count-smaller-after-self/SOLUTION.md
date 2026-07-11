# Count of Smaller Numbers After Self — Solution

## Brute Force

For each `i`, scan all `j > i` and count how many `nums[j] < nums[i]`.

- **Time:** `O(n^2)`.
- **Space:** `O(1)` beyond the output.

Correct but quadratic — too slow for `n = 10^5`.

## Optimal Approach (Divide and Conquer — Merge Sort Inversion Counting)

**Idea:** `counts[i]` asks how many elements *to the right* of index `i` are *strictly
smaller* — this is exactly counting the inversions each element participates in as the
"larger, earlier" partner. Merge sort naturally discovers these during its **merge**
step.

Sort a list of **original indices** by their `nums` value. Split into a left half
(earlier original positions) and a right half (later original positions). When merging
the two sorted halves in ascending order:

- Every element in the right half is originally *to the right* of every element in the
  left half.
- When we are about to place a left-half element `L`, let `j` be the number of
  right-half elements **already** emitted. All `j` of them were emitted because they
  were strictly smaller than some left element `≤ L`, hence strictly smaller than `L` —
  and they sit to `L`'s right. So we credit `counts[L] += j`.

Cross-pair contributions are summed across all levels of the recursion; combined with
the base-case single elements (which have no inversions), every ordered pair
`(i, j)` with `i < j` and `nums[j] < nums[i]` is counted exactly once — at the level
where `i` and `j` first land in different halves.

```python
def countSmaller(nums):
    n = len(nums)
    counts = [0] * n

    def sort(idx):                       # idx: original indices, returns them
        if len(idx) <= 1:                # sorted ascending by nums[.]
            return idx
        mid = len(idx) // 2
        left = sort(idx[:mid])
        right = sort(idx[mid:])
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if nums[left[i]] <= nums[right[j]]:
                counts[left[i]] += j     # j right-elements already placed are smaller
                merged.append(left[i]); i += 1
            else:
                merged.append(right[j]); j += 1
        while i < len(left):             # right exhausted: all j were smaller
            counts[left[i]] += j
            merged.append(left[i]); i += 1
        while j < len(right):
            merged.append(right[j]); j += 1
        return merged

    sort(list(range(n)))
    return counts
```

**Why the `<=` matters:** placing the left element on ties (`nums[left[i]] ==
nums[right[j]]`) ensures equal-valued right elements are **not** counted as smaller —
the problem wants *strictly* smaller. Every right element already emitted when we place
`left[i]` was emitted under `nums[left'] > nums[right]`, and since the left half is
ascending, that value is `< nums[left[i]]`.

**Recurrence:** `T(n) = 2T(n/2) + O(n)` → `O(n log n)`.

- **Time:** `O(n log n)`.
- **Space:** `O(n)` for the index/merge buffers and `O(log n)` recursion stack.

## Key Insights & Edge Cases

- **Sort indices, not values.** The answer must land in `counts[original_index]`, so
  the entities we merge are original indices ordered by their value.
- **The counting happens in the merge (combine) step** — this is the recurring D&C
  theme: the split is trivial, the combine carries the cleverness.
- **Strict vs. non-strict** is controlled entirely by the tie rule. Use `<=` (take from
  the left on ties) so equal values are not miscounted — see example 2 (`[-1,-1] →
  [0,0]`).
- **Count while the right pointer leads:** the value `j` (right elements already placed)
  is precisely the number of smaller-and-to-the-right elements for the current left
  element; don't forget to also credit the *drain* loop when the right half empties
  first.
- **Alternatives:** a Binary Indexed Tree / merge-sort BIT after coordinate
  compression, or an order-statistics BST, also solve this in `O(n log n)`. The merge
  sort version is the cleanest pure Divide and Conquer formulation.
