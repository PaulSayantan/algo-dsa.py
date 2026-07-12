# Number of Wonderful Substrings — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def wonderfulSubstrings(self, word):
        count = [0] * 1024
        count[0] = 1
        mask = 0
        res = 0
        for ch in word:
            mask ^= 1 << (ord(ch) - ord('a'))
            res += count[mask]
            for i in range(10):
                res += count[mask ^ (1 << i)]
            count[mask] += 1
        return res
```

### Complexity

O(10 * n) time, O(1024) space.
