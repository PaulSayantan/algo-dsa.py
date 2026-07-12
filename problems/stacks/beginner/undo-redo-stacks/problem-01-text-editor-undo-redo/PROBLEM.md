# Text Editor with Undo/Redo

**Difficulty:** Medium

**Source:** Classic — two-stack undo/redo

## Description

Design a simple text buffer supporting: `type(word)` (append the word to the text), `undo()` (revert the last type/undo-able change), `redo()` (reapply the last undone change), and `text()` (return the current text). A new `type` clears the redo history.

## Hint

Keep an undo stack of previous states and a redo stack; type snapshots current state and clears redo.
