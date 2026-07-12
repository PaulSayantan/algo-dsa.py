# Throttling Gateway — Solution

## Optimal Approach

This is the recent-counter throttling pattern applied to three windows at once. Keep one FIFO queue of timestamps per limit — a 1-second, a 10-second, and a 60-second window. Since `requestTime` is non-decreasing, each queue stays sorted, so expiring old entries is a front-popping loop.

For each arrival at time `t`:

1. Enqueue `t` into all three queues.
2. Pop the front of the 1-second queue while it is `< t` (only the current second survives), the 10-second queue while the front is `<= t - 10`, and the 60-second queue while the front is `<= t - 60`.
3. After trimming, the queue lengths are the counts (including this request) in each window. Drop the request if the 1-second queue exceeds 3, the 10-second queue exceeds 20, or the 60-second queue exceeds 60.

Note the request is dropped but its timestamp still stays in the queues, because every request counts toward the limits. Each timestamp is enqueued and dequeued at most once per queue, so the whole pass is O(n).

### Reference implementation

```python
class Solution:
    def droppedRequests(self, requestTime):
        q1, q10, q60 = deque(), deque(), deque()
        dropped = 0
        for t in requestTime:
            q1.append(t)
            q10.append(t)
            q60.append(t)
            while q1[0] < t:
                q1.popleft()
            while q10[0] <= t - 10:
                q10.popleft()
            while q60[0] <= t - 60:
                q60.popleft()
            if len(q1) > 3 or len(q10) > 20 or len(q60) > 60:
                dropped += 1
        return dropped
```
