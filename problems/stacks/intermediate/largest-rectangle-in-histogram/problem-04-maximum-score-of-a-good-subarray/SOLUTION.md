# Maximum Score of a Good Subarray — Solution

## Optimal Approach

Read `nums` as histogram bar heights. For a fixed bar `i` acting as the window
minimum, the widest window in which `nums[i]` is the minimum runs from just past
the previous strictly-smaller bar to just before the next strictly-smaller bar —
exactly the left/right boundaries the largest-rectangle-in-histogram monotonic
stack finds. If that maximal span `[left, right]` covers index `k`, then
`nums[i] * (right - left + 1)` is an achievable score; take the max over all `i`.
Two O(n) monotonic-stack passes (previous-smaller, then next-smaller) give the
boundaries, so the whole thing is O(n).

### Reference implementation

```python
class Solution:
    def maximumScore(self, nums, k):
        n = len(nums)
        prev = [-1] * n  # index of previous strictly-smaller bar
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            prev[i] = stack[-1] if stack else -1
            stack.append(i)
        nxt = [n] * n  # index of next strictly-smaller bar
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            nxt[i] = stack[-1] if stack else n
            stack.append(i)
        best = 0
        for i in range(n):
            left, right = prev[i] + 1, nxt[i] - 1
            if left <= k <= right:
                best = max(best, nums[i] * (right - left + 1))
        return best
```
