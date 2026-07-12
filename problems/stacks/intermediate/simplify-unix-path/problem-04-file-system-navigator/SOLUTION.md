# Design File System Navigator — Solution

## Optimal Approach

Store the current directory as a list of surviving path components — exactly the
`simplify-unix-path` stack. On `cd`, clear the stack first if the argument is
absolute, then fold the argument's parts in: skip empty parts and `.`, pop on
`..` (bounded at root), and push any real name. `pwd` joins the stack with `/`
after a leading root `/`.

### Reference implementation

```python
class FileSystemNavigator:
    def __init__(self):
        self.stack = []

    def cd(self, path):
        if path.startswith('/'):
            self.stack = []
        for part in path.split('/'):
            if part == '' or part == '.':
                continue
            if part == '..':
                if self.stack:
                    self.stack.pop()
            else:
                self.stack.append(part)

    def pwd(self):
        return '/' + '/'.join(self.stack)
```
