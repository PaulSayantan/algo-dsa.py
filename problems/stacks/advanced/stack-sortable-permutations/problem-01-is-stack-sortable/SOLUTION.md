# Is a Permutation Stack-Sortable? — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def isStackSortable(self, perm):
        stack = []
        want = 1
        for x in perm:
            stack.append(x)
            while stack and stack[-1] == want:
                stack.pop()
                want += 1
        return not stack
```
