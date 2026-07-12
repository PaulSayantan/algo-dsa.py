# Find the Index of the First Occurrence in a String — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    BASE = 911382323
    MOD = 972663749

    def matchIndices(self, text, pattern):
        n, m = len(text), len(pattern)
        if m == 0:
            return list(range(n + 1))
        if m > n:
            return []
        high = pow(self.BASE, m - 1, self.MOD)
        phash = 0
        whash = 0
        for i in range(m):
            phash = (phash * self.BASE + ord(pattern[i])) % self.MOD
            whash = (whash * self.BASE + ord(text[i])) % self.MOD
        res = []
        for i in range(n - m + 1):
            if whash == phash and text[i:i + m] == pattern:
                res.append(i)
            if i < n - m:
                whash = ((whash - ord(text[i]) * high) * self.BASE + ord(text[i + m])) % self.MOD
        return res

    def countOccurrences(self, text, pattern):
        return len(self.matchIndices(text, pattern))

    def strStr(self, haystack, needle):
        hits = self.matchIndices(haystack, needle)
        return hits[0] if hits else -1
```
