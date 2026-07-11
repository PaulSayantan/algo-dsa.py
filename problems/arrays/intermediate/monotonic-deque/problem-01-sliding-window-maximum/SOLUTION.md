# Sliding Window Maximum — Solution

## Brute Force

For each of the `n - k + 1` windows, scan its `k` elements and take the max.

```python
def brute(nums, k):
    res = []
    for i in range(len(nums) - k + 1):
        res.append(max(nums[i:i + k]))
    return res
```

- **Time:** `O(n * k)` — up to `k` comparisons per window.
- **Space:** `O(1)` beyond the output.

This is fine for tiny inputs but times out at `n = 10^5, k = 5*10^4`.

## Optimal Approach (Monotonic Deque)

Keep a **deque of indices** whose corresponding values are **strictly
decreasing** from front to back. Two invariants make the front the answer:

1. **Back-eviction (keep it decreasing).** Before pushing index `r`, pop every
   index `j` from the back while `nums[j] <= nums[r]`. Those elements are both
   older and no larger, so no future window can ever pick them over `nums[r]` —
   they are dominated and gone forever.
2. **Front-expiry (keep it inside the window).** The window covering right edge
   `r` starts at `r - k + 1`. If the front index equals `r - k` (or smaller), it
   has slid out; pop it from the front.

After processing index `r`, once `r >= k - 1` the window `[r-k+1, r]` is complete
and `nums[deque[0]]` is its maximum.

```python
from collections import deque

def optimal(nums, k):
    dq = deque()      # indices, nums[...] decreasing front -> back
    res = []
    for r, x in enumerate(nums):
        # 1. evict smaller-or-equal values from the back
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(r)
        # 2. drop the front if it left the window
        if dq[0] <= r - k:
            dq.popleft()
        # 3. record the answer once the first window is full
        if r >= k - 1:
            res.append(nums[dq[0]])
    return res
```

### Why it is correct

At every step the deque contains exactly the indices in the current window that
are **not dominated** by a later element in that window — i.e. the candidates
that could still be the maximum of some window ending at or after `r`. Because we
evict all smaller-or-equal predecessors, the values stay strictly decreasing, so
the front is the largest. Front-expiry guarantees the front index is still inside
the window. Hence `nums[deque[0]]` is precisely the window maximum.

### Step-by-step on `nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3`

Deque shown as indices (values decreasing front to back); the window becomes
full at `r = 2`. Front-expiry pops the front only when `dq[0] <= r - k`.

| r | x  | after back-evict + push | after front-expiry | output max |
|---|----|-------------------------|--------------------|------------|
| 0 | 1  | [0]                     | [0]                | —          |
| 1 | 3  | [1] (popped 0)          | [1]                | —          |
| 2 | -1 | [1,2]                   | [1,2]              | nums[1]=3  |
| 3 | -3 | [1,2,3]                 | [1,2,3]            | nums[1]=3  |
| 4 | 5  | [4] (popped 3,2,1)      | [4]                | nums[4]=5  |
| 5 | 3  | [4,5]                   | [4,5]              | nums[4]=5  |
| 6 | 6  | [6] (popped 5,4)        | [6]                | nums[6]=6  |
| 7 | 7  | [7] (popped 6)          | [7]                | nums[7]=7  |

At `r = 3` the front index `1` is not expired because `1 <= 3 - 3 = 0` is false,
so the maximum correctly stays `nums[1] = 3`.

Result: `[3, 3, 5, 5, 6, 7]`, matching Example 1.

- **Time:** `O(n)` — every index is appended once and popped at most once, so at
  most `2n` deque operations total.
- **Space:** `O(k)` — the deque never holds more than `k` indices.

## Key Insights & Edge Cases

- **Store indices, not values**, so front-expiry (`dq[0] <= r - k`) is testable.
- Popping with `<=` (not `<`) is fine and preferred: equal values are also
  dominated by the newer index, and keeping fewer entries is cheaper. Using `<`
  would still be correct but leaves duplicates on the deque.
- `k == 1` makes each element its own window, so the output equals the input; the
  deque holds one index at a time.
- `k == len(nums)` yields a single window and one output value (the global max).
- A **max-heap with lazy deletion** also works but costs `O(n log n)` time and up
  to `O(n)` space — strictly worse than the deque.
- For a sliding-window **minimum**, flip the comparison to
  `while dq and nums[dq[-1]] >= x: dq.pop()` so the deque stays increasing.
