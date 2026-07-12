# Maximum Number of Balloons — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def maxNumberOfBalloons(self, text):
        have = Counter(text)
        need = Counter("balloon")
        return min(have[c] // need[c] for c in need)
```
