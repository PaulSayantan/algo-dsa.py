# Basic Calculator II — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def calculate(self, s):
        stack = []
        num = 0
        op = '+'
        s = s + '+'
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == ' ':
                continue
            else:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                else:
                    prev = stack.pop()
                    stack.append(int(prev / num))
                op = ch
                num = 0
        return sum(stack)
```
