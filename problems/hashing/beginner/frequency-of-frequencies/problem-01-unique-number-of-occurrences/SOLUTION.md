# Unique Number of Occurrences — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def uniqueOccurrences(self, arr):
        counts = Counter(arr)
        freqs = list(counts.values())
        return len(freqs) == len(set(freqs))
```
