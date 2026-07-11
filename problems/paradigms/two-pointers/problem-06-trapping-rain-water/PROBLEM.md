# Trapping Rain Water

**Difficulty:** Hard

**Source:** LeetCode 42 (Trapping Rain Water)

## Description

Given `n` non-negative integers representing an elevation map where the width of
each bar is `1`, compute how much water it can trap after raining.

Water sits on top of a bar `i` up to the height of the shorter of the two tallest
walls on its left and right. Formally, the water above index `i` is
`max(0, min(maxLeft(i), maxRight(i)) - height[i])`, where `maxLeft(i)` and
`maxRight(i)` are the tallest bars at or before `i` and at or after `i`
respectively. The answer is the sum of trapped water over all indices.

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

Explanation: The elevation map traps `6` units of water. For instance the dip
between the bar of height `2` (index 3) and the bar of height `3` (index 7) holds
several units, and smaller pockets contribute the rest.

### Example 2

```
Input:  height = [4, 2, 0, 3, 2, 5]
Output: 9
```

Explanation: Reading left to right, the bounded pockets above indices 1..4 hold
`2 + 4 + 1 + 2 = 9` units of water (bounded by the walls of height `4` on the
left and `5` on the right).

### Example 3

```
Input:  height = [3, 0, 2]
Output: 2
```

Explanation: The single dip at index 1 is bounded by walls of height `3` and `2`;
water rises to `min(3, 2) = 2`, and `2 - 0 = 2` units are trapped.

## Hint

Use the **Two Pointers** technique: converge from both ends while tracking the
running maximum wall seen from each side. The side with the smaller running
maximum determines how much water is trapped at that step.
