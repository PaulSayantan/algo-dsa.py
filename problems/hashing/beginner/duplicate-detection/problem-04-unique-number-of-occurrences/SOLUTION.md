# Unique Number of Occurrences — Solution

## Optimal Approach

First map value -> count, then test whether those counts are themselves distinct: `len(set(counts)) == len(counts)`. A second hashing layer over the count values does the uniqueness check.

### Reference implementation

```python
class Solution:
    def uniqueOccurrences(self, arr):
        counts = list(Counter(arr).values())
        return len(set(counts)) == len(counts)
```

### Complexity

Time O(n), space O(n).
