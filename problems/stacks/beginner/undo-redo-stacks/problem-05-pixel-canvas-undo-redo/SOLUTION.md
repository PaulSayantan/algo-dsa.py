# Pixel Canvas with Command Undo/Redo — Solution

## Optimal Approach

Instead of snapshotting the entire canvas on every edit, record each `paint` as a
small **inverse command**: the cell that changed and the color it held *before*
the edit. The undo stack holds these commands; undoing replays the inverse of one
operation (restore the previous color), which is O(1) regardless of canvas size.

`paint` pushes `(r, c, previous_color)` onto the undo stack, clears the redo stack
(a fresh edit invalidates any redo path), and applies the new color. `undo` pops
the last command, pushes an inverse describing the *current* color onto the redo
stack, and restores the previous color. `redo` is the mirror image. Painted cells
live in a dict keyed by `(r, c)`; a missing cell is color `0`, and painting a cell
back to `0` removes it so the map stays sparse.

### Reference implementation

```python
class Canvas:
    def __init__(self):
        self._cells = {}   # (r, c) -> color; absent means 0 (blank)
        self._undo = []    # inverse commands: (r, c, prev_color)
        self._redo = []    # inverse commands staged for reapply

    def _get(self, r, c):
        return self._cells.get((r, c), 0)

    def _set(self, r, c, color):
        if color == 0:
            self._cells.pop((r, c), None)
        else:
            self._cells[(r, c)] = color

    def paint(self, r, c, color):
        self._undo.append((r, c, self._get(r, c)))  # remember how to revert
        self._redo.clear()
        self._set(r, c, color)

    def undo(self):
        if self._undo:
            r, c, prev = self._undo.pop()
            self._redo.append((r, c, self._get(r, c)))
            self._set(r, c, prev)

    def redo(self):
        if self._redo:
            r, c, val = self._redo.pop()
            self._undo.append((r, c, self._get(r, c)))
            self._set(r, c, val)

    def color(self, r, c):
        return self._get(r, c)
```
