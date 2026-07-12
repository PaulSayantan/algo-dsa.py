# Palindrome Check with a Deque — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def isPalindrome(self, s):
        dq = deque(s)
        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False
        return True
```
