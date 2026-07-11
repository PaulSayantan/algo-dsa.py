# Solution — Kth Largest Element in an Array

## Brute Force

Sort the array in descending order and return the element at index `k - 1`.

```python
def findKthLargest(nums, k):
    nums.sort(reverse=True)
    return nums[k - 1]
```

- **Time:** `O(n log n)` — dominated by the sort.
- **Space:** `O(1)` extra (in-place sort) or `O(n)` for a sorted copy.

Correct and simple, but it does more work than needed: it fully orders all `n` elements
when we only care about the top `k`.

## Optimal Approach (Top-K via Heap)

We only need the `k` largest values, and among those the smallest is the answer. Maintain
a **min-heap of size `k`**:

1. Iterate through `nums`, pushing each value.
2. Whenever the heap exceeds size `k`, pop the root (the current minimum).
3. After the pass, `heap[0]` is the smallest of the `k` largest values = the `k`-th
   largest overall.

```python
import heapq

def findKthLargest(nums, k):
    heap = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]
```

**Why it is correct:** the heap is invariantly "the `k` largest elements seen so far." A
value smaller than the current `k`-th largest is pushed then immediately evicted, so it
cannot corrupt the set; a larger value evicts the current minimum, keeping exactly the top
`k`. The root is therefore the `k`-th largest.

- **Time:** `O(n log k)` — `n` pushes, each `O(log k)`.
- **Space:** `O(k)` for the heap.

This beats the sort whenever `k << n`, and it also generalizes to streams where the full
array is never in memory at once.

### Alternative: Quickselect — `O(n)` average

If the whole array is available and you only need the value (not a sorted top-`k`),
Quickselect finds it in linear average time. Finding the `k`-th largest is equivalent to
finding the element at index `n - k` in ascending order:

```python
import random

def findKthLargest(nums, k):
    target = len(nums) - k  # index in ascending order

    def select(lo, hi):
        pivot = nums[random.randint(lo, hi)]
        # 3-way partition: < pivot | == pivot | > pivot
        lt, i, gt = lo, lo, hi
        while i <= gt:
            if nums[i] < pivot:
                nums[lt], nums[i] = nums[i], nums[lt]; lt += 1; i += 1
            elif nums[i] > pivot:
                nums[i], nums[gt] = nums[gt], nums[i]; gt -= 1
            else:
                i += 1
        if target < lt:
            return select(lo, lt - 1)
        if target > gt:
            return select(gt + 1, hi)
        return nums[target]

    return select(0, len(nums) - 1)
```

- **Time:** `O(n)` average (each partition discards a side), `O(n^2)` worst case; a random
  pivot makes the worst case astronomically unlikely. The 3-way partition also handles
  arrays with many duplicates gracefully.
- **Space:** `O(1)` extra (partition in place; recursion is `O(log n)` expected).

## Key Insights & Edge Cases

- **Min-heap for k largest.** Capping a min-heap at `k` keeps the biggest `k` and surfaces
  the answer at the root — the recurring Top-K pattern.
- **k = 1 or k = n.** `k = 1` returns the maximum; `k = n` returns the minimum. Both fall
  out of the heap logic without special cases.
- **Duplicates count by position.** In `[3,2,3,1,2,4,5,5,6]` with `k=4`, the two 5s occupy
  ranks 2 and 3, so rank 4 is 4 — not the 4th *distinct* value.
- **Heap vs. Quickselect trade-off.** Heap: `O(n log k)`, `O(k)` space, streaming-friendly,
  no worst-case blowup. Quickselect: `O(n)` average, in-place, but mutates the input and has
  an `O(n^2)` worst case. Pick the heap for streams or when a stable bound matters.
