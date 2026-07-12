# Count Stable Windows — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def countStableWindows(self, nums, k, threshold):
        maxd = deque()
        mind = deque()
        count = 0
        for i, x in enumerate(nums):
            while maxd and nums[maxd[-1]] <= x:
                maxd.pop()
            maxd.append(i)
            while mind and nums[mind[-1]] >= x:
                mind.pop()
            mind.append(i)
            if maxd[0] <= i - k:
                maxd.popleft()
            if mind[0] <= i - k:
                mind.popleft()
            if i >= k - 1 and nums[maxd[0]] - nums[mind[0]] <= threshold:
                count += 1
        return count
```

### Complexity

O(n) time, O(k) space.
