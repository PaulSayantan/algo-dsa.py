# Shortest Subarray with Sum at Least K — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def shortestSubarray(self, nums, k):
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        dq = deque()  # indices into prefix, increasing values
        best = n + 1
        for i in range(n + 1):
            while dq and prefix[i] - prefix[dq[0]] >= k:
                best = min(best, i - dq.popleft())
            while dq and prefix[dq[-1]] >= prefix[i]:
                dq.pop()
            dq.append(i)
        return best if best <= n else -1
```
