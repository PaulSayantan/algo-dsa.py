# Josephus Circle of Names — Solution

## Optimal Approach

The Josephus simulation does not care whether the circle holds numbers or
labels: seed the queue with the name strings in order, then run the same
rotate-`k-1`-people-to-the-back and dequeue-the-`k`-th loop until a single name
is left. That name is the survivor.

### Reference implementation

```python
class Solution:
    def survivor(self, names, k):
        q = deque(names)
        while len(q) > 1:
            for _ in range(k - 1):
                q.append(q.popleft())
            q.popleft()
        return q[0]
```
