# Valid Anagram — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)
```
