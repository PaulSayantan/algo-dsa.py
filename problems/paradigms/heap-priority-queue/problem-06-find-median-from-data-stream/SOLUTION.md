# Find Median from Data Stream — Solution

## Brute Force

Keep all numbers in a list. On `addNum`, append (`O(1)`) or insert in sorted position
(`O(n)`); on `findMedian`, sort if needed and read the middle element(s).

- **Time:** `O(n log n)` per `findMedian` if you sort on demand, or `O(n)` per `addNum`
  if you keep the list sorted via insertion. Either way one operation is linear or worse.
- **Space:** `O(n)`.

With up to `5 * 10^4` interleaved operations this is quadratic overall — too slow, and it
does far more ordering work than the median actually requires.

## Optimal Approach (Two Heaps / Priority Queues)

**Idea:** We never need the full sorted order — only the middle. Split the data into two
halves:

- `low` — a **max-heap** holding the smaller half; its root is the *largest of the small
  numbers*.
- `high` — a **min-heap** holding the larger half; its root is the *smallest of the large
  numbers*.

Keep the two heaps **balanced** so their sizes differ by at most 1, and every element in
`low` is `<=` every element in `high`. Then the two roots straddle the median:

- If the total count is **odd**, one heap has an extra element; its root is the median.
- If **even**, the median is the average of the two roots.

Since `heapq` is a min-heap, implement `low` by pushing **negated** values.

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.low = []    # max-heap (store negatives): smaller half
        self.high = []   # min-heap: larger half

    def addNum(self, num):
        # 1. push onto max-heap, then move its max over to keep low <= high
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        # 2. rebalance so low is never smaller than high (low holds the extra)
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self):
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2.0
```

**Why it is correct:** The push-then-transfer step guarantees the ordering invariant
(`max(low) <= min(high)`): every new element first enters `low`, and `low`'s current
maximum is immediately handed to `high`, so nothing in `low` can exceed anything in
`high`. The rebalance keeps `len(low) == len(high)` or `len(low) == len(high) + 1`. Under
that invariant the middle of the sorted stream is exactly `low`'s root when the count is
odd, or the mean of the two roots when even.

- **Time:** `O(log n)` per `addNum` (a constant number of heap pushes/pops); `O(1)` per
  `findMedian` (just read the roots).
- **Space:** `O(n)` — every number is stored across the two heaps.

## Key Insights & Edge Cases

- **Two heaps beat one sorted list** because we only ever touch the boundary between the
  halves — insertion and median both avoid an `O(n)` shift.
- **The transfer trick** (`push to low`, then `pop low's max into high`) enforces the
  cross-heap ordering without any explicit comparison, which is easy to get subtly wrong
  when pushing directly to the "correct" side.
- **Balance convention:** here `low` carries the extra element on odd counts, so on an odd
  total the median is `-low[0]`. Pick a convention and keep `findMedian` consistent with
  it.
- **First element / odd counts:** after one `addNum`, `low` has one item, `high` is empty,
  and `findMedian` returns that single value.
- **Return a float** and divide by `2.0` for the even case to avoid integer division and
  satisfy the `10^-5` tolerance.
- **Negatives and duplicates** are handled naturally — the heaps order by value regardless
  of sign, and equal values simply pile up.
