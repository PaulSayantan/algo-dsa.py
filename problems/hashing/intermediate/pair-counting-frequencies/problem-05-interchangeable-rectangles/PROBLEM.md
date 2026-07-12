# Number of Pairs of Interchangeable Rectangles

**Difficulty:** Medium

**Source:** LeetCode 2001 — Number of Pairs of Interchangeable Rectangles

## Description

You are given `rectangles` where `rectangles[i] = [width, height]`. Two rectangles are interchangeable if they have the same width-to-height ratio. Return the number of interchangeable pairs. Use the reduced fraction `(width/g, height/g)` (with `g = gcd`) as an exact, floating-point-free ratio key.

## Examples

### Example 1

```
Input:  rectangles = [[4,8],[3,6],[10,20],[15,30]]
Output: 6
```

**Explanation:** All four share ratio 1/2, giving C(4,2) = 6 pairs.

### Example 2

```
Input:  rectangles = [[4,5],[7,8]]
Output: 0
```

**Explanation:** Different ratios.

## Hint

Group by the gcd-reduced (w, h) tuple; add count[key] before incrementing it.
