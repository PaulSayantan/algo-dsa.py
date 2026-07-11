# The Untended Antiquity

**Difficulty:** Hard

**Source:** Codeforces 869E — "The Untended Antiquity"

## Description

You have an `n x m` grid (1-indexed). You process `q` operations of three kinds:

- `1 r1 c1 r2 c2` — **add a barrier**: build a wall along the *outer boundary* of
  the rectangle with corners `(r1, c1)` and `(r2, c2)`. It is guaranteed the new
  barrier does not intersect or touch any existing barrier.
- `2 r1 c1 r2 c2` — **remove a barrier**: remove the barrier that was previously
  added with exactly these corners (guaranteed to exist).
- `3 r1 c1 r2 c2` — **query**: can a token walk between cells `(r1, c1)` and
  `(r2, c2)` moving only up/down/left/right between adjacent cells **without
  crossing any barrier**? Print `Yes` or `No`.

Because barriers never intersect or touch, any two barrier rectangles are either
**strictly nested** or **completely disjoint**. Consequently, two cells are
connected **iff they are enclosed by exactly the same set of barriers** — the
grid never needs an actual pathfinding search.

## Constraints

- `1 <= n, m <= 2500`
- `1 <= q <= 10^5`
- For add/query, `1 <= r1 <= r2 <= n` and `1 <= c1 <= c2 <= m`.
- Added barriers never touch or intersect existing barriers.
- A remove op always names a currently-present barrier.

## Examples

### Example 1

```
Input:
5 6 5
1 2 2 4 5
1 3 3 3 3
3 4 4 1 1
2 2 2 4 5
3 1 1 4 4

Output:
No
Yes
```

**Explanation:**
- Barrier `A = (2,2)-(4,5)` and barrier `B = (3,3)-(3,3)` are added; `B` is
  nested inside `A`.
- Query `(4,4) -> (1,1)`: cell `(4,4)` lies inside `A` but outside the tiny `B`,
  so its enclosing set is `{A}`; cell `(1,1)` is inside no barrier, so its set is
  `{}`. Different enclosing sets → `No`.
- Barrier `A` is removed (only `B` remains).
- Query `(1,1) -> (4,4)`: `(4,4)` was never inside `B` and `A` is gone, so its
  enclosing set is `{}`; `(1,1)`'s set is also `{}`. Same enclosing set → `Yes`.

### Example 2

```
Input:
3 3 4
3 1 1 3 3
1 2 2 2 2
3 2 2 1 1
3 1 1 1 3

Output:
Yes
No
Yes
```

**Explanation:**
- Query `(1,1) -> (3,3)` with no barriers: both enclosed by nothing → `Yes`.
- Add a barrier around the single cell `(2,2)`.
- Query `(2,2) -> (1,1)`: `(2,2)` is inside the barrier, `(1,1)` is outside →
  different sets → `No`.
- Query `(1,1) -> (1,3)`: both outside the barrier → same set → `Yes`.

## Hint

Give each barrier a **random 64-bit id**. "Adding a barrier" becomes a
**range-update** that XORs/adds that id to every cell inside the rectangle;
"remove" undoes it. A cell's accumulated value is a fingerprint of the set of
barriers enclosing it, so two cells are connected iff their fingerprints match —
implement the rectangle-add / point-read with a **2D BIT** and compare two point
reads.
