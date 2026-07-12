# Crawler Log Folder — Solution

## Optimal Approach

Only the final depth matters, so keep a running counter that behaves like the
size of a path-component stack: `../` pops (bounded at zero), `./` is a no-op,
and any other entry pushes a real folder name.

### Reference implementation

```python
class Solution:
    def minOperations(self, logs):
        depth = 0
        for log in logs:
            if log == '../':
                if depth > 0:
                    depth -= 1
            elif log == './':
                continue
            else:
                depth += 1
        return depth
```
