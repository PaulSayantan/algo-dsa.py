# Jump Game VI — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def maxResult(self, nums, k):
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dq = deque([0])
        for i in range(1, n):
            while dq and dq[0] < i - k:
                dq.popleft()
            dp[i] = nums[i] + dp[dq[0]]
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
            dq.append(i)
        return dp[n - 1]
```
