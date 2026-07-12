# N-th Generated Binary Number — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def nthBinary(self, n):
        q = deque(["1"])
        result = ""
        for _ in range(n):
            result = q.popleft()
            q.append(result + "0")
            q.append(result + "1")
        return result
```
