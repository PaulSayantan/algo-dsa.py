# Longest Substring with At Most K Distinct Characters — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if k == 0:
            return 0
        count = defaultdict(int)
        left = 0
        best = 0
        for right, c in enumerate(s):
            count[c] += 1
            while len(count) > k:
                lc = s[left]
                count[lc] -= 1
                if count[lc] == 0:
                    del count[lc]
                left += 1
            best = max(best, right - left + 1)
        return best
```

### Complexity

O(n) time, O(k) space.
