# Check If N and Its Double Exist — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def checkIfExist(self, arr):
        seen = set()
        for x in arr:
            if 2 * x in seen or (x % 2 == 0 and x // 2 in seen):
                return True
            seen.add(x)
        return False
```
