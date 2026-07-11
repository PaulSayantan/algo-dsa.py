# Container With Most Water

**Difficulty:** Medium

**Source:** LeetCode 11 (Container With Most Water)

## Description

You are given an integer array `height` of length `n`. There are `n` vertical
lines drawn such that the two endpoints of the `i`-th line are `(i, 0)` and
`(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the
container holds the most water. Return the **maximum amount of water** a
container can store.

Notice that you may not slant the container. The amount of water held between
lines `i` and `j` (with `i < j`) equals `min(height[i], height[j]) * (j - i)`.

## Constraints

- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

## Examples

### Example 1

```
Input:  height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49
```

Explanation: The best container uses the lines at indices `1` and `8` with
heights `8` and `7`. Width is `8 - 1 = 7`, limiting height is
`min(8, 7) = 7`, so the area is `7 * 7 = 49`.

### Example 2

```
Input:  height = [1, 1]
Output: 1
```

Explanation: The only pair is indices `0` and `1`. Width is `1`, limiting height
is `min(1, 1) = 1`, so the area is `1 * 1 = 1`.

### Example 3

```
Input:  height = [4, 3, 2, 1, 4]
Output: 16
```

Explanation: The outermost lines at indices `0` and `4` both have height `4`.
Width is `4`, limiting height is `4`, so the area is `4 * 4 = 16`.

## Hint

Use the **Two Pointers** technique: start with the widest possible container
(one line at each end) and repeatedly move the pointer at the **shorter** line
inward, because that is the only move that could possibly increase the area.
