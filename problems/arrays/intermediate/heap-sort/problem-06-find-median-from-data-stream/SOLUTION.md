# Solution — Find Median from Data Stream

## Brute Force

Keep every number in a list. On `addNum`, append; on `findMedian`, sort and read
the middle.

- **Time:** `O(n log n)` per `findMedian` (or `O(n)` per `addNum` if you keep the
  list sorted by inserting in place). With up to `5 * 10^4` interleaved calls this
  is quadratic overall.
- **Space:** `O(n)`.

We only ever need the **middle** of the data, not a full ordering — two heaps
give us that middle in `O(1)` while keeping inserts at `O(log n)`.

## Optimal Approach (Two heaps)

Split the elements into two halves:

- **`lo`** — a **max-heap** holding the smaller half. Its root is the largest of
  the small half. Python's `heapq` is a min-heap, so store negated values.
- **`hi`** — a **min-heap** holding the larger half. Its root is the smallest of
  the large half.

Maintain two invariants after every insertion:

1. **Ordering:** every element in `lo` is `<=` every element in `hi`.
2. **Balance:** `len(lo) == len(hi)` or `len(lo) == len(hi) + 1` (let `lo` hold
   the extra element when the total count is odd).

Then the median is `lo`'s root when the total is odd, or the average of the two
roots when it is even.

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.lo = []   # max-heap (negated) — smaller half
        self.hi = []   # min-heap          — larger half

    def addNum(self, num):
        # Push to lo, then move lo's max over to hi (keeps ordering correct).
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        # Rebalance so lo is never smaller than hi.
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self):
        if len(self.lo) > len(self.hi):
            return float(-self.lo[0])
        return (-self.lo[0] + self.hi[0]) / 2.0
```

- **Time:** `O(log n)` per `addNum` (a constant number of pushes/pops);
  `O(1)` per `findMedian`.
- **Space:** `O(n)` to store all elements across the two heaps.

**Why it is correct.** The "push to `lo`, pop its max into `hi`, then rebalance"
sequence guarantees invariant 1: any new element is compared through both roots,
so it lands on the correct side and no element of `lo` ends up larger than an
element of `hi`. The final rebalance enforces invariant 2 by moving `hi`'s
minimum back to `lo` whenever `hi` gets ahead. Given both invariants, the roots
straddle the true middle: with an odd count `lo` has exactly one more element, so
its root *is* the median; with an even count the two roots are the two central
values, whose average is the median.

### Worked trace on `addNum(1), addNum(2), findMedian(), addNum(3), findMedian()`

```
addNum(1): push -> lo=[1]; move max -> hi=[1], lo=[]; rebalance -> lo=[1], hi=[]
addNum(2): push -> lo=[2,1]; move max(2) -> hi=[2], lo=[1]; sizes equal
           state: lo=[1] (max-heap), hi=[2]
findMedian(): sizes equal -> (1 + 2) / 2 = 1.5
addNum(3): push -> lo=[3,1]; move max(3) -> hi=[2,3], lo=[1];
           hi bigger -> move min(2) back -> lo=[2,1], hi=[3]
           state: lo top = 2, hi top = 3
findMedian(): len(lo) > len(hi) -> 2.0
```

## Key Insights & Edge Cases

- **Two heaps sandwich the median.** A max-heap of the low half and a min-heap of
  the high half expose both central candidates at their roots in `O(1)`.
- **Push-then-transfer keeps ordering honest.** Always routing the new value
  through one heap and moving that heap's extreme to the other guarantees
  invariant 1 without any explicit comparison of `num` against the roots.
- **Deterministic size rule.** Letting `lo` carry the extra element on odd counts
  makes `findMedian` a simple size check — no ambiguity about which root to read.
- **`heapq` is a min-heap:** negate values going into `lo` and negate its root on
  the way out to emulate a max-heap.
- **Return a float** and average as `/ 2.0` so even-count medians like `1.5` and
  `7.5` are exact; the first element (Example 2) correctly returns `5.0`.
- **Follow-ups:** if all values fall in a small range (e.g. `[0, 100]`), a
  counting/bucket structure gives `O(1)` updates; for a fixed sliding window, two
  heaps plus lazy deletion (or a balanced BST / order-statistics tree) maintains
  the median online.
