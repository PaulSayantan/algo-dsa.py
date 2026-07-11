# Sliding Window Maximum — Solution

## Brute Force

For each window start `i` from `0` to `n - k`, scan the `k` elements `nums[i : i+k]` and
take the max.

- **Time:** `O(n * k)`.
- **Space:** `O(1)` beyond the output.

With `n` up to `10^5` and `k` up to `n`, this is `O(n^2)` in the worst case — too slow.

A heap of `(value, index)` improves this to `O(n log n)` (push each element, pop stale
maxima lazily from the top). Good, but we can do strictly linear time.

## Optimal Approach (Monotonic Stack / Queue)

Maintain a **monotonic deque** (double-ended queue) of **indices** whose corresponding
values are **strictly decreasing** from front to back. Two invariants hold at all times:

1. The deque only contains indices inside the current window.
2. Values at those indices are decreasing, so `nums[deque[0]]` (the front) is the current
   window's maximum.

For each index `i`:

1. **Expire the front:** if `deque[0] == i - k`, that index has slid out of the window; pop
   it from the front.
2. **Maintain monotonicity:** while the deque is non-empty and `nums[deque[-1]] <= nums[i]`,
   pop from the back — those smaller/equal values can never be a maximum while `i` is in the
   window (i stays longer and is at least as large).
3. **Append** `i` at the back.
4. **Record:** once the first window is complete (`i >= k - 1`), append `nums[deque[0]]` to
   the result.

### Why it is correct

Any element that is smaller than a later element `nums[i]` and also enters the window no
later than `i`'s exit can never again be the window maximum — `nums[i]` dominates it for the
rest of that element's lifetime. So we may discard it immediately (step 2). What remains is a
decreasing sequence of "candidates," and the largest (front) is exactly the window max. The
front-expiry check (step 1) guarantees we never report an index that has left the window.

### Reference implementation

```python
from collections import deque

def maxSlidingWindow(self, nums, k):
    dq = deque()           # indices, values strictly decreasing front -> back
    result = []
    for i, x in enumerate(nums):
        if dq and dq[0] == i - k:      # front slid out of the window
            dq.popleft()
        while dq and nums[dq[-1]] <= x:  # drop dominated candidates
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```

### Complexity

- **Time:** `O(n)`. Each index is appended once and removed at most once across the whole run.
- **Space:** `O(k)` — the deque holds at most one window's worth of indices.

## Key Insights & Edge Cases

- **Store indices, not values:** you need positions to know when an element leaves the window.
- **Deque, not stack:** this is the "queue" side of the monotonic family. You pop from the
  back (to keep it decreasing) and from the front (to expire the oldest index).
- **`<=` on the back pop:** popping equal values too keeps the deque compact; correctness is
  unaffected because equal values give the same maximum, and the later index survives longer.
- **First `k-1` steps produce no output:** only start recording once a full window exists.
- **`k == 1`:** every element is its own window; the deque holds a single index each step and
  the output equals `nums`.
- **`k == n`:** a single window; the front converges to the index of the global maximum.
