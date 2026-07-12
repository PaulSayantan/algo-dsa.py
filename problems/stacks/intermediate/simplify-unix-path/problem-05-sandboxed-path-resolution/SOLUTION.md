# Sandboxed Path Resolution — Solution

## Optimal Approach

Start the `simplify-unix-path` stack seeded with the canonical components of
`root`, then fold `user_path` into it (skip empty/`.`, pop on `..`, push real
names). Because `root` is already on the stack, a `..` can only escape the jail
if it pops past `root`'s components. After resolving, confirm the stack is still
at least as deep as `root` and that its first `len(root)` components equal
`root`; if not, the path escaped, so return `""`.

### Reference implementation

```python
class Solution:
    def safeResolve(self, root, user_path):
        base = [p for p in root.split('/') if p]
        stack = list(base)
        for part in user_path.split('/'):
            if part == '' or part == '.':
                continue
            if part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        if len(stack) < len(base) or stack[:len(base)] != base:
            return ''
        return '/' + '/'.join(stack)
```
