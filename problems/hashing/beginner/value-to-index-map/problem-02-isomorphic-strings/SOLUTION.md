# Isomorphic Strings — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        s2t = {}
        t2s = {}
        for a, b in zip(s, t):
            if a in s2t and s2t[a] != b:
                return False
            if b in t2s and t2s[b] != a:
                return False
            s2t[a] = b
            t2s[b] = a
        return True
```

### Complexity

O(n) time, O(1) extra space (alphabet-bounded maps).
