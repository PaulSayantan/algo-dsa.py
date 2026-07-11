# 3Sum Smaller

**Difficulty:** Medium

**Source:** LeetCode 259 (3Sum Smaller)

## Description

Given an array of `n` integers `nums` and a target integer `target`, find the
**number of index triplets** `(i, j, k)` with `0 <= i < j < k < n` that satisfy the
condition:

```
nums[i] + nums[j] + nums[k] < target
```

Return that count.

## Constraints

- `n == nums.length`
- `0 <= n <= 3500`
- `-100 <= nums[i] <= 100`
- `-100 <= target <= 100`

## Examples

**Example 1**

```
Input:  nums = [-2, 0, 1, 3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
             [-2, 0, 1]  (sum -1) and [-2, 0, 3] (sum 1).
             The other triplets ([-2, 1, 3] = 2 and [0, 1, 3] = 4) are not below 2.
```

**Example 2**

```
Input:  nums = [], target = 0
Output: 0
Explanation: There are no elements, hence no triplets.
```

**Example 3**

```
Input:  nums = [0, 0, 0], target = 1
Output: 1
Explanation: The only triplet [0, 0, 0] sums to 0, which is less than 1.
```

## Hint

Sort the array, fix the smallest index `i`, then run **Two-Pointer on Sorted Sums
(k-Sum)** on the suffix. When a pair sum is small enough, every element between the
two pointers also works — so you can count a whole batch of triplets at once.
