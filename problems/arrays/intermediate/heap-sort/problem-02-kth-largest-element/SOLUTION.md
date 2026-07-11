# Solution — Kth Largest Element in an Array

## Brute Force

Sort the whole array and index the k-th largest.

```python
return sorted(nums)[-k]
```

- **Time:** `O(n log n)` — fully sorting when we only need one order statistic.
- **Space:** `O(n)` (or `O(log n)` in place).

Correct, but it does far more work than necessary: we do not need the other
`n - 1` elements ranked.

## Optimal Approach (Heaps)

There are two heap-based strategies; both are direct applications of heap-sort
mechanics (build a heap, then extract).

### Option A — Max-heap, pop `k` times (partial heap sort)

Heapify all `n` elements into a max-heap in `O(n)`, then extract the maximum `k`
times. The k-th extraction is the answer — this is literally the first `k` steps
of an in-place heap sort. Python's `heapq` is a **min-heap**, so negate values.

```python
import heapq

def findKthLargest(self, nums, k):
    heap = [-x for x in nums]
    heapq.heapify(heap)                 # O(n) build
    for _ in range(k - 1):              # discard the k-1 largest
        heapq.heappop(heap)
    return -heap[0]                     # k-th largest
```

- **Time:** `O(n + k log n)`.
- **Space:** `O(n)` for the heap (or `O(1)` if you heapify `nums` in place).

### Option B — Min-heap of size `k` (best when `k << n`)

Keep a min-heap holding the `k` largest values seen so far. Push each element; if
the heap exceeds size `k`, pop the smallest. After the scan, the smallest of the
`k` largest — the heap root — is exactly the k-th largest.

```python
import heapq

def findKthLargest(self, nums, k):
    heap = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)         # drop the smallest so far
    return heap[0]                      # k-th largest
```

- **Time:** `O(n log k)` — each push/pop is `O(log k)`.
- **Space:** `O(k)`.

**Why it is correct.** In Option A, extracting the max repeatedly walks the
elements in descending order, so the `k`-th value pulled is the k-th largest. In
Option B, the invariant is that the heap always contains the `k` largest values
encountered; when a new value arrives that is larger than the current smallest of
those `k`, it displaces it, and any value smaller than the root can never be in
the top `k`. The root is the minimum of the top `k`, i.e. the k-th largest.

### Worked trace on `nums = [3,2,1,5,6,4], k = 2` (Option B)

```
push 3 -> [3]
push 2 -> [2,3]            size 2 == k
push 1 -> [1,3,2] pop 1 -> [2,3]     (1 too small)
push 5 -> [2,3,5] pop 2 -> [3,5]
push 6 -> [3,5,6] pop 3 -> [5,6]
push 4 -> [4,6,5] pop 4 -> [5,6]
root = 5   -> 2nd largest
```

## Key Insights & Edge Cases

- **`heapq` is a min-heap.** For a max-heap, negate on the way in and negate the
  result on the way out (Option A).
- **Choosing the option:** Option B's `O(n log k)` wins when `k` is small
  relative to `n`; Option A is simpler when `k` is close to `n`.
- **Duplicates count.** Rank is by sorted position, not distinct value — the
  size-`k` heap and the pop-`k`-times approach both handle this automatically
  (Example 2's two `5`s occupy ranks 2 and 3).
- **`k == n`** returns the minimum; **`k == 1`** returns the maximum. Both fall
  out of the same code with no special casing.
- **Quickselect alternative:** an in-place Hoare partition gives `O(n)` average
  time but `O(n^2)` worst case; the heap approach trades a `log` factor for a
  guaranteed bound and is the natural fit for the "top-k / streaming" family.
