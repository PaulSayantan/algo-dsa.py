# Find All Duplicates in an Array — Solution

## Optimal Approach

A frequency map cleanly identifies count-2 values. Sorting the result gives a canonical order. (An O(1)-space trick negates nums[abs(x)-1] to mark seen values, but the counter is clearest.)

### Reference implementation

```python
class Solution:
    def findDuplicates(self, nums):
        counts = Counter(nums)
        return sorted(x for x, c in counts.items() if c == 2)
```

### Complexity

Time O(n log n) with the final sort (O(n) counting), space O(n).
