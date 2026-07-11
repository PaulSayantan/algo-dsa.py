# Two Sum

**Difficulty:** Easy

**Source:** LeetCode 1 (Two Sum)

## Description

Given an array of integers `nums` and an integer `target`, return the **indices
of the two numbers** such that they add up to `target`.

You may assume that each input has **exactly one solution**, and you may not use
the *same element* twice. You can return the answer in any order.

The most direct way to solve this is to consider every possible pair of
positions `(i, j)` with `i < j` and check whether `nums[i] + nums[j] == target`.
With `n` numbers there are only `n·(n-1)/2` such pairs, so simply examining all
of them is a perfectly valid strategy.

## Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Exactly one valid answer exists.

## Examples

### Example 1

```
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9, so we return the indices 0 and 1.
```

### Example 2

```
Input:  nums = [3, 2, 4], target = 6
Output: [1, 2]
Explanation: nums[1] + nums[2] = 2 + 4 = 6. Note that indices 0 and 0 cannot be
used because an element may not be reused, so [0] alone (3 + 3) is invalid here.
```

### Example 3

```
Input:  nums = [3, 3], target = 6
Output: [0, 1]
Explanation: The two 3's live at distinct indices 0 and 1, and 3 + 3 = 6.
```

## Hint

Use **Brute Force / Complete Search**: enumerate every unordered pair of indices
and test whether it sums to the target.
