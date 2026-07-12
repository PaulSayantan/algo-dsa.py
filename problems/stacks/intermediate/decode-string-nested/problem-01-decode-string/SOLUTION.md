# Decode String — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def decodeString(self, s):
        stack = []  # (prev_string, repeat)
        cur = ''
        num = 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                stack.append((cur, num))
                cur = ''
                num = 0
            elif ch == ']':
                prev, k = stack.pop()
                cur = prev + cur * k
            else:
                cur += ch
        return cur
```
