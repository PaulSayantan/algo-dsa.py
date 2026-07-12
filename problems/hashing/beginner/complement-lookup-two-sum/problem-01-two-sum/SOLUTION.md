# Two Sum — Solution

## Optimal Approach

A single hash-map pass records each value's index; the complement lookup is O(1).

### Reference implementation

```python
class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i
        return []
```

### Complexity

O(n) time, O(n) space.
