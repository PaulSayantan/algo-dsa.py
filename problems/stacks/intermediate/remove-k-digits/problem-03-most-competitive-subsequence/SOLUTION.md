# Most Competitive Subsequence — Solution

## Optimal Approach

Keep a monotonic increasing stack. When a smaller value arrives, pop larger tops
— but only while there are still enough remaining elements to refill the stack to
size `k` (`len(stack) + (n - i) > k`). Finally trim to the first `k` entries.

### Reference implementation

```python
class Solution:
    def mostCompetitive(self, nums, k):
        stack = []
        n = len(nums)
        for i, num in enumerate(nums):
            while stack and stack[-1] > num and len(stack) + (n - i) > k:
                stack.pop()
            stack.append(num)
        return stack[:k]
```
