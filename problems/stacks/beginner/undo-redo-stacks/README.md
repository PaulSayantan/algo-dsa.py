# Undo / Redo Stacks

Editors and text buffers implement undo/redo with two stacks: performing an action pushes its (reversible) state onto the undo stack and clears the redo stack; undo pops from undo and pushes onto redo; redo does the reverse. LIFO gives the correct most-recent-first ordering.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Text Editor with Undo/Redo](problem-01-text-editor-undo-redo/PROBLEM.md) | Two-stack undo/redo | Medium |
| 2 | [Design Browser History](problem-02-design-browser-history/PROBLEM.md) | Back/forward stacks; visit clears redo | Easy |
| 3 | [Baseball Game](problem-03-baseball-game/PROBLEM.md) | Score stack; `C` undoes last score | Easy |
| 4 | [Backspace String Compare](problem-04-backspace-string-compare/PROBLEM.md) | Build string on a stack; `#` is undo | Easy |
| 5 | [Pixel Canvas with Command Undo/Redo](problem-05-pixel-canvas-undo-redo/PROBLEM.md) | Command-object (inverse-op) undo/redo | Easy |
