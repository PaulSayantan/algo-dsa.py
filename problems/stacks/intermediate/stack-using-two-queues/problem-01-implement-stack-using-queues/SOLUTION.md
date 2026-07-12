# Implement Stack using Queues — Solution

## Optimal Approach

### Reference implementation

```python
class MyStack:
    def __init__(self):
        self._q = deque()

    def push(self, x):
        self._q.append(x)
        for _ in range(len(self._q) - 1):
            self._q.append(self._q.popleft())

    def pop(self):
        return self._q.popleft()

    def top(self):
        return self._q[0]

    def empty(self):
        return not self._q
```
