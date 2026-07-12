# Number of Atoms — Solution

## Optimal Approach

Same two-stack skeleton as decoding a nested string, but each frame holds an
atom-count map instead of a partial string. Scan left to right:

- `(` pushes a fresh empty count map (a new frame).
- `)` reads the trailing multiplier, pops the current frame, and merges every
  atom count times that multiplier into the frame below.
- An atom token (uppercase + lowercase*) with its optional trailing count is
  added into the current top frame.

At the end the bottom frame holds the totals; emit names in sorted order,
appending the count only when it exceeds `1`.

### Reference implementation

```python
class Solution:
    def countOfAtoms(self, formula):
        stack = [defaultdict(int)]
        i, n = 0, len(formula)
        while i < n:
            ch = formula[i]
            if ch == '(':
                stack.append(defaultdict(int))
                i += 1
            elif ch == ')':
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                mult = int(formula[start:i] or 1)
                top = stack.pop()
                for name, cnt in top.items():
                    stack[-1][name] += cnt * mult
            else:
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                name = formula[start:i]
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                cnt = int(formula[start:i] or 1)
                stack[-1][name] += cnt
        counts = stack[0]
        out = []
        for name in sorted(counts):
            out.append(name)
            if counts[name] > 1:
                out.append(str(counts[name]))
        return ''.join(out)
```
