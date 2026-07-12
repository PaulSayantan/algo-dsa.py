# Relative Path Between Directories — Solution

## Optimal Approach

Canonicalize each absolute path into a list of surviving components using the
`simplify-unix-path` stack (skip empty/`.`, pop on `..`). Walk both component
lists together to find the longest common prefix, then the relative path is one
`..` for every remaining source component followed by the remaining destination
components. An empty result means the two paths are equal, which we render as
`.`.

### Reference implementation

```python
class Solution:
    def relativePath(self, from_path, to_path):
        def canon(path):
            stack = []
            for part in path.split('/'):
                if part == '' or part == '.':
                    continue
                if part == '..':
                    if stack:
                        stack.pop()
                else:
                    stack.append(part)
            return stack

        src, dst = canon(from_path), canon(to_path)
        i = 0
        while i < len(src) and i < len(dst) and src[i] == dst[i]:
            i += 1
        parts = ['..'] * (len(src) - i) + dst[i:]
        return '/'.join(parts) if parts else '.'
```
