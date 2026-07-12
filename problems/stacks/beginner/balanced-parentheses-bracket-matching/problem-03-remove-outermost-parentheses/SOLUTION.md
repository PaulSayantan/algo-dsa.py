# Remove Outermost Parentheses — Solution

## Optimal Approach

Walk the string keeping a running `depth` (this mirrors a stack of open brackets). A `(` increments depth *after* deciding whether to keep it, and a `)` decrements depth *before* deciding. An opener seen at depth 0 and the closer that drops depth back to 0 are the outermost pair of a primitive, so we skip exactly those. O(n) time, O(n) output.

### Reference implementation

```python
class Solution:
    def removeOuterParentheses(self, s):
        res = []
        depth = 0
        for c in s:
            if c == '(':
                if depth > 0:
                    res.append(c)
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    res.append(c)
        return ''.join(res)
```
