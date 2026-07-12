# Palindrome Check on a Queue — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def isPalindrome(self, q):
        stack = []
        for x in q:
            stack.append(x)
        reversed_q = []
        while stack:
            reversed_q.append(stack.pop())
        return reversed_q == list(q)
```
