# Sort Colors

**Difficulty:** Medium

**Source:** LeetCode 75 — Sort Colors (the "Dutch National Flag" problem)

## Description

Given an array `nums` with `n` objects colored red, white, or blue, sort them **in place** so
that objects of the same color are adjacent, with the colors in the order red, white, and
blue.

We use the integers `0`, `1`, and `2` to represent the color red, white, and blue,
respectively.

You must solve this problem **without using the library's built-in sort function**. Because
there are only three possible values, you can count how many of each color exist and then
overwrite the array with the correct number of `0`s, then `1`s, then `2`s.

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

**Explanation:** There are two `0`s, two `1`s, and two `2`s. Writing them back in order
red-white-blue gives `[0,0,1,1,2,2]`.

### Example 2

```
Input:  nums = [2,0,1]
Output: [0,1,2]
```

**Explanation:** One of each color; sorted order is `[0,1,2]`.

### Example 3

```
Input:  nums = [0]
Output: [0]
```

**Explanation:** A single element is already sorted.

## Hint

There are only three distinct keys (`k = 3`), which is the ideal case for **Counting Sort**:
count the `0`s, `1`s, and `2`s in one pass, then overwrite `nums` in place with that many
`0`s, `1`s, and `2`s in order. (A one-pass three-pointer partition also works, but the
counting approach is the direct counting-sort application.)
