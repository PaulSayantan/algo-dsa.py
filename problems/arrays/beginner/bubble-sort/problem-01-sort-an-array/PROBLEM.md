# Sort an Array

**Difficulty:** Easy

*Source: LeetCode 912 (Sort an Array) — adapted here for Bubble Sort practice with small constraints.*

## Description

Given an array of integers `nums`, return the array sorted in **ascending order**.

For this exercise, implement the sort yourself using the classic adjacent-swap technique
rather than calling a built-in `sort()`. The array may contain duplicates and negative
numbers. You may sort the array in place and return it, or return a new sorted array.

## Constraints

- `1 <= nums.length <= 1000`
- `-10^5 <= nums[i] <= 10^5`

(The length is kept small on purpose so that an `O(n^2)` algorithm is acceptable.)

## Examples

**Example 1**

```
Input:  nums = [5, 2, 3, 1]
Output: [1, 2, 3, 5]
```
Explanation: The four values arranged from smallest to largest are 1, 2, 3, 5.

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

Use **Bubble Sort**: repeatedly sweep the array, comparing each element with its neighbor and
swapping the pair when they are out of order. After each sweep the largest unsorted value
settles at the end.
