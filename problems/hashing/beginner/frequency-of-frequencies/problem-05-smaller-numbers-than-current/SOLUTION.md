# How Many Numbers Are Smaller Than the Current Number — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        count = [0] * 101
        for x in nums:
            count[x] += 1
        prefix = [0] * 101
        for i in range(1, 101):
            prefix[i] = prefix[i - 1] + count[i - 1]
        return [prefix[x] for x in nums]
```
