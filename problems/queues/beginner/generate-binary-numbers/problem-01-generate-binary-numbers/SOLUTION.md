# Generate Binary Numbers from 1 to N — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def generate(self, n):
        q = deque()
        q.append("1")
        out = []
        for _ in range(n):
            s = q.popleft()
            out.append(s)
            q.append(s + "0")
            q.append(s + "1")
        return out
```
