# Minimum Number of Arrows to Burst Balloons — Solution

This is the "dual" of activity selection. Every arrow position corresponds to a point
that stabs a group of mutually overlapping balloons. The minimum number of arrows
equals the maximum number of **pairwise non-overlapping** balloons — but we compute it
directly with the same sort-by-end greedy.

## Brute Force

Try candidate arrow positions (e.g. every distinct endpoint), and search for the
smallest set of positions such that each balloon contains at least one chosen position.
This is a set-cover-flavored search and blows up combinatorially.

- **Time:** exponential in the worst case.
- **Space:** `O(n)`.

Not viable for `n` up to `10^5`.

## Optimal Approach (Meeting Rooms / Interval Scheduling — greedy)

Sort balloons by their **end** coordinate. Fire an arrow at the end of the
earliest-finishing balloon; it bursts that balloon and every later balloon that starts
at or before this position. Only when a balloon starts strictly *after* the current
arrow do we need a new arrow, placed at that balloon's end.

Steps:

1. Sort `points` by `x_end`.
2. Initialize `arrows = 1` and `arrow_x = points[0][1]` (shoot at the first balloon's
   end).
3. For each balloon `[s, e]` from the second onward:
   - If `s > arrow_x`, the current arrow cannot reach this balloon → shoot a new arrow:
     `arrows += 1` and `arrow_x = e`.
   - Otherwise `s <= arrow_x`, so the current arrow already bursts it — do nothing.
4. Return `arrows`.

```python
def findMinArrowShots(points):
    points.sort(key=lambda p: p[1])
    arrows = 1
    arrow_x = points[0][1]
    for s, e in points[1:]:
        if s > arrow_x:        # cannot reach -> new arrow
            arrows += 1
            arrow_x = e
    return arrows
```

- **Time:** `O(n log n)` for the sort, `O(n)` for the sweep.
- **Space:** `O(1)` extra beyond the sort.

### Why it is correct

By sorting on end coordinate, the first balloon has the smallest end `e_0`. Any arrow
that bursts this balloon must land at some `x <= e_0`; placing it exactly at `e_0`
maximizes reach to the right and therefore bursts a superset of what any other valid
position for this balloon could. So there is always an optimal solution shooting at
`e_0`. Remove every balloon that `e_0` bursts and recurse on the rest — the same
argument applies to the next surviving balloon. This exchange argument shows the greedy
uses the fewest arrows.

## Key Insights & Edge Cases

- **`points` is guaranteed non-empty** (`length >= 1`), so `arrows` starts at 1. If you
  handle a possibly-empty input, return `0` when `points` is empty.
- **Touching balloons share an arrow:** `[1, 2]` and `[2, 3]` overlap at `x = 2`. Use
  `s > arrow_x` (strict) so a start equal to the arrow position still counts as a hit.
- **Beware integer overflow in other languages.** Endpoints span the full 32-bit range;
  comparing `s > arrow_x` is safe, but computing midpoints like `(s + e) // 2` can
  overflow in languages with fixed-width ints — Python is immune. Shooting at the end
  coordinate avoids any arithmetic entirely.
- **Fully disjoint balloons** need one arrow each (Example 2).
