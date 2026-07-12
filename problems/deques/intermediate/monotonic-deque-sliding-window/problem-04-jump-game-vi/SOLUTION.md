# Jump Game VI — Solution

## Optimal Approach

Let `dp[i]` be the best score to reach index `i`. Since you arrive at `i` from
some `j` in `[i-k, i-1]`, `dp[i] = nums[i] + max(dp[j])` over that window. Naively
scanning the window is O(nk); instead keep a **decreasing monotonic deque** of
indices ordered by `dp` value so the maximum previous `dp` inside `[i-k, i-1]` is
always at the deque front. Before reading the front, evict indices that have
fallen out of the window (`dq[0] < i - k`); after computing `dp[i]`, pop tail
indices whose `dp` is `<=` `dp[i]` and push `i`. The answer is `dp[n-1]`.

### Reference implementation

```python
class Solution:
    def maxResult(self, nums, k):
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dq = deque([0])  # indices, dp values decreasing front -> back
        for i in range(1, n):
            while dq and dq[0] < i - k:
                dq.popleft()
            dp[i] = nums[i] + dp[dq[0]]
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
            dq.append(i)
        return dp[-1]
```

### Complexity

O(n) time, O(n) space — each index enters and leaves the deque once.
