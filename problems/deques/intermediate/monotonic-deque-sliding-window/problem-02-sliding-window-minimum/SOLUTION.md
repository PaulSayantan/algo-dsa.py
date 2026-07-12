# Sliding Window Minimum — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def minSlidingWindow(self, nums, k):
        dq = deque()  # indices, values increasing front -> back
        out = []
        for i, x in enumerate(nums):
            while dq and nums[dq[-1]] >= x:
                dq.pop()
            dq.append(i)
            if dq[0] <= i - k:
                dq.popleft()
            if i >= k - 1:
                out.append(nums[dq[0]])
        return out
```

### Complexity

O(n) time, O(k) space.
