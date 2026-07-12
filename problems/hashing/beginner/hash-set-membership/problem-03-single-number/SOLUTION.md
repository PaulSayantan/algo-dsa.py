# Single Number — Solution

## Optimal Approach

Adding a value on its first appearance and removing it on its second cancels every pair, leaving exactly the unique element in the set. (XOR gives an O(1)-space alternative, but the set makes the pairing explicit.)

### Reference implementation

```python
class Solution:
    def singleNumber(self, nums):
        seen = set()
        for x in nums:
            if x in seen:
                seen.discard(x)
            else:
                seen.add(x)
        return seen.pop()
```

### Complexity

Time O(n), space O(n) for the set.
