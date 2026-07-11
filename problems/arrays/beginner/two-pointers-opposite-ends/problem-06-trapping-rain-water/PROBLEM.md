# Trapping Rain Water

**Difficulty:** Hard

**Source:** LeetCode 42 — Trapping Rain Water

## Description

Given `n` non-negative integers representing an elevation map where the width of
each bar is `1`, compute how much water it can trap after raining.

Water sits on top of a bar `i` up to the level of the lower of the two tallest
bars to its left and to its right. Concretely, the water above index `i` is
`max(0, min(maxLeft[i], maxRight[i]) - height[i])`, where `maxLeft[i]` and
`maxRight[i]` are the tallest bars at or before / at or after index `i`. The
total trapped water is the sum over all indices.

## Constraints

- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

## Examples

### Example 1
- **Input:** `height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]`
- **Output:** `6`
- **Explanation:** The elevation map traps `6` units of water across the dips
  between the taller bars (for instance, water pools in the valleys around
  indices 2–6 and 8–10).

### Example 2
- **Input:** `height = [4, 2, 0, 3, 2, 5]`
- **Output:** `9`
- **Explanation:** Water is held above indices 1–4. For example index 2
  (height 0) sits under level `min(4, 5) = 4`, trapping `4` units; the pools at
  indices 1, 3, and 4 add the remaining `5`, totaling `9`.

### Example 3
- **Input:** `height = [3, 0, 2]`
- **Output:** `2`
- **Explanation:** The single dip at index 1 (height 0) is bounded by `3` on the
  left and `2` on the right, so it holds `min(3, 2) - 0 = 2` units.

## Hint

Use **Two Pointers (opposite ends)**: converge from both ends while tracking the
running maximum seen from the left and from the right. At each step the **lower**
running maximum determines how much water the current bar traps.
