# Longest Substring with At Most Two Distinct Characters — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        count = defaultdict(int)
        left = 0
        best = 0
        for right, c in enumerate(s):
            count[c] += 1
            while len(count) > 2:
                lc = s[left]
                count[lc] -= 1
                if count[lc] == 0:
                    del count[lc]
                left += 1
            best = max(best, right - left + 1)
        return best
```

### Complexity

O(n) time, O(1) space.
