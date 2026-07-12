# Next Smaller Element — Solution

## Optimal Approach

This is the next-greater-element scan with the comparison reversed. Keep a stack of
indices whose values are increasing from bottom to top. When `nums[i]` arrives, it
is strictly smaller than every value on top that exceeds it, so those pending
indices get resolved to `nums[i]`; pop them. Push `i` and continue. Anything left
on the stack at the end never found a smaller value and stays `-1`. O(n).

### Reference implementation

```python
class Solution:
    def nextSmallerElement(self, nums):
        n = len(nums)
        answer = [-1] * n
        stack = []  # indices with strictly increasing values
        for i, x in enumerate(nums):
            while stack and nums[stack[-1]] > x:
                answer[stack.pop()] = x
            stack.append(i)
        return answer
```
