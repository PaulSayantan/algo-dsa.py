# Range of Each Sliding Window — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def windowRanges(self, nums, k):
        maxd = deque()  # decreasing -> front is window max
        mind = deque()  # increasing -> front is window min
        out = []
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
            if i >= k - 1:
                out.append(nums[maxd[0]] - nums[mind[0]])
        return out
```

### Complexity

O(n) time, O(k) space.
