# Falling Squares

**Difficulty:** Hard

**Source:** LeetCode 699 — Falling Squares

## Description

There are several axis-aligned squares dropped one at a time onto the number line (the
X-axis). You are given a 2D array `positions` where `positions[i] = [left_i, sideLength_i]`
represents the `i`-th square with a side length `sideLength_i` whose left edge is aligned at
`left_i` on the X-axis.

Each square is dropped from a great height and falls straight down. It lands either on the
X-axis or on top of a previously dropped square, resting on the highest surface it overlaps
(squares that touch only at a single point — i.e. share just an edge boundary — do **not**
stack on each other). Once a square lands it stays put.

After dropping each square, record the height of the **tallest stack** so far. Return a list
`ans` where `ans[i]` is the maximum height of any square after the `i`-th drop.

The X-coordinates can be as large as `10^8`, but there are at most a few thousand distinct
edges. Compressing those edges into a small index range lets you run a segment tree
(range-max update + range-max query) over the intervals between consecutive edges.

## Constraints

- `1 <= positions.length <= 1000`
- `1 <= left_i <= 10^8`
- `1 <= sideLength_i <= 10^6`

## Examples

### Example 1

```
Input:  positions = [[1, 2], [2, 3], [6, 1]]
Output: [2, 5, 5]
```

**Explanation:**
- Drop square 1 covering `[1, 3]` with height 2 -> tallest is 2.
- Drop square 2 covering `[2, 5]`; it overlaps square 1, lands on top, top at height `2 + 3
  = 5` -> tallest is 5.
- Drop square 3 covering `[6, 7]`; it overlaps nothing, lands on the ground, height 1 ->
  tallest so far is still 5.

### Example 2

```
Input:  positions = [[100, 100], [200, 100]]
Output: [100, 100]
```

**Explanation:** Square 1 covers `[100, 200]` with height 100. Square 2 covers `[200, 300]`.
They touch only at the single point `x = 200`, which does **not** count as overlap, so
square 2 lands on the ground at height 100. The tallest stack is 100 after each drop.

## Hint

Use **Coordinate Compression** on the square edges, then a segment tree supporting range-max
assignment and range-max query over the compressed intervals.
