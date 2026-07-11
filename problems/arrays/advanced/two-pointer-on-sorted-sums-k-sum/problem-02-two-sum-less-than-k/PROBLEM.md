# Two Sum Less Than K

**Difficulty:** Easy

**Source:** LeetCode 1099 (Two Sum Less Than K)

## Description

Given an array `nums` of integers and an integer `k`, return the **maximum** sum
`nums[i] + nums[j]` such that `i < j` and `nums[i] + nums[j] < k`.

If no `i, j` exist satisfying this condition, return `-1`.

## Constraints

- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 1000`
- `1 <= k <= 2000`

## Examples

**Example 1**

```
Input:  nums = [34, 23, 1, 24, 75, 33, 54, 8], k = 60
Output: 58
Explanation: We can use 34 and 24 to sum 58 which is less than 60.
             No valid pair sums to a value in (58, 60), so 58 is the maximum.
```

**Example 2**

```
Input:  nums = [10, 20, 30], k = 15
Output: -1
Explanation: In this case it is not possible to get a pair sum less than 15.
             The smallest pair sum is 10 + 20 = 30, which is not below 15.
```

**Example 3**

```
Input:  nums = [1, 2, 3, 4], k = 5
Output: 4
Explanation: 1 + 3 = 4 < 5 and 1 + 2 = 3 < 5; the largest pair sum still below 5 is 4.
             (2 + 3 = 5 is not allowed because it is not strictly less than k.)
```

## Hint

Sort the array first, then apply **Two-Pointer on Sorted Sums (k-Sum)**: with a
pointer at each end, whenever the pair sum is below `k` you have found a valid
candidate — record it and try to grow it; otherwise shrink the sum.
