"""Text editor with undo/redo backed by two stacks (design)."""


class TextEditor:
    def __init__(self) -> None:
        # TODO: current text + undo stack + redo stack
        pass

    def type(self, word: str) -> None:
        # TODO
        pass

    def undo(self) -> None:
        # TODO
        pass

    def redo(self) -> None:
        # TODO
        pass

    def text(self) -> str:
        # TODO
        pass


if __name__ == "__main__":
    ed = TextEditor()
    ed.type("abc")
    ed.type("def")
    print(ed.text())  # expected: 'abcdef'
    ed.undo()
    print(ed.text())  # expected: 'abc'
    ed.redo()
    print(ed.text())  # expected: 'abcdef'
    ed.undo()
    ed.undo()
    print(ed.text())  # expected: ''
