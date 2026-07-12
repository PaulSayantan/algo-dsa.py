# 132 Pattern — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def find132pattern(self, nums):
        stack = []
        two = float('-inf')  # best candidate for the '2'
        for x in reversed(nums):
            if x < two:
                return True
            while stack and stack[-1] < x:
                two = stack.pop()
            stack.append(x)
        return False
```
