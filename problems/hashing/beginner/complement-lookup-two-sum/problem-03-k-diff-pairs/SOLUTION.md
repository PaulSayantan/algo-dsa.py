# K-diff Pairs in an Array — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def findPairs(self, nums, k):
        if k < 0:
            return 0
        cnt = Counter(nums)
        result = 0
        for x in cnt:
            if k == 0:
                if cnt[x] >= 2:
                    result += 1
            elif x + k in cnt:
                result += 1
        return result
```

### Complexity

O(n) time, O(n) space via a Counter over distinct values.
