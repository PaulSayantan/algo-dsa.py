# First Unique Character in a String — Solution

## Optimal Approach

A two-pass approach: the first pass builds the frequency map, the second returns the earliest index whose count is 1. Scanning the original string (not the map) preserves left-to-right order.

### Reference implementation

```python
class Solution:
    def firstUniqChar(self, s):
        counts = Counter(s)
        for i, c in enumerate(s):
            if counts[c] == 1:
                return i
        return -1
```

### Complexity

Time O(n), space O(k).
