# Sort Colors

**Difficulty:** Medium

**Source:** LeetCode 75 — Sort Colors (a.k.a. the Dutch National Flag problem)

## Description

Given an array `nums` with `n` objects colored red, white, or blue, sort them
**in place** so that objects of the same color are adjacent, in the order red, white,
and blue.

The colors are represented by the integers `0` (red), `1` (white), and `2` (blue).

You must **not** use a library sort function. A two-pass counting sort is allowed but
the intended answer is a single pass with **constant extra space**: this is exactly the
**3-way partition** used inside Quick Sort, where you partition the array into three
regions — values less than the pivot, equal to the pivot, and greater than the pivot —
around the pivot value `1`.

## Constraints

- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` is either `0`, `1`, or `2`.

## Examples

### Example 1

```
Input:  nums = [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]
Explanation: All 0s come first, then all 1s, then all 2s.
```

### Example 2

```
Input:  nums = [2, 0, 1]
Output: [0, 1, 2]
Explanation: One of each color, arranged red, white, blue.
```

### Example 3

```
Input:  nums = [0]
Output: [0]
Explanation: A single element is trivially sorted.
```

## Hint

Treat `1` as the pivot and apply a **3-way partition** (the Dutch National Flag
scheme), the same partitioning step Quick Sort uses to handle many duplicate keys.
Maintain three pointers to grow a `< pivot` region, a `> pivot` region, and scan the
middle in a single pass.
