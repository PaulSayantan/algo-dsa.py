# Reverse the First K Elements of a Queue — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def reverseFirstK(self, q, k):
        stack = []
        for i in range(k):
            stack.append(q[i])
        result = []
        while stack:
            result.append(stack.pop())
        result.extend(q[k:])
        return result
```

Pushing the first `k` elements and popping them reverses just that prefix
(LIFO); the untouched tail `q[k:]` is appended in original order. Runs in O(n)
time and O(k) extra space for the stack.
