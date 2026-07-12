# Evaluate Infix Arithmetic Expression — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def evaluate(self, expr):
        prec = {'+': 1, '-': 1, '*': 2, '/': 2}
        vals = []
        ops = []

        def apply():
            op = ops.pop()
            b = vals.pop()
            a = vals.pop()
            if op == '+':
                vals.append(a + b)
            elif op == '-':
                vals.append(a - b)
            elif op == '*':
                vals.append(a * b)
            else:
                vals.append(int(a / b))  # truncate toward zero

        i = 0
        n = len(expr)
        while i < n:
            c = expr[i]
            if c == ' ':
                i += 1
                continue
            if c.isdigit():
                num = 0
                while i < n and expr[i].isdigit():
                    num = num * 10 + int(expr[i])
                    i += 1
                vals.append(num)
                continue
            if c == '(':
                ops.append(c)
            elif c == ')':
                while ops and ops[-1] != '(':
                    apply()
                ops.pop()  # discard '('
            else:  # an operator
                while ops and ops[-1] in prec and prec[ops[-1]] >= prec[c]:
                    apply()
                ops.append(c)
            i += 1
        while ops:
            apply()
        return vals[-1]
```
