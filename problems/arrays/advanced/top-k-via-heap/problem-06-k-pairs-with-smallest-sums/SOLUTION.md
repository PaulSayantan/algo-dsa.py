# Solution — Find K Pairs with Smallest Sums

## Brute Force

Generate all `m * n` pairs, sort them by sum, and take the first `k`.

```python
def kSmallestPairs(nums1, nums2, k):
    pairs = [[u, v] for u in nums1 for v in nums2]
    pairs.sort(key=sum)
    return pairs[:k]
```

- **Time:** `O(m·n log(m·n))` — building and sorting every pair.
- **Space:** `O(m·n)` to hold all pairs.

With `m, n` up to `10^5`, `m·n` reaches `10^10` pairs — far too many to enumerate. We must
avoid materializing pairs we will never return.

## Optimal Approach (Top-K via Heap)

**Key structure.** Think of the sums as an `m x n` matrix `M[i][j] = nums1[i] + nums2[j]`.
Because both arrays are sorted, every row and every column of `M` is non-decreasing (top-left
is the global minimum). Finding the `k` smallest sums is exactly the classic "merge `k`
sorted sequences" problem: row `i` is a sorted sequence starting at `M[i][0]`.

**Frontier idea.** Maintain a min-heap of candidate pairs identified by indices `(i, j)`,
keyed on their sum. The invariant: the heap always contains the smallest not-yet-emitted
candidate from each row we have started. When we pop `(i, j)` (the global minimum among
candidates), the only new pair that can now become a frontier candidate is its right
neighbor `(i, j+1)` — everything above and to the left has already been emitted.

**Algorithm:**

1. Seed the heap with `(nums1[i] + nums2[0], i, 0)` for `i` in `0 .. min(k, m) - 1`. We need
   at most `k` starting rows because the answer has only `k` pairs.
2. Pop the smallest `(sum, i, j)`, append `[nums1[i], nums2[j]]` to the result.
3. Push its right neighbor `(nums1[i] + nums2[j+1], i, j+1)` if `j + 1 < n`.
4. Repeat until we have `k` pairs or the heap empties.

```python
import heapq

def kSmallestPairs(nums1, nums2, k):
    if not nums1 or not nums2:
        return []

    heap = []
    # Seed with the first column, capped at k rows.
    for i in range(min(k, len(nums1))):
        heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

    result = []
    while heap and len(result) < k:
        _, i, j = heapq.heappop(heap)
        result.append([nums1[i], nums2[j]])
        if j + 1 < len(nums2):
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
    return result
```

**Why it is correct:** the smallest un-emitted sum is always on the frontier — the set of
right-neighbors of already-emitted pairs plus the un-started row heads. Seeding column 0 puts
every row's head on the frontier; each pop advances exactly one row's pointer rightward, which
is the only cell that can newly become minimal. By always popping the heap minimum we emit
sums in non-decreasing order, so the first `k` pops are the `k` smallest sums. We never seed
more than `k` rows because no pair beyond the `k`-th row-head can be among the `k` smallest
(each row-head is already `>=` the previous rows' heads in sorted `nums1`).

- **Time:** `O(k log k)` — the heap holds at most `min(k, m) + k` entries, and we perform
  `O(k)` pushes and pops, each `O(log k)`. Independent of the huge `m·n`.
- **Space:** `O(k)` for the heap.

## Key Insights & Edge Cases

- **Never enumerate the matrix.** The whole point is to explore only the `O(k)` cells near
  the top-left frontier of the implicit sum matrix, not all `m·n` cells.
- **Seed the first column, expand rightward.** Because `nums2` is sorted, `M[i][j+1] >=
  M[i][j]`, so the right neighbor is the correct next candidate for a row. Seeding the first
  column (not the first row) and expanding right is one consistent, correct scheme; the
  transpose works equally well.
- **Cap the seed at k rows.** Seeding `min(k, m)` rows avoids pushing up to `10^5` useless
  entries when `k` is small — this is what keeps the bound at `O(k log k)` rather than
  `O((m + k) log ...)`.
- **Fewer than k pairs.** If `m * n < k` (e.g. `nums1=[1,2]`, `nums2=[3]`, `k=3`), the heap
  empties first and we return all available pairs — the `while heap` guard handles it.
- **Empty input guard.** If either array is empty there are no pairs; return `[]` up front.
- **Duplicates and negatives.** Equal sums (e.g. two `1 + 1 = 2` pairs) and negative values
  need no special handling; the heap orders purely by numeric sum and ties resolve on the
  index fields.
- **Avoid revisiting cells.** Seeding only column 0 and only ever moving right guarantees each
  `(i, j)` is pushed at most once, so no visited-set is needed.
