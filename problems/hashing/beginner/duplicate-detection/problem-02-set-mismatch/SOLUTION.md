# Set Mismatch — Solution

## Optimal Approach

Scanning 1..n against the frequency map pinpoints the value seen twice and the value seen zero times in a single ordered pass, giving the fixed [dup, missing] answer.

### Reference implementation

```python
class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        counts = Counter(nums)
        dup = missing = -1
        for i in range(1, n + 1):
            c = counts.get(i, 0)
            if c == 2:
                dup = i
            elif c == 0:
                missing = i
        return [dup, missing]
```

### Complexity

Time O(n), space O(n).
