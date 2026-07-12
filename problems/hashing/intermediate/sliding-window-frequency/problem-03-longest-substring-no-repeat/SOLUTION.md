# Longest Substring Without Repeating Characters — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        last = {}
        left = 0
        best = 0
        for i, c in enumerate(s):
            if c in last and last[c] >= left:
                left = last[c] + 1
            last[c] = i
            best = max(best, i - left + 1)
        return best
```

### Complexity

O(n) time, O(min(n, alphabet)) space.
