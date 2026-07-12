# Minimum Window Covering a Multiset Target — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def minWindowMultiset(self, nums, target):
        if not target:
            return 0
        need = Counter(target)
        missing = len(target)
        left = 0
        best = float("inf")
        for right, x in enumerate(nums):
            if need[x] > 0:
                missing -= 1
            need[x] -= 1
            while missing == 0:
                best = min(best, right - left + 1)
                need[nums[left]] += 1
                if need[nums[left]] > 0:
                    missing += 1
                left += 1
        return best if best != float("inf") else 0
```

### Complexity

O(n) time, O(|target|) space.
