# Replace the Substring for Balanced String — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def balancedString(self, s):
        n = len(s)
        need = n // 4
        count = Counter(s)
        left = 0
        best = n
        for right in range(n):
            count[s[right]] -= 1
            while left < n and all(count[c] <= need for c in "QWER"):
                best = min(best, right - left + 1)
                count[s[left]] += 1
                left += 1
        return best
```

### Complexity

O(n) time, O(1) space.
