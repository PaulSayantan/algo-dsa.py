# Holes — Ball Jumping with Power Updates

**Difficulty:** Hard

**Source:** Codeforces 13E — "Holes" (adapted to 0-indexed arrays).

## Description

There is a row of `n` holes, numbered `0` to `n - 1`. Each hole `i` has a
positive **power** `powers[i]`. When a ball is thrown into hole `i`, it
immediately jumps to hole `i + powers[i]`. From there it jumps again by that
hole's power, and so on, until a jump would send it to an index `>= n` — at
that point the ball **leaves the row**.

Support two operations, issued in any order:

- `set_power(index, val)` — set `powers[index] = val` (a positive integer).
- `throw(start)` — throw a ball into hole `start` and report two things:
  1. the index of the **last hole** the ball occupied before leaving the row,
     and
  2. the **total number of jumps** the ball made.

Simulating each throw jump-by-jump is `O(n)` per throw in the worst case (for
example when every power is `1`), which is too slow when many throws and updates
are interleaved. You must make both operations sublinear on average.

Implement the `Holes` class:

- `Holes(int[] powers)` — initializes the row.
- `void set_power(int index, int val)` — updates one hole's power.
- `int[] throw(int start)` — returns `[last_hole, num_jumps]`.

## Constraints

- `1 <= n = powers.length <= 1 * 10^5`
- `1 <= powers[i] <= n`
- `0 <= index, start < n`
- `1 <= val <= n`
- At most `1 * 10^5` calls total to `set_power` and `throw`.

## Examples

### Example 1
- **Input:**
  ```
  ["Holes", "throw", "set_power", "throw"]
  [[[2, 1, 1, 3, 1, 2]], [0], [2, 4], [0]]
  ```
- **Output:** `[null, [3, 3], null, [2, 2]]`
- **Explanation:**
  - `throw(0)`: `0 -> 2 -> 3 -> 6`. Index `6 >= 6` leaves the row, so the last
    occupied hole is `3` after `3` jumps → `[3, 3]`.
  - `set_power(2, 4)` changes powers to `[2, 1, 4, 3, 1, 2]`.
  - `throw(0)`: `0 -> 2 -> 6`. The last occupied hole is `2` after `2` jumps →
    `[2, 2]`.

### Example 2
- **Input:**
  ```
  ["Holes", "throw", "throw", "set_power", "throw"]
  [[[1, 1, 1, 1, 1]], [0], [2], [1, 10], [0]]
  ```
- **Output:** `[null, [4, 5], [4, 3], null, [1, 2]]`
- **Explanation:**
  - `throw(0)`: `0 -> 1 -> 2 -> 3 -> 4 -> 5`. Last hole `4`, `5` jumps →
    `[4, 5]`.
  - `throw(2)`: `2 -> 3 -> 4 -> 5`. Last hole `4`, `3` jumps → `[4, 3]`.
  - `set_power(1, 10)` changes powers to `[1, 10, 1, 1, 1]`.
  - `throw(0)`: `0 -> 1 -> 11`. Last hole `1`, `2` jumps → `[1, 2]`.

## Hint

Use **Square Root Decomposition**. Split the holes into blocks of size about
`sqrt(n)` and, for each hole, precompute (a) how many jumps it takes to leave
its *block*, (b) which hole it lands on right after leaving the block, and (c)
the last hole visited inside the block. A throw then hops block-to-block instead
of hole-to-hole, and a `set_power` only recomputes the one block it touches.
