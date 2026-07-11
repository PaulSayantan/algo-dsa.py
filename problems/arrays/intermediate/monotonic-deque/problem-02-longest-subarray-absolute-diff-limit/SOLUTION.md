# Longest Subarray With Absolute Diff <= Limit — Solution

## Brute Force

Try every subarray `[l, r]`, compute its max and min, and keep the longest that
satisfies the limit.

```python
def brute(nums, limit):
    n, best = len(nums), 0
    for l in range(n):
        for r in range(l, n):
            window = nums[l:r + 1]
            if max(window) - min(window) <= limit:
                best = max(best, r - l + 1)
    return best
```

- **Time:** `O(n^3)` naively (or `O(n^2)` if you maintain a running max/min).
- **Space:** `O(1)` beyond the input.

## Optimal Approach (Two Monotonic Deques)

The condition "`max - min <= limit`" is **monotone in window growth**: if a
window is invalid, extending its right edge can only keep it invalid or make it
worse, so we can use a **sliding window with a left pointer that never moves
back**. The only missing piece is querying the current window's max and min in
`O(1)` — which is exactly what monotonic deques give.

Maintain two deques of **indices**:

- `max_dq`: values **decreasing** front to back, so `nums[max_dq[0]]` is the
  window maximum.
- `min_dq`: values **increasing** front to back, so `nums[min_dq[0]]` is the
  window minimum.

For each right edge `r`:

1. Push `r` into both deques, evicting dominated indices from each back.
2. While `nums[max_dq[0]] - nums[min_dq[0]] > limit`, the window is too wide:
   advance `l` by one and pop any deque front whose index is now `< l`.
3. Record `best = max(best, r - l + 1)`.

```python
from collections import deque

def optimal(nums, limit):
    max_dq, min_dq = deque(), deque()  # indices
    l = best = 0
    for r, x in enumerate(nums):
        while max_dq and nums[max_dq[-1]] <= x:
            max_dq.pop()
        max_dq.append(r)
        while min_dq and nums[min_dq[-1]] >= x:
            min_dq.pop()
        min_dq.append(r)

        while nums[max_dq[0]] - nums[min_dq[0]] > limit:
            l += 1
            if max_dq[0] < l:
                max_dq.popleft()
            if min_dq[0] < l:
                min_dq.popleft()

        best = max(best, r - l + 1)
    return best
```

### Why it is correct

Each deque independently answers "max (or min) of the current window in `O(1)`"
using the same invariant as Sliding Window Maximum. The left pointer only ever
moves right, and it moves exactly as far as needed to restore
`max - min <= limit`; because widening a window can never *decrease* the
max-min spread, we never skip a longer valid window. Every index enters and
leaves each deque at most once.

### Step-by-step on `nums = [10, 1, 2, 4, 7, 2], limit = 5`

| r | x | l | max_dq (idx) | min_dq (idx) | max | min | window len |
|---|---|---|--------------|--------------|-----|-----|------------|
| 0 | 10| 0 | [0]          | [0]          | 10  | 10  | 1          |
| 1 | 1 | 1 | [1]          | [1]          | 1   | 1   | 1          |
| 2 | 2 | 1 | [2]          | [1,2]        | 2   | 1   | 2          |
| 3 | 4 | 1 | [3]          | [1,2,3]      | 4   | 1   | 3          |
| 4 | 7 | 2 | [4]          | [2,3,4]      | 7   | 2   | 3          |
| 5 | 2 | 2 | [4,5]        | [2,5]        | 7   | 2   | 4          |

At `r = 4`, before shrinking, max `7` - min `1` = `6 > 5`, so `l` advances to `2`
and index `1` leaves `min_dq`. The best window length reached is `4`
(the subarray `[2, 4, 7, 2]`), matching the expected output.

- **Time:** `O(n)` — each index is pushed and popped at most once per deque.
- **Space:** `O(n)` worst case for the two deques.

## Key Insights & Edge Cases

- You need **two** deques because you must track both the max and the min of the
  same window simultaneously.
- Advance `l` with a `while`, not an `if`: one new element can force several
  left-side removals (though amortized it is still `O(n)`).
- After moving `l`, only pop a deque front when its index `< l`; a front already
  inside the window must stay.
- `limit == 0` degenerates to "longest run of equal values" (Example 3).
- The answer is always `>= 1` since a single element has max-min `= 0 <= limit`.
- Values can be up to `10^9`; the differences fit comfortably in Python ints and
  in 64-bit integers in other languages.
