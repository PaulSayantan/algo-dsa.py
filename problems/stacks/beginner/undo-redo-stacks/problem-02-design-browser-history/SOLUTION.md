# Design Browser History — Solution

## Optimal Approach

Keep the `current` page plus two stacks: `back_stack` holds the pages behind the
current one, `forward_stack` holds the pages ahead of it. `visit` is the "do an
action" step — it pushes the current page onto `back_stack`, moves to the new
URL, and clears `forward_stack` (a new action always invalidates the redo path).
`back` pops from `back_stack` onto `forward_stack`; `forward` does the reverse.
Bounding each loop by the available depth handles the "move only `x` steps" rule.

### Reference implementation

```python
class BrowserHistory:
    def __init__(self, homepage):
        self.current = homepage
        self.back_stack = []
        self.forward_stack = []

    def visit(self, url):
        self.back_stack.append(self.current)
        self.current = url
        self.forward_stack.clear()

    def back(self, steps):
        while steps > 0 and self.back_stack:
            self.forward_stack.append(self.current)
            self.current = self.back_stack.pop()
            steps -= 1
        return self.current

    def forward(self, steps):
        while steps > 0 and self.forward_stack:
            self.back_stack.append(self.current)
            self.current = self.forward_stack.pop()
            steps -= 1
        return self.current
```
