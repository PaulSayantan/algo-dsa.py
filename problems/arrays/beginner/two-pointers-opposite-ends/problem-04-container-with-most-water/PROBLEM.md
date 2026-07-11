# Container With Most Water

**Difficulty:** Medium

**Source:** LeetCode 11 — Container With Most Water

## Description

You are given an integer array `height` of length `n`. There are `n` vertical
lines drawn such that the two endpoints of the `i`-th line are `(i, 0)` and
`(i, height[i])`.

Find two lines that, together with the x-axis, form a container that holds the
**most water**. Return the maximum amount of water a container can store.

The amount of water held between line `i` and line `j` (with `i < j`) is
`min(height[i], height[j]) * (j - i)` — the shorter of the two walls determines
the water level, and the horizontal distance is the width. You may **not** slant
the container.

## Constraints

- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

## Examples

### Example 1
- **Input:** `height = [1, 8, 6, 2, 5, 4, 8, 3, 7]`
- **Output:** `49`
- **Explanation:** The best container uses the lines at indices `1` and `8`
  (heights `8` and `7`). Water = `min(8, 7) * (8 - 1) = 7 * 7 = 49`.

### Example 2
- **Input:** `height = [1, 1]`
- **Output:** `1`
- **Explanation:** Only one container is possible, using both lines:
  `min(1, 1) * (1 - 0) = 1`.

### Example 3
- **Input:** `height = [4, 3, 2, 1, 4]`
- **Output:** `16`
- **Explanation:** The outermost lines (indices `0` and `4`, both height `4`)
  give `min(4, 4) * (4 - 0) = 4 * 4 = 16`, which is the maximum.

## Hint

Use **Two Pointers (opposite ends)**: start with the widest possible container
(both ends) and move the pointer at the **shorter** wall inward, since that is
the only move that could ever increase the area.
