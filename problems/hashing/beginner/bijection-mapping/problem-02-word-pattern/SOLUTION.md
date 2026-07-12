# Word Pattern — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False
        forward, backward = {}, {}
        for c, w in zip(pattern, words):
            if c in forward and forward[c] != w:
                return False
            if w in backward and backward[w] != c:
                return False
            forward[c] = w
            backward[w] = c
        return True
```
