# Pratt-Parse and Evaluate (with Power) — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def evaluate(self, s):
        tokens = []
        i = 0
        while i < len(s):
            c = s[i]
            if c == ' ':
                i += 1
            elif c.isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                tokens.append(num)
            else:
                tokens.append(c)
                i += 1
        pos = [0]

        def parse(min_bp):
            tok = tokens[pos[0]]
            pos[0] += 1
            if tok == '(':
                left = parse(0)
                pos[0] += 1  # skip ')'
            elif tok == '-':
                left = -parse(100)  # unary minus
            else:
                left = tok
            while pos[0] < len(tokens):
                op = tokens[pos[0]]
                if op not in ('+', '-', '*', '/', '^'):
                    break
                lbp = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}[op]
                if lbp < min_bp:
                    break
                pos[0] += 1
                right_bp = lbp if op == '^' else lbp + 1
                right = parse(right_bp)
                if op == '+':
                    left = left + right
                elif op == '-':
                    left = left - right
                elif op == '*':
                    left = left * right
                elif op == '/':
                    left = int(left / right)
                else:
                    left = left ** right
            return left

        return parse(0)
```
