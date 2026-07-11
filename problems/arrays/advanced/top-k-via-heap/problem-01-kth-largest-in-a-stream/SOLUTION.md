# Solution — Kth Largest Element in a Stream

## Brute Force

Store every value in a list. On each `add`, append the new value, sort the list in
descending order, and return the element at index `k - 1`.

- **Time:** `O(n log n)` per `add` call (a full sort each time). Across `m` calls this
  degrades to `O(m · n log n)`.
- **Space:** `O(n)` to hold the whole stream.

This re-sorts data that was already ordered, wasting almost all of the work — the wrong
tool for a stream.

## Optimal Approach (Top-K via Heap)

**Key observation:** we never need the whole sorted stream — we only need the `k`
largest elements, and among those, the *smallest* one is the answer.

Maintain a **min-heap capped at size `k`**:

1. In the constructor, push every element of `nums`. After each push, if the heap size
   exceeds `k`, pop the root (the current minimum).
2. On `add(val)`: push `val`, then if the size exceeds `k`, pop the root.
3. The answer is always `heap[0]` — the smallest of the `k` largest elements, i.e. the
   `k`-th largest overall.

**Why it is correct:** the heap is an invariant "the `k` largest values seen so far."
Any value smaller than the current `k`-th largest gets evicted immediately (it is pushed
then popped), so it can never displace a rightful member. Any value larger than the root
kicks out the old minimum, correctly shrinking the surviving set to the top `k`. The root
is therefore exactly the `k`-th largest.

```python
import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = nums[:]          # copy
        heapq.heapify(self.heap)     # O(n)
        while len(self.heap) > k:    # trim down to k
            heapq.heappop(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
```

- **Constructor time:** `O(n log k)` (heapify `O(n)` plus at most `n` trimming pops).
- **`add` time:** `O(log k)` per call — one push plus at most one pop.
- **Space:** `O(k)` — the heap never holds more than `k` elements once trimmed.

## Key Insights & Edge Cases

- **Min-heap, not max-heap.** Capping a *min*-heap at size `k` keeps the *largest* `k`
  and exposes the answer at the root. This inversion is the crux of every Top-K problem.
- **Empty initial `nums`.** The heap may start empty; that is fine. The problem guarantees
  at least `k` elements exist before any answer is requested, so the root is well-defined
  when queried.
- **Duplicates count.** Because we rank by sorted position (not distinct values), equal
  elements each occupy a slot. `[8,5,5,4]` has 3rd largest = 5, not 4.
- **Negative numbers** need no special handling — heap ordering works on any comparable
  ints.
- **Don't over-trim.** If `len(nums) < k` initially, do not pop below `k`; just let the
  heap fill up as `add` is called.
