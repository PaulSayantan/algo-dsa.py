# Design Count-Min Sketch

**Difficulty:** Medium

**Source:** Classic — Count-Min Sketch (frequency sketch)

## Description

Implement a Count-Min Sketch with `depth = d` rows and `width = w` columns. Row `r` hashes with `col_r(x) = (x * 2654435761 + (r+1) * 40503) mod w`. `update(x, c)` adds `c` to `table[r][col_r(x)]` for every row; `estimate(x)` returns the minimum of those `d` counters. The estimate never underestimates the true count.

## Examples

### Example 1

```
Input:  update(5,3); estimate(5)
Output: 3
```

**Explanation:** No collisions, so the min counter equals the true count.

### Example 2

```
Input:  estimate(9) (never added)
Output: 0
```

**Explanation:** All of 9's counters are still zero.

## Hint

One counter per row indexed by that row's hash; estimate is the min across rows.
