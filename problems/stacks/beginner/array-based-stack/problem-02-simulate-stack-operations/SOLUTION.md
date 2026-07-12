# Simulate Stack Operations — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def finalStack(self, ops):
        st = []
        for op in ops:
            if op[0] == "push":
                st.append(op[1])
            elif op[0] == "pop":
                st.pop()
        return st
```
