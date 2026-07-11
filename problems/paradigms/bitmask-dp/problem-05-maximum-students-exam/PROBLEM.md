# Maximum Students Taking Exam

**Difficulty:** Hard

**Source:** LeetCode 1349 (Maximum Students Taking Exam)

## Description

Given a `m x n` matrix `seats` that represents the seats distribution in a
classroom. If a seat is **broken**, it is denoted by `'#'`; otherwise, it is
denoted by a `'.'`.

Students can see the answers of those sitting next to them on the **left**,
**right**, **upper left**, and **upper right**, but **not** the seats directly
in front or behind them. Return the **maximum number of students** that can take
the exam together without any cheating being possible.

Students must be placed in seats in good condition (`'.'`), and the placement
must satisfy:

- No two students sit in horizontally adjacent seats (left/right).
- No student sits in the upper-left or upper-right seat of another student
  (diagonal front neighbours).

## Constraints

- `seats` contains only characters `'.'` and `'#'`.
- `m == seats.length`
- `n == seats[i].length`
- `1 <= m <= 8`
- `1 <= n <= 8`

## Examples

### Example 1

```
Input: seats = [["#", ".", "#", "#", ".", "#"],
                [".", "#", "#", "#", "#", "."],
                ["#", ".", "#", "#", ".", "#"]]
Output: 4
```

Explanation: Place 4 students in the available seats so no two are horizontally
adjacent and none is diagonally in front of another. One valid placement seats
two students in the top row (columns 1 and 4) and two in the bottom row
(columns 1 and 4); the middle row's two open seats (columns 0 and 5) conflict
diagonally and cannot both add students beyond this count.

### Example 2

```
Input: seats = [[".", "#"],
                ["#", "#"],
                ["#", "."],
                ["#", "#"],
                [".", "#"]]
Output: 3
```

Explanation: The only open seats are `(0,0)`, `(2,1)`, and `(4,0)`. No two of
them are horizontally adjacent, and none sits diagonally in front of another
(they are in non-consecutive rows or diagonally clear), so all 3 students can
be seated.

### Example 3

```
Input: seats = [["#", ".", ".", ".", "#"],
                [".", "#", ".", "#", "."],
                [".", ".", "#", ".", "."],
                [".", "#", ".", "#", "."],
                ["#", ".", ".", ".", "#"]]
Output: 10
```

Explanation: The broken seats break up the rows enough that 10 students can be
seated with no left/right adjacency and no upper-left/upper-right conflict.

## Hint

Each row has at most 8 seats, so a row's chosen-seat pattern fits in an 8-bit
integer. Do a **Bitmask DP** row by row: the DP state is the seating mask of the
current row, constrained by the previous row's mask (profile / broken-profile
DP).
