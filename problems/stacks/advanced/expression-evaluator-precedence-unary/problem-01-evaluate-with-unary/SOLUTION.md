# Evaluate Expression with Unary Minus — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def evaluate(self, s):
        def apply(vals, op):
            b = vals.pop()
            a = vals.pop()
            if op == '+':
                vals.append(a + b)
            elif op == '-':
                vals.append(a - b)
            elif op == '*':
                vals.append(a * b)
            else:
                vals.append(int(a / b))

        prec = {'+': 1, '-': 1, '*': 2, '/': 2}
        vals = []
        ops = []
        i = 0
        n = len(s)
        prev = None  # 'num', ')', or an operator/'('
        while i < n:
            c = s[i]
            if c == ' ':
                i += 1
                continue
            if c.isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                vals.append(num)
                prev = 'num'
                continue
            if c == '(':
                ops.append(c)
                prev = '('
            elif c == ')':
                while ops and ops[-1] != '(':
                    apply(vals, ops.pop())
                ops.pop()
                prev = ')'
            else:  # operator
                if c == '-' and prev in (None, '(', '+', '-', '*', '/'):
                    vals.append(0)  # unary minus: 0 - x
                while ops and ops[-1] != '(' and prec[ops[-1]] >= prec[c]:
                    apply(vals, ops.pop())
                ops.append(c)
                prev = c
            i += 1
        while ops:
            apply(vals, ops.pop())
        return vals[-1]
```
