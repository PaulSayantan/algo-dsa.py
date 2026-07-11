# Sort an Array

**Difficulty:** Easy

**Source:** LeetCode 912 — "Sort an Array" (constrained here to a from-scratch Selection Sort;
LeetCode itself forbids the built-in sort).

## Description

Given an array of integers `nums`, return the array sorted in **ascending** order. You must
implement the sorting yourself rather than calling a language-provided sort. For this exercise,
implement **Selection Sort**: repeatedly find the minimum element of the not-yet-sorted suffix and
place it at the front of that suffix.

The array may contain duplicate values and negative numbers. You may sort the array in place and
return it, or return a new sorted array — either is accepted.

## Constraints

- `1 <= nums.length <= 5000`
- `-5 * 10^4 <= nums[i] <= 5 * 10^4`

## Examples

### Example 1

```
Input:  nums = [5, 2, 3, 1]
Output: [1, 2, 3, 5]
```

**Explanation:** Pass 1 finds the min `1` (at index 3) and swaps it with index 0 → `[1, 2, 3, 5]`.
Passes 2–3 find `2` and `3` already in place. The final array is `[1, 2, 3, 5]`.

### Example 2

```
Input:  nums = [5, 1, 1, 2, 0, 0]
Output: [0, 0, 1, 1, 2, 5]
```

**Explanation:** The two `0`s bubble to the front over the first two passes, then the two `1`s,
then `2`, then `5`. Duplicates are handled naturally because equal keys never force a swap.

### Example 3

```
Input:  nums = [-3, 0, -3, 7]
Output: [-3, -3, 0, 7]
```

**Explanation:** Negative numbers compare like any other integers; the smaller `-3` values are
selected first.

## Hint

Use **Selection Sort**: for each starting index `i`, scan `i .. n-1` to find the index of the
minimum element, then swap it into position `i`.
