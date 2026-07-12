# Sum of Subarray Ranges — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def subarrayRanges(self, nums):
        n = len(nums)

        def sum_of_extreme(is_min):
            prev = [-1] * n
            nxt = [n] * n
            stack = []
            for i in range(n):
                while stack and (nums[stack[-1]] > nums[i] if is_min else nums[stack[-1]] < nums[i]):
                    stack.pop()
                prev[i] = stack[-1] if stack else -1
                stack.append(i)
            stack = []
            for i in range(n - 1, -1, -1):
                while stack and (nums[stack[-1]] >= nums[i] if is_min else nums[stack[-1]] <= nums[i]):
                    stack.pop()
                nxt[i] = stack[-1] if stack else n
                stack.append(i)
            return sum(nums[i] * (i - prev[i]) * (nxt[i] - i) for i in range(n))

        return sum_of_extreme(False) - sum_of_extreme(True)
```
