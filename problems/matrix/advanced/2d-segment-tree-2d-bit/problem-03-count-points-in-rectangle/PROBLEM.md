# Count Points in a Rectangle

**Difficulty:** Medium

**Source:** Classic 2D range-counting / Codeforces-style problem
("Points and Queries"). Related: LeetCode 2250 — Count Number of Rectangles
Containing Each Point.

## Description

You must support a stream of operations over integer lattice points in a grid:

- `add x y` — insert a new point at coordinates `(x, y)`. Multiple points may
  share the same coordinates.
- `count x1 y1 x2 y2` — report how many currently-inserted points `(x, y)`
  satisfy `x1 <= x <= x2` and `y1 <= y <= y2` (an axis-aligned rectangle,
  inclusive on all sides).

Operations are given **online** and interleaved — you must answer each `count`
before seeing later operations, so you cannot simply sort everything up front.

Return the answer to every `count` query, in order.

## Constraints

- Number of operations `q` satisfies `1 <= q <= 2 * 10^5`.
- All coordinates satisfy `1 <= x, y <= 10^9`.
- For every `count` query, `x1 <= x2` and `y1 <= y2`.
- Coordinates may repeat; the grid is sparse relative to the coordinate range.

## Examples

### Example 1

```
Input:
6
add 1 1
add 4 4
add 2 3
count 1 1 4 4
count 3 1 4 4
count 5 5 9 9

Output:
3
1
0
```

**Explanation:**
- After the three `add`s the points are `(1,1)`, `(4,4)`, `(2,3)`.
- `count 1 1 4 4` — all three points lie in `[1,4] x [1,4]` → `3`.
- `count 3 1 4 4` — only `(4,4)` has `x >= 3` → `1`.
- `count 5 5 9 9` — no point has `x >= 5` → `0`.

### Example 2

```
Input:
5
add 2 2
add 2 2
count 2 2 2 2
count 1 1 3 3
count 3 3 5 5

Output:
2
2
0
```

**Explanation:**
- Two points are inserted at the same location `(2,2)`.
- `count 2 2 2 2` — both points sit exactly on `(2,2)` → `2`.
- `count 1 1 3 3` — the rectangle contains `(2,2)`, covering both points → `2`.
- `count 3 3 5 5` — `(2,2)` is outside → `0`.

## Hint

Store point frequencies in a **2D Binary Indexed Tree** and answer each
rectangle with inclusion–exclusion of four prefix counts. Because coordinates
range up to `10^9`, first apply **coordinate compression** so the BIT
dimensions stay `O(q)`.
