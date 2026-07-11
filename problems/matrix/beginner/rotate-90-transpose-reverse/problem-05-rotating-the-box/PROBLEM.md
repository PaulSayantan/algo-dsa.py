# Rotating the Box

**Difficulty:** Medium

**Source:** LeetCode 1861 — Rotating the Box

## Description

You are given an `m × n` matrix of characters `box` representing a side-view of
a box. Each cell is one of:

- `'#'` — a stone
- `'*'` — a stationary obstacle
- `'.'` — empty space

The box is rotated **90 degrees clockwise**. Because of gravity, when the box is
rotated the stones fall (as far down as possible), landing on the box's floor,
on an obstacle, or on another stone. Gravity does **not** affect obstacles, and
the inertia from the rotation does not move the stones horizontally in the
initial (pre-rotation) frame.

Return an `n × m` matrix representing the box **after** the rotation.

The core of the answer is a 90° clockwise rotation. The subtlety is that gravity
must be resolved first, in the original orientation, before the Rotate 90°
technique is applied.

## Constraints

- `m == box.length`
- `n == box[i].length`
- `1 <= m, n <= 500`
- `box[i][j]` is `'#'`, `'*'`, or `'.'`

## Examples

### Example 1

```
Input:  box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]
```

Explanation: In the single row, the two stones settle to the right past the
empty cell → `[".","#","#"]`. Rotating that row 90° clockwise turns it into a
column, top to bottom: `.`, `#`, `#`.

### Example 2

```
Input:  box = [["#",".","*","."],
               ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]
```

Explanation: Stones in each row fall right until they hit the obstacle `*` or
the wall. Row 0 becomes `[".","#","*","."]` and row 1 becomes
`[".","#","#","*"]`. Rotating clockwise (transpose, then reverse each row)
produces the 4×2 output shown.

### Example 3

```
Input:  box = [["#","#","*",".","*","."],
               ["#","#","#","*",".","."],
               ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]
```

Explanation: After gravity pulls stones rightward within each row (stopping at
obstacles), a 90° clockwise rotation yields the 6×3 grid shown.

## Hint

Resolve gravity first: for each row, let stones settle toward the right, stopping
at obstacles or the right wall. Then apply Rotate 90° (transpose + reverse) — a
clockwise turn is transpose followed by reversing each row.
