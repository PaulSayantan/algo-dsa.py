# Group Anagrams — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        result = [sorted(g) for g in groups.values()]
        result.sort()
        return result
```
