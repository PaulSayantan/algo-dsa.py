# Valid Palindrome (Alphanumeric Only) — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def isPalindrome(self, s):
        dq = deque(c.lower() for c in s if c.isalnum())
        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False
        return True
```
