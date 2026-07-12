# Contains Duplicate — Solution

## Optimal Approach

Insert values into a set one at a time; the first value that is already present proves a duplicate exists. Early-exit avoids scanning the rest of the array.

### Reference implementation

```python
class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False
```

### Complexity

Time O(n), space O(n).
