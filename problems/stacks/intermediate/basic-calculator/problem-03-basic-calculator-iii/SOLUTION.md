# Basic Calculator III — Solution

## Optimal Approach

This is the term-stack calculator of Basic Calculator II extended with the
nested-context handling of Basic Calculator. We scan the string left to right,
keeping a pending operator `op` and building the current number `num`. On `+`/`-`
we push the (signed) term; on `*`/`/` we fold `num` into the last pushed term
immediately, so precedence is respected without any operator stack.

Parentheses are the only new piece: when we meet `(` we recursively evaluate the
sub-expression starting after it, and the recursive call's return value becomes
the current `num` — a single operand for whatever operator is pending. The
recursion stops when it consumes the matching `)` (or the end of input), and
summing the term stack at that level gives the group's value. Because every
character is visited once, the whole evaluation is O(n).

### Reference implementation

```python
class Solution:
    def calculate(self, s):
        def evaluate(it):
            stack = []
            num = 0
            op = '+'
            while True:
                ch = next(it, None)
                if ch is not None and ch.isdigit():
                    num = num * 10 + int(ch)
                elif ch == '(':
                    num = evaluate(it)
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
                    num = 0
                    if ch == ')' or ch is None:
                        break
                    op = ch
            return sum(stack)

        return evaluate(iter(s))
```
