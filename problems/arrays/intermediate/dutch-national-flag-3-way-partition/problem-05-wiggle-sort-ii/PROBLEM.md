# Wiggle Sort II

**Difficulty:** Hard

**Source:** LeetCode 324 — Wiggle Sort II

## Description

Given an integer array `nums`, reorder it **in place** so that it follows the strict wiggle
pattern:

```
nums[0] < nums[1] > nums[2] < nums[3] > nums[4] < ...
```

That is, every even-indexed element is strictly less than its right neighbor, and every
odd-indexed element is strictly greater than its right neighbor. It is guaranteed that a
valid reordering exists for the given input.

**Follow-up:** Can you do it in O(n) time (on average) and/or with O(1) extra space?

Note the contrast with "Wiggle Sort I": here the comparisons are **strict** (`<` and `>`),
so equal neighbors are not allowed. This is what forces careful handling of duplicate values
around the median — a natural fit for a Dutch National Flag partition combined with an
index-mapping placement.

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `0 <= nums[i] <= 5000`
- It is guaranteed that there is a valid answer for the given input `nums`.

## Examples

### Example 1

```
Input:  nums = [1, 5, 1, 1, 6, 4]
Output: [1, 6, 1, 5, 1, 4]
```

Explanation: Check the pattern: `1 < 6 > 1 < 5 > 1 < 4`. Every relation holds, so this is a
valid wiggle ordering. (Other valid answers exist, e.g. `[1,4,1,5,1,6]`.)

### Example 2

```
Input:  nums = [1, 3, 2, 2, 3, 1]
Output: [2, 3, 1, 3, 1, 2]
```

Explanation: Check the pattern: `2 < 3 > 1 < 3 > 1 < 2`. All relations hold. The two
duplicate `3`s and duplicate `2`s are placed so that equal values never sit next to each
other.

### Example 3

```
Input:  nums = [1]
Output: [1]
```

Explanation: A single element trivially satisfies the (empty) wiggle constraint.

## Hint

Find the **median** (via quickselect), then partition the values into `< median`,
`== median`, `> median` using the **Dutch National Flag (3-way partition)**. Placing the
smaller half into the even index slots and the larger half into the odd index slots — in a
specific order that pushes the median copies as far apart as possible — produces a strict
wiggle even when there are many duplicates.
