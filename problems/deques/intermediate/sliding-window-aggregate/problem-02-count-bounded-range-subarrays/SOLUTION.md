# Count Subarrays With Bounded Range — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def countSubarrays(self, nums, limit):
        maxd = deque()
        mind = deque()
        left = 0
        total = 0
        for right, x in enumerate(nums):
            while maxd and nums[maxd[-1]] <= x:
                maxd.pop()
            maxd.append(right)
            while mind and nums[mind[-1]] >= x:
                mind.pop()
            mind.append(right)
            while nums[maxd[0]] - nums[mind[0]] > limit:
                left += 1
                if maxd[0] < left:
                    maxd.popleft()
                if mind[0] < left:
                    mind.popleft()
            total += right - left + 1
        return total
```

### Complexity

O(n) time, O(n) space.
