# Sort an Array

**Difficulty:** Medium

**Source:** LeetCode 912 — Sort an Array

## Description

Given an array of integers `nums`, sort the array in **ascending order** and
return it.

You must solve the problem **without using any built-in sorting functions**, in
`O(n log n)` time complexity, and with the smallest space complexity possible.

This is the canonical exercise for implementing **heap sort** end to end:
build a max-heap over the array, then repeatedly swap the root (the current
maximum) to the end and restore the heap on the shrinking prefix.

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `-5 * 10^4 <= nums[i] <= 5 * 10^4`

## Examples

### Example 1

```
Input:  nums = [5,2,3,1]
Output: [1,2,3,5]
```

**Explanation:** After sorting in ascending order, `1` and `2` come before `3`
and `5`.

### Example 2

```
Input:  nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
```

**Explanation:** Values are not unique. Duplicate `0`s and `1`s are grouped
together and the whole array is non-decreasing.

### Example 3

```
Input:  nums = [-3,0,-3,2]
Output: [-3,-3,0,2]
```

**Explanation:** Negative numbers are ordered correctly relative to zero and the
positive value.

## Hint

Use **Heap Sort**. First rearrange `nums` into a max-heap in `O(n)` with
bottom-up heapify. Then repeatedly swap the max (index `0`) with the last
unsorted slot, reduce the heap size by one, and sift the new root down to
restore the max-heap property. Each swap locks one element into its final
position — no extra array required.
