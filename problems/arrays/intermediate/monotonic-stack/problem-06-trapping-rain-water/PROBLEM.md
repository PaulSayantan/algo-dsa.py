# Trapping Rain Water

**Difficulty:** Hard

**Source:** LeetCode 42 — Trapping Rain Water

## Description

Given `n` non-negative integers representing an elevation map where the width of
each bar is `1`, compute how much water it can trap after raining.

Water sits on top of a bar up to the level of the lower of the tallest bars to
its left and to its right; the trapped amount at each position is
`min(max_left, max_right) - height`, when positive.

## Constraints

- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

## Examples

### Example 1

```
Input:  height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6
```

**Explanation:** The elevation map traps `6` units of water. For instance, the
dip between the `2` at index 3 and the `3` at index 7 holds water above the low
bars at indices 4, 5, 6.

### Example 2

```
Input:  height = [4, 2, 0, 3, 2, 5]
Output: 9
```

**Explanation:**
- Index 1 (h=2): bounded by 4 (left) and 5 (right) -> traps `min(4,5)-2 = 2`.
- Index 2 (h=0): traps `min(4,5)-0 = 4`.
- Index 3 (h=3): traps `min(4,5)-3 = 1`.
- Index 4 (h=2): traps `min(4,5)-2 = 2`.
- Total `2 + 4 + 1 + 2 = 9`.

### Example 3

```
Input:  height = [3, 0, 2, 0, 4]
Output: 7
```

**Explanation:** Index 1 traps `min(3,4)-0 = 3`, index 2 traps `min(3,4)-2 = 1`,
index 3 traps `min(3,4)-0 = 3`. Total `3 + 1 + 3 = 7`.

## Hint

Process bars left to right with a **Monotonic Stack** of indices kept
decreasing in height. Each time a taller bar arrives, it forms the right wall of
a trapped region; pop the bottom, and the water added is a horizontal layer
bounded by the new right wall and the bar now beneath it on the stack.
