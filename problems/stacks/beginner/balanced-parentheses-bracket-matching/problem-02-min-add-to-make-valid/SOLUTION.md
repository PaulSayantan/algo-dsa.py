# Minimum Add to Make Parentheses Valid — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def minAddToMakeValid(self, s):
        open_needed = 0  # unmatched ')'
        balance = 0      # unmatched '('
        for c in s:
            if c == '(':
                balance += 1
            else:
                if balance:
                    balance -= 1
                else:
                    open_needed += 1
        return open_needed + balance
```
