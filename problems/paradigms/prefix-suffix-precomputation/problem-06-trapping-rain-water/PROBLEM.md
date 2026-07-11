# Trapping Rain Water

**Difficulty:** Hard

**Source:** LeetCode 42 — Trapping Rain Water

## Description

Given `n` non-negative integers representing an elevation map where the width of each
bar is `1`, compute how much water it can trap after raining.

Water sits on top of bar `i` up to the level of the **shorter** of the two tallest
walls on either side of it. The amount of water above bar `i` is therefore

```
water(i) = max(0, min(tallest bar to the left, tallest bar to the right) - height[i])
```

Return the total trapped water summed over all bars.

## Constraints

- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

## Examples

### Example 1

```
Input:  height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The elevation map traps 6 units of water. For instance, the dip
             between the bar of height 2 (index 3) and the bar of height 3
             (index 7) holds water up to level 2.
```

### Example 2

```
Input:  height = [4,2,0,3,2,5]
Output: 9
Explanation:
    index 1 (h=2): min(4,5) - 2 = 2
    index 2 (h=0): min(4,5) - 0 = 4
    index 3 (h=3): min(4,5) - 3 = 1
    index 4 (h=2): min(4,5) - 2 = 2
    Total = 2 + 4 + 1 + 2 = 9.
```

### Example 3

```
Input:  height = [2, 0, 2]
Output: 2
Explanation: The single dip at index 1 holds water up to level min(2, 2) = 2,
             so 2 - 0 = 2 units are trapped.
```

## Hint

Use **Prefix / Suffix Precomputation**: for each bar you need the tallest bar to its
**left** (a prefix-max) and the tallest bar to its **right** (a suffix-max). Since
`max` has no inverse, keep both arrays and combine them per index — or collapse them
into a two-pointer sweep for O(1) space.
