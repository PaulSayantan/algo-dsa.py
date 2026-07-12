# Josephus Last Two Survivors — Solution

## Optimal Approach

Same circular-queue simulation as the single-survivor Josephus, but change the
loop guard: keep eliminating while more than two people remain. When the loop
ends the queue holds exactly the two survivors; return them sorted so the answer
is deterministic regardless of their circular position.

### Reference implementation

```python
class Solution:
    def lastTwoSurvivors(self, n, k):
        q = deque(range(1, n + 1))
        while len(q) > 2:
            for _ in range(k - 1):
                q.append(q.popleft())
            q.popleft()
        return sorted(q)
```
