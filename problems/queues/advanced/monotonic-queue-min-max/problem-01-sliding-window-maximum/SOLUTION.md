# Sliding Window Maximum — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()  # indices, decreasing values
        res = []
        for i, x in enumerate(nums):
            while dq and nums[dq[-1]] <= x:
                dq.pop()
            dq.append(i)
            if dq[0] <= i - k:
                dq.popleft()
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res
```
