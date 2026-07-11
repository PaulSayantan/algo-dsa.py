# 3Sum

**Difficulty:** Medium

**Source:** LeetCode 15 (3Sum)

## Description

Given an integer array `nums`, return **all the triplets** `[nums[i], nums[j], nums[k]]`
such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must **not contain duplicate triplets**. Two triplets
are considered duplicates if they contain the same multiset of values, regardless of
order. The order of the triplets in the output and the order of numbers within each
triplet do not matter.

## Constraints

- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

## Examples

**Example 1**

```
Input:  nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
Explanation: -1 + -1 + 2 = 0 and -1 + 0 + 1 = 0.
             Although -1 appears twice, the triplet [-1, 0, 1] is listed only once.
             The distinct triplets summing to zero are [-1, -1, 2] and [-1, 0, 1].
```

**Example 2**

```
Input:  nums = [0, 1, 1]
Output: []
Explanation: The only possible triplet [0, 1, 1] sums to 2, not 0, so there is no answer.
```

**Example 3**

```
Input:  nums = [0, 0, 0]
Output: [[0, 0, 0]]
Explanation: The only triplet sums to 0; it is reported exactly once.
```

## Hint

Sort the array, fix the first element, and reduce the rest to a 2-Sum-to-target
problem solved with **Two-Pointer on Sorted Sums (k-Sum)**. Sorting also lets you
skip equal neighbors to avoid duplicate triplets.
