# Trapping Rain Water

**Difficulty:** Hard

**Source:** LeetCode 42 — Trapping Rain Water

## Description

Given `n` non-negative integers representing an elevation map where the width of
each bar is `1`, compute how much water it can trap after raining.

Water sits on top of a bar up to the level of the shorter of the tallest bar to
its left and the tallest bar to its right. Bars at the two ends cannot trap any
water on their outer sides.

## Constraints

- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

## Examples

### Example 1

```
Input:  height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6

Explanation:
The elevation map traps 6 units of water. For instance, the dip at indices 4-6
(heights 1, 0, 1) is bounded by height 2 on the left (index 3) and height 3 on
the right (index 7), and the various valleys together hold 6 units.
```

### Example 2

```
Input:  height = [4, 2, 0, 3, 2, 5]
Output: 9

Explanation:
Water is trapped over the dips between the tall bars at index 0 (height 4) and
index 5 (height 5):
  index 1: min(4, 5) - 2 = 2
  index 2: min(4, 5) - 0 = 4
  index 3: min(4, 5) - 3 = 1
  index 4: min(4, 5) - 2 = 2
Total = 2 + 4 + 1 + 2 = 9.
```

## Hint

For each bar, the water above it is `min(maxLeft, maxRight) - height[i]`.
Precompute `maxRight` as a **Suffix Maximum** (a suffix aggregate using `max`
instead of `+`) and `maxLeft` as a prefix maximum, then combine in one pass.
