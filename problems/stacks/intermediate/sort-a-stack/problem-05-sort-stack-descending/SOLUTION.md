# Sort a Stack in Descending Order — Solution

## Optimal Approach

Mirror the ascending single-aux-stack sort. Pop each value from the input; before
pushing it onto the temp stack, move any temp elements that are *smaller* than it
back to the input. The temp stack ends up with the smallest value on top, which
is exactly the descending bottom-to-top order we return. Time O(n²), space O(n).

### Reference implementation

```python
class Solution:
    def sortStackDesc(self, stack):
        stack = list(stack)
        temp = []
        while stack:
            cur = stack.pop()
            while temp and temp[-1] < cur:
                stack.append(temp.pop())
            temp.append(cur)
        return temp
```
