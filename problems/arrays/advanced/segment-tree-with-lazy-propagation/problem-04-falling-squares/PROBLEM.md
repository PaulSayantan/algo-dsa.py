# Falling Squares

**Difficulty:** Hard

**Source:** LeetCode 699 — "Falling Squares".

## Description

There are several axis-aligned squares dropped, one at a time, onto the number
line (the X-axis). You are given a 2-D array `positions` where
`positions[i] = [left_i, sideLength_i]` means the `i`-th square has side length
`sideLength_i` and its **left edge** is at X-coordinate `left_i` (so it occupies
the interval `[left_i, left_i + sideLength_i]` on the X-axis).

Each square is dropped from a height above every currently landed square and falls
straight down. It lands either on the X-axis or on top of another square with which
it shares a positive-length horizontal overlap; its bottom rests at the highest
surface directly beneath it. Squares stick where they land (they do not topple or
merge).

After each square lands, record the **height of the tallest stack so far** (the
maximum top-edge height over all squares dropped up to and including this one).

Return a list `ans` where `ans[i]` is that running maximum after the `i`-th drop.

Two squares that only touch at a single point (share an edge but no positive-length
interval) do **not** stack on each other.

## Constraints

- `1 <= len(positions) <= 1000`
- `1 <= left_i <= 10^8`
- `1 <= sideLength_i <= 10^6`

## Examples

### Example 1

```
Input:
  positions = [[1, 2], [2, 3], [6, 1]]
Output:
  [2, 5, 5]
Explanation:
  Drop [1,2]: covers X in [1,3], lands on the ground, top height = 2.
              tallest so far = 2.
  Drop [2,3]: covers X in [2,5], overlaps the first square over [2,3],
              lands on top of it (base height 2), top height = 2 + 3 = 5.
              tallest so far = 5.
  Drop [6,1]: covers X in [6,7], overlaps nothing, lands on the ground,
              top height = 1. tallest so far = max(5, 1) = 5.
```

### Example 2

```
Input:
  positions = [[100, 100], [200, 100]]
Output:
  [100, 100]
Explanation:
  Drop [100,100]: covers X in [100,200], top height = 100. tallest = 100.
  Drop [200,100]: covers X in [200,300]. It only touches the first square at
                  the single point X = 200 (no positive-length overlap), so it
                  lands on the ground. top height = 100. tallest = max(100,100)=100.
```

## Hint

Compress the X-coordinates (endpoints of all intervals) into a small index space,
then use a **Segment Tree with Lazy Propagation** that supports *range assign to a
value* and *range maximum*. For each square, query the current max height over the
half-open interval it covers, add its side length to get its new top, then assign
that new top across the interval. Use half-open intervals so squares that merely
touch at a point do not interact.
