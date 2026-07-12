"""Pixel canvas with command-object (inverse-operation) undo/redo (design)."""


class Canvas:
    def __init__(self) -> None:
        # TODO: cell map (defaults to 0) + undo stack + redo stack of inverse commands
        pass

    def paint(self, r: int, c: int, color: int) -> None:
        # TODO: push inverse command (r, c, current color), clear redo, set color
        pass

    def undo(self) -> None:
        # TODO: pop last command, stage current color for redo, restore previous color
        pass

    def redo(self) -> None:
        # TODO: pop redo command, stage current color for undo, reapply color
        pass

    def color(self, r: int, c: int) -> int:
        # TODO: return current color of (r, c); 0 if never painted
        pass


if __name__ == "__main__":
    cv = Canvas()
    cv.paint(0, 0, 5)
    cv.paint(0, 0, 7)
    print(cv.color(0, 0))  # expected: 7
    cv.undo()
    print(cv.color(0, 0))  # expected: 5
    cv.undo()
    print(cv.color(0, 0))  # expected: 0
    cv.redo()
    print(cv.color(0, 0))  # expected: 5
    cv.paint(1, 2, 9)      # clears redo history
    print(cv.color(1, 2))  # expected: 9
    cv.redo()              # nothing staged to redo
    print(cv.color(0, 0))  # expected: 5
