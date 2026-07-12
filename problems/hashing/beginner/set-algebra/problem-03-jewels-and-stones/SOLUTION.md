# Jewels and Stones — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def numJewelsInStones(self, jewels, stones):
        jset = set(jewels)
        return sum(1 for s in stones if s in jset)
```
