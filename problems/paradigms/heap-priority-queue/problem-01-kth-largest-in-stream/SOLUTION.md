# Kth Largest Element in a Stream — Solution

## Brute Force

Keep every element in a list. On each `add`, append the value, sort the whole list in
descending order, and return the element at index `k - 1`.

- **Time:** `O(n log n)` per `add` (a full sort of up to `n` elements). Across `m`
  adds this is `O(m · n log n)`.
- **Space:** `O(n)` to store the stream.

Correct but wasteful: we re-sort the entire history every call, even though only one
element changed and we only ever need the `k`th boundary.

## Optimal Approach (Heap / Priority Queue)

**Idea:** We never need the full sorted order — only the kth largest. Maintain a
**min-heap that holds exactly the `k` largest elements** seen so far. Because it is a
min-heap, its root `heap[0]` is the *smallest of those top `k`*, which is precisely the
kth largest element overall.

Procedure:

1. In the constructor, push all initial `nums` into the heap, popping the smallest
   whenever the size exceeds `k`.
2. On `add(val)`: push `val`; if the heap now has more than `k` elements, pop the
   minimum. Return `heap[0]`.

```python
import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = nums[:]          # copy so we don't mutate the caller's list
        heapq.heapify(self.heap)     # O(n)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
```

A slightly slicker `add` uses `heappushpop` once the heap is full (push then pop the min
in one balanced operation):

```python
    def add(self, val):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)   # pop min, push val
        return self.heap[0]
```

**Why it is correct:** An element belongs to the "top `k`" iff it is larger than the
current smallest member of the top `k` (the root). If a new value is `<=` the root, it
cannot displace anything and is discarded; if it is larger, it kicks out the current
root, which was the weakest of the top `k`. Thus the heap always contains exactly the
`k` largest values, and its minimum is the kth largest.

- **Time:** `O(log k)` per `add` (push + pop on a heap of size `k`); constructor is
  `O(n log k)` (or `O(n)` heapify then trim). Independent of the total stream length.
- **Space:** `O(k)` — the heap never grows beyond `k` elements.

## Key Insights & Edge Cases

- **Min-heap for kth *largest*** feels backwards at first: the trick is that keeping the
  *smallest* of the top `k` at the root lets you cheaply reject weak newcomers and read
  the answer in `O(1)`.
- **Bounded memory:** the heap is capped at `k`, so this scales to arbitrarily long
  streams — the whole point over the brute-force list.
- **Duplicates count:** it is the kth largest in sorted order, not among distinct values.
  A min-heap naturally keeps duplicates (e.g. two `5`s can both live in the top `k`).
- **Initial `nums` shorter than `k`:** the heap holds fewer than `k` items until enough
  values arrive; the problem guarantees `add` is only queried once `>= k` elements exist.
- **Copy the input list** before `heapify` if you must not mutate the caller's array.
