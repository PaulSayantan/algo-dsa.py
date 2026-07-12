# Pixel Canvas with Command Undo/Redo

**Difficulty:** Easy

**Source:** Classic — command-object (inverse-operation) undo/redo

## Description

Design a small pixel canvas where every cell starts blank (color `0`). Unlike a
full-snapshot editor, this canvas records each edit as a **command** — just the
single cell that changed and the color it held *before* the edit — so an undo
replays the inverse of one operation instead of restoring a whole saved state.

Implement the `Canvas` class:

- `Canvas()` — initializes an empty canvas; every cell is `0`.
- `paint(r, c, color)` — sets cell `(r, c)` to `color`, recording an inverse
  command so the change can be undone. This clears the redo history.
- `undo()` — reverts the most recent `paint`/`redo` change by replaying its
  inverse command. Does nothing if there is nothing to undo.
- `redo()` — reapplies the most recently undone change. Does nothing if there is
  nothing to redo.
- `color(r, c)` — returns the current color of cell `(r, c)`.

A new `paint` clears the redo history.

## Examples

### Example 1

```
Input:
["Canvas", "paint", "paint", "color", "undo", "color", "paint", "redo", "color", "color"]
[[], [0, 0, 3], [0, 0, 8], [0, 0], [], [0, 0], [1, 1, 4], [], [0, 0], [1, 1]]

Output:
[null, null, null, 8, null, 3, null, null, 3, 4]
```

**Explanation:** `paint(0,0,3)` then `paint(0,0,8)` leaves cell `(0,0)` at `8`.
`undo()` replays the inverse of the last paint, restoring `(0,0)` to `3`.
`paint(1,1,4)` records a new command and clears the redo stack, so the pending
`redo()` does nothing and `(0,0)` stays `3` while `(1,1)` is `4`.

## Hint

Push an inverse command `(r, c, previous_color)` onto the undo stack on every
`paint` and clear the redo stack. `undo` pops that command, records the *current*
color as the inverse to redo, and restores the previous color; `redo` mirrors it.
Store only painted cells in a dict and treat a missing cell as color `0`.
