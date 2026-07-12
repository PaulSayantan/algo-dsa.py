# Text Editor with Undo/Redo — Solution

## Optimal Approach

### Reference implementation

```python
class TextEditor:
    def __init__(self):
        self._text = ''
        self._undo = []
        self._redo = []

    def type(self, word):
        self._undo.append(self._text)
        self._redo.clear()
        self._text += word

    def undo(self):
        if self._undo:
            self._redo.append(self._text)
            self._text = self._undo.pop()

    def redo(self):
        if self._redo:
            self._undo.append(self._text)
            self._text = self._redo.pop()

    def text(self):
        return self._text
```
