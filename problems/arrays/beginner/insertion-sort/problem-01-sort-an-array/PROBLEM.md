# Sort an Array

**Difficulty:** Easy

*Source: LeetCode 912 (Sort an Array) — adapted here for Insertion Sort practice with small constraints.*

## Description

Given an array of integers `nums`, return the array sorted in **ascending order**.

For this exercise, implement the sort yourself by growing a sorted prefix and inserting each
new element into place, rather than calling a built-in `sort()`. The array may contain
duplicates and negative numbers. You may sort the array in place and return it, or return a
new sorted array.

## Constraints

- `1 <= nums.length <= 1000`
- `-10^5 <= nums[i] <= 10^5`

(The length is kept small on purpose so that an `O(n^2)` algorithm is acceptable.)

## Examples

**Example 1**

```
Input:  nums = [5, 2, 4, 1, 3]
Output: [1, 2, 3, 4, 5]
```
Explanation: Starting from the left, each element is inserted into the growing sorted prefix:
`[5]` → `[2,5]` → `[2,4,5]` → `[1,2,4,5]` → `[1,2,3,4,5]`.

**Example 2**

```
Input:  nums = [5, 1, 1, 2, 0, 0]
Output: [0, 0, 1, 1, 2, 5]
```
Explanation: Duplicates are preserved; both `0`s and both `1`s appear, then `2`, then `5`.

**Example 3**

```
Input:  nums = [-3, 0, -1, 2, -3]
Output: [-3, -3, -1, 0, 2]
```
Explanation: Negative numbers sort before non-negative ones; the two `-3`s stay together.

## Hint

Use **Insertion Sort**: keep the left part of the array sorted, then take the next element as
a `key` and shift every larger element in the sorted prefix one position right until the
`key` lands in its correct slot.
