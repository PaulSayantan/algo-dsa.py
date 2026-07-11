# 3Sum

**Difficulty:** Medium

**Source:** LeetCode 15 (3Sum)

## Description

Given an integer array `nums`, return **all unique triplets** `[nums[i], nums[j],
nums[k]]` such that `i`, `j`, `k` are distinct indices and
`nums[i] + nums[j] + nums[k] == 0`.

The solution set must **not contain duplicate triplets**. Two triplets are considered the
same if they contain the same three values (order within the triplet does not matter).
You may return the triplets in any order.

## Constraints

- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

## Examples

**Example 1**

```
Input:  nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
Explanation: The distinct value-triplets summing to 0 are (-1)+(-1)+2 = 0 and
(-1)+0+1 = 0. Although -1 appears twice, the triplet [-1, 0, 1] is only reported once.
```

**Example 2**

```
Input:  nums = [0, 1, 1]
Output: []
Explanation: No three of these values add to 0 (0+1+1 = 2), so the answer is empty.
```

**Example 3**

```
Input:  nums = [0, 0, 0, 0]
Output: [[0, 0, 0]]
Explanation: 0+0+0 = 0. Even though there are four zeros, the value-triplet [0,0,0] is
reported exactly once.
```

## Hint

Use **Sorting as Preprocessing**: sort the array, then fix one element and run a
two-pointer scan over the remaining sorted suffix. Sorting also makes duplicate triplets
trivial to skip because equal values sit next to each other.
