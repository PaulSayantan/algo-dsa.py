# Sliding Window Rate Limiter — Solution

## Optimal Approach

This is the sliding-window-log rate-limiting pattern. Maintain a queue holding the timestamps of the requests that have been **allowed** so far. Because the input is chronologically sorted, the queue stays sorted too, so expiring old entries is a simple front-popping loop.

For each request at time `t`:

1. Pop from the front of the queue while the front timestamp is `<= t - window` — those allowed requests have slid out of the window.
2. If fewer than `limit` timestamps remain, this request is allowed: enqueue `t` and record `True`.
3. Otherwise reject it (do not enqueue) and record `False`.

Each timestamp is enqueued and dequeued at most once, so the whole pass is O(n) time and O(limit) space for the queue.

### Reference implementation

```python
class Solution:
    def rateLimit(self, requests, limit, window):
        q = deque()
        out = []
        for t in requests:
            while q and q[0] <= t - window:
                q.popleft()
            if len(q) < limit:
                q.append(t)
                out.append(True)
            else:
                out.append(False)
        return out
```
