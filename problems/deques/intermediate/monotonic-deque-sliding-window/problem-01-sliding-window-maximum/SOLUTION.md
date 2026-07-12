# Sliding Window Maximum — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()  # indices, values decreasing front -> back
        out = []
        for i, x in enumerate(nums):
            while dq and nums[dq[-1]] <= x:
                dq.pop()
            dq.append(i)
            if dq[0] <= i - k:
                dq.popleft()
            if i >= k - 1:
                out.append(nums[dq[0]])
        return out
```

### Complexity

O(n) time, O(k) space — each index enters and leaves the deque once.
