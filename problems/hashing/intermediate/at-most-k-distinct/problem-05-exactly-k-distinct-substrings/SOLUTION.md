# Count Substrings With Exactly K Distinct Characters — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def countExactlyKDistinct(self, s, k):
        def at_most(m):
            if m < 0:
                return 0
            count = defaultdict(int)
            left = 0
            res = 0
            for right, c in enumerate(s):
                count[c] += 1
                while len(count) > m:
                    count[s[left]] -= 1
                    if count[s[left]] == 0:
                        del count[s[left]]
                    left += 1
                res += right - left + 1
            return res
        return at_most(k) - at_most(k - 1)
```

### Complexity

O(n) time, O(k) space.
