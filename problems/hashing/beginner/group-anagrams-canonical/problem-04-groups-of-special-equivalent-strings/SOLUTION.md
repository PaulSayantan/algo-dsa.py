# Groups of Special-Equivalent Strings — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def numSpecialEquivGroups(self, words):
        sigs = set()
        for w in words:
            even = "".join(sorted(w[0::2]))
            odd = "".join(sorted(w[1::2]))
            sigs.add((even, odd))
        return len(sigs)
```
