# Describe the Painting

**Difficulty:** Medium

**Source:** LeetCode 1943 — "Describe the Painting"

## Description

There is a long, thin painting laid out on a number line. The painting is
described by overlapping colored segments. You are given a 2D array `segments`
where `segments[i] = [start_i, end_i, color_i]` means the half-open segment
`[start_i, end_i)` is painted with an integer `color_i`.

Colors mix additively: at any point covered by several segments, the observed
color is the **sum** of all the `color_i` values covering that point. Points
covered by nothing have no color and are not reported.

Return the painting described as a list of non-overlapping "painted segments"
`[left, right, mixedColor]`, where within `[left, right)` the mixed color is
constant and equal to `mixedColor`. A new segment must begin wherever the **set**
of active colors changes — that is, at every coordinate where some segment starts
or ends. (Two neighbors may therefore share the same numeric `mixedColor` yet
stay separate, because their underlying color *sets* differ.) Return the
segments sorted by `left`.

## Constraints

- `1 <= segments.length <= 2 * 10^4`
- `segments[i].length == 3`
- `1 <= start_i < end_i <= 10^5`
- `1 <= color_i <= 10^9`

## Examples

### Example 1

```
Input:  segments = [[1, 4, 5], [4, 7, 7], [1, 7, 9]]
Output: [[1, 4, 14], [4, 7, 16]]
Explanation:
  On [1, 4): colors 5 and 9 mix   -> 14.
  On [4, 7): colors 7 and 9 mix   -> 16.
  The two adjacent painted pieces have different mixed colors (14 vs 16),
  so they stay separate.
```

### Example 2

```
Input:  segments = [[1, 7, 9], [6, 8, 15], [8, 10, 7]]
Output: [[1, 6, 9], [6, 7, 24], [7, 8, 15], [8, 10, 7]]
Explanation:
  On [1, 6): only color 9              -> 9.
  On [6, 7): colors 9 and 15 mix       -> 24.
  On [7, 8): only color 15             -> 15.
  On [8, 10): only color 7             -> 7.
```

### Example 3

```
Input:  segments = [[1, 4, 5], [1, 4, 7], [4, 7, 1], [4, 7, 11]]
Output: [[1, 4, 12], [4, 7, 12]]
Explanation:
  On [1, 4): colors 5 and 7 mix   -> 12.
  On [4, 7): colors 1 and 11 mix  -> 12.
  Even though both pieces mix to 12, they are NOT merged because the painted
  region is described exactly: [1,4) and [4,7) are reported separately here
  ONLY because a color boundary falls at 4 (the running color sum actually
  changes at 4, then returns to 12). Adjacent pieces are merged only when the
  color sum is continuous across the boundary with no change.
```

## Hint

This is a **weighted** sweep that *emits output segments* rather than a single
number. Add `+color` at each `start` and `-color` at each `end`, then run a
**Sweep Line (1D events)**: walk the sorted distinct coordinates, and for each
gap between consecutive coordinates where the running color sum is nonzero,
output `[prev, cur, runningSum]`. Then merge neighboring pieces that share the
same sum with no coordinate/gap between them.
