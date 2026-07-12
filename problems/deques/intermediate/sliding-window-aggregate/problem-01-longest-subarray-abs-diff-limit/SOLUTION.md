# Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def longestSubarray(self, nums, limit):
        maxd = deque()  # decreasing values -> front is window max
        mind = deque()  # increasing values -> front is window min
        left = 0
        best = 0
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
            best = max(best, right - left + 1)
        return best
```

### Complexity

O(n) time, O(n) space in the worst case.
