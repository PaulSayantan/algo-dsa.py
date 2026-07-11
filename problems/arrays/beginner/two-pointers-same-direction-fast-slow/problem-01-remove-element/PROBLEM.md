# Remove Element

**Difficulty:** Easy

**Source:** LeetCode 27 (Remove Element)

## Description

You are given an integer array `nums` and an integer `val`. Remove **all
occurrences** of `val` in `nums` **in place**. The relative order of the elements
that remain may be changed.

Since it is impossible to change the length of the array in some languages, you
must instead return `k`, the number of elements in `nums` that are **not** equal
to `val`, and arrange the array so that the **first `k` elements** of `nums`
contain the elements that are not equal to `val`. The elements beyond the first
`k` positions do not matter (they can be anything).

Return `k`.

You must do this using only O(1) extra space.

## Constraints

- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`

## Examples

### Example 1

```
Input:  nums = [3, 2, 2, 3], val = 3
Output: 2, nums = [2, 2, _, _]
```

**Explanation:** Your function should return `k = 2`, with the first two elements
of `nums` being `2`. The two underscores are positions we no longer care about.

### Example 2

```
Input:  nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
Output: 5, nums = [0, 1, 3, 0, 4, _, _, _]
```

**Explanation:** Your function should return `k = 5`, with the first five
elements of `nums` being `0, 1, 3, 0, 4` in any order. There are five values not
equal to `2`, so `k = 5`.

### Example 3

```
Input:  nums = [2, 2, 2], val = 2
Output: 0, nums = [_, _, _]
```

**Explanation:** Every element equals `val`, so nothing is kept and `k = 0`.

## Hint

Use **Two Pointers (same direction / fast-slow)**: let a *reader* pointer scan
every element while a *writer* pointer marks where the next kept element goes.
Only copy elements that are not equal to `val`.
