# Remove Duplicates from Sorted Array

**Difficulty:** Easy

**Source:** LeetCode 26 (Remove Duplicates from Sorted Array)

## Description

Given an integer array `nums` sorted in **non-decreasing order**, remove the
duplicates **in place** such that each unique element appears only once. The
relative order of the elements should be kept the same. Then return the number
of unique elements in `nums`.

Consider the number of unique elements to be `k`. To be accepted, you must do the
following:

- Change the array `nums` such that the first `k` elements of `nums` contain the
  unique elements in the order they were present originally. The remaining
  elements of `nums` (beyond position `k`) do not matter.
- Return `k`.

You must modify the array in place with `O(1)` extra memory.

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in non-decreasing order.

## Examples

### Example 1

```
Input:  nums = [1, 1, 2]
Output: 2, nums = [1, 2, _]
```

Explanation: The function returns `k = 2`, with the first two elements of `nums`
being `1` and `2` respectively. The underscore denotes a position whose value is
irrelevant.

### Example 2

```
Input:  nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
```

Explanation: The function returns `k = 5`, with the first five elements being
`0`, `1`, `2`, `3`, and `4`.

### Example 3

```
Input:  nums = [5]
Output: 1, nums = [5]
```

Explanation: A single element is already unique, so `k = 1`.

## Hint

Use the **Two Pointers** technique in the same direction: a slow "write" pointer
marks where the next unique value belongs, while a fast "read" pointer scans
ahead. Because the array is sorted, duplicates are always adjacent.
