# 3Sum Closest

**Difficulty:** Medium

**Source:** LeetCode 16 (3Sum Closest)

## Description

Given an integer array `nums` of length `n` and an integer `target`, find three
integers in `nums` such that the sum is **closest** to `target`.

Return **the sum of the three integers**.

You may assume that each input has exactly one solution.

## Constraints

- `3 <= nums.length <= 500`
- `-1000 <= nums[i] <= 1000`
- `-10^4 <= target <= 10^4`

## Examples

**Example 1**

```
Input:  nums = [-1, 2, 1, -4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
             No triplet sum is closer to 1 than distance 1.
```

**Example 2**

```
Input:  nums = [0, 0, 0], target = 1
Output: 0
Explanation: The only triplet sums to 0, which is the closest (and only) sum to 1.
```

**Example 3**

```
Input:  nums = [1, 1, 1, 0], target = -100
Output: 2
Explanation: The smallest achievable triplet sum is 0 + 1 + 1 = 2, which is the
             closest we can get to -100. Its distance from the target is 102.
```

## Hint

Sort the array, fix the first element, and sweep the rest with **Two-Pointer on
Sorted Sums (k-Sum)**. Instead of matching a target exactly, track the triplet sum
whose distance to `target` is smallest, and move pointers toward the target.
