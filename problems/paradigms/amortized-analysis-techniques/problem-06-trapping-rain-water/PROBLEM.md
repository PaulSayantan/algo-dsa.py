# Trapping Rain Water

**Difficulty:** Hard

**Source:** LeetCode 42 — Trapping Rain Water

## Description

Given `n` non-negative integers representing an elevation map where the width of each
bar is `1`, compute how much water it can trap after raining.

Water is trapped above a bar when there are taller bars on both its left and right; the
water level over any position is bounded by the shorter of the tallest bar to its left
and the tallest bar to its right.

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

Explanation: The elevation map traps `6` units of water. For instance, the dip between
the bar of height `2` (index 3) and the bar of height `3` (index 7) holds water above
indices 4, 5, 6, and smaller pockets contribute the rest.

### Example 2

```
Input:  height = [4, 2, 0, 3, 2, 5]
Output: 9
```

Explanation: Water pools in the wide basin bounded by the height-4 bar on the left and
the height-5 bar on the right, trapping `9` units total across indices 1..4.

### Example 3

```
Input:  height = [3, 0, 2]
Output: 2
```

Explanation: The single dip at index 1 (height 0) is bounded by `3` on the left and `2`
on the right, so the water level is `min(3, 2) = 2`, trapping `2 - 0 = 2` units.

## Hint

Use **Amortized Analysis Techniques** with a **monotonic decreasing stack** of bar
indices. When a bar taller than the stack top arrives, it forms a right wall: pop the
bottom of the dip, and the water sits between the new bar and the next bar left on the
stack. Each bar is pushed once and popped at most once, so the whole pass is O(n) even
though a single bar may close off many trapped layers.
