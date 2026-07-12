# Longest Well-Performing Interval — Solution

## Optimal Approach

Map to +/-1; a positive prefix qualifies wholesale, else seek score-1's first index.

### Reference implementation

```python
class Solution:
    def longestWPI(self, hours):
        first = {}
        cur = 0
        best = 0
        for i, h in enumerate(hours):
            cur += 1 if h > 8 else -1
            if cur > 0:
                best = i + 1
            else:
                if cur - 1 in first:
                    best = max(best, i - first[cur - 1])
            if cur not in first:
                first[cur] = i
        return best
```

### Complexity

Time O(n), space O(n).

## Key Insights & Edge Cases

When cur>0 the answer is i+1; otherwise the earliest cur-1 gives the longest span.
