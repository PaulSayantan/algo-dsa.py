# House Robber

**Difficulty:** Medium

**Source:** LeetCode 198 (House Robber)

## Description

You are a professional robber planning to rob houses along a street. Each house has a
certain amount of money stashed. The only constraint stopping you from robbing all of
them is that **adjacent houses have security systems connected**, and it will
automatically contact the police if two adjacent houses are broken into on the same
night.

Given an integer array `nums` representing the amount of money in each house, return the
**maximum amount of money you can rob tonight without alerting the police** (i.e.,
without robbing two adjacent houses).

## Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

## Examples

### Example 1

```
Input: nums = [1, 2, 3, 1]
Output: 4
Explanation: Rob house 0 (money = 1) and house 2 (money = 3); 1 + 3 = 4.
Robbing houses 0 and 2 avoids adjacency, and no other valid choice beats 4.
```

### Example 2

```
Input: nums = [2, 7, 9, 3, 1]
Output: 12
Explanation: Rob house 0 (2), house 2 (9), and house 4 (1); 2 + 9 + 1 = 12.
```

### Example 3

```
Input: nums = [5]
Output: 5
Explanation: A single house; rob it for 5.
```

## Hint

Use **Dynamic Programming (memoization / tabulation)**: at each house decide *rob* (add
its money to the best up to two houses back) or *skip* (carry the best up to the previous
house). Cache the best total achievable through each prefix.
