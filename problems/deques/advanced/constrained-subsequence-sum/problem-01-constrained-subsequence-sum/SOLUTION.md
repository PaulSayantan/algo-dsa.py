# Constrained Subsequence Sum — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def constrainedSubsetSum(self, nums, k):
        dq = deque()  # indices, decreasing dp
        dp = [0] * len(nums)
        best = nums[0]
        for i, x in enumerate(nums):
            while dq and dq[0] < i - k:
                dq.popleft()
            take = dp[dq[0]] if dq else 0
            dp[i] = x + max(0, take)
            best = max(best, dp[i])
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
            dq.append(i)
        return best
```
