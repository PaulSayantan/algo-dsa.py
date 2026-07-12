# Find All Numbers Disappeared in an Array — Solution

## Optimal Approach

A presence set plus a 1..n scan yields the absent values in ascending order directly. (In-place index marking gives O(1) extra space.)

### Reference implementation

```python
class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        present = set(nums)
        return [i for i in range(1, n + 1) if i not in present]
```

### Complexity

Time O(n), space O(n).
