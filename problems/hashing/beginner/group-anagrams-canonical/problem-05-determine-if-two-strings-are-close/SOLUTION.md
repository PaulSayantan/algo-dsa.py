# Determine if Two Strings Are Close — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def closeStrings(self, word1, word2):
        c1, c2 = Counter(word1), Counter(word2)
        return set(c1) == set(c2) and sorted(c1.values()) == sorted(c2.values())
```
