# Sort Colors

**Difficulty:** Medium

**Source:** LeetCode 75 — Sort Colors (a.k.a. Dutch National Flag problem)

## Description

Given an array `nums` with `n` objects colored red, white, or blue, sort them **in place**
so that objects of the same color are adjacent, with the colors in the order red, white,
and blue.

The integers `0`, `1`, and `2` are used to represent the colors red, white, and blue,
respectively.

You must solve this problem **without using the library's sort function**, and the intended
solution runs in a **single pass** using only **constant extra space** (i.e., do not do a
count-then-overwrite two-pass approach if you can avoid it).

## Constraints

- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` is either `0`, `1`, or `2`.

## Examples

### Example 1

```
Input:  nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

Explanation: There are two 0s, two 1s, and two 2s. Grouped in the order red(0), white(1),
blue(2) they become `[0,0,1,1,2,2]`.

### Example 2

```
Input:  nums = [2,0,1]
Output: [0,1,2]
```

Explanation: One of each color; sorted ascending gives `[0,1,2]`.

### Example 3

```
Input:  nums = [1]
Output: [1]
```

Explanation: A single element is already sorted.

## Hint

Sort in one pass with three pointers using the **Dutch National Flag (3-way partition)**
technique: maintain a boundary for confirmed 0s, a scanning pointer, and a boundary for
confirmed 2s. Pivot value is `1`.
