# Find and Replace Pattern — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def findAndReplacePattern(self, words, pattern):
        def normalize(w):
            seen = {}
            return [seen.setdefault(c, len(seen)) for c in w]
        target = normalize(pattern)
        return [w for w in words if normalize(w) == target]
```
