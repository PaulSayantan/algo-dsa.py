# Count Nice Pairs in an Array — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def countNicePairs(self, nums):
        MOD = 10 ** 9 + 7
        def rev(n):
            r = 0
            while n > 0:
                r = r * 10 + n % 10
                n //= 10
            return r
        count = Counter()
        res = 0
        for x in nums:
            key = x - rev(x)
            res += count[key]
            count[key] += 1
        return res % MOD
```

### Complexity

O(n * digits) time, O(n) space.
