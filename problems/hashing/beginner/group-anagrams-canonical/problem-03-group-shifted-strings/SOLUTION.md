# Group Shifted Strings — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def groupStrings(self, strings):
        groups = defaultdict(list)
        for s in strings:
            base = ord(s[0])
            key = tuple((ord(c) - base) % 26 for c in s)
            groups[key].append(s)
        result = [sorted(g) for g in groups.values()]
        result.sort()
        return result
```
