# Count Subsets With Given Sum

**Difficulty:** Medium

Source: Classic counting variant of subset-sum (SPOJ / competitive-programming staple).

## Description

You are given an array of integers `nums` and an integer `target`. Count **how many
distinct subsets** (chosen by index, so two subsets are different if their index sets
differ even when the value multisets match) sum to exactly `target`. The empty subset
sums to `0` and is counted when `target == 0`.

As in the decision version, `n` is small (up to 40) but values can be large, so a table
indexed by sum is not viable. Return the count as an integer.

## Constraints

- `1 <= len(nums) <= 40`
- `-10^9 <= nums[i] <= 10^9`
- `-10^14 <= target <= 10^14`
- The answer fits in a 64-bit signed integer.

## Examples

### Example 1
```
Input:  nums = [1, 2, 3], target = 3
Output: 2
Explanation: Two subsets sum to 3: {3} and {1, 2}.
```

### Example 2
```
Input:  nums = [2, 2, 2], target = 4
Output: 3
Explanation: Choosing any two of the three (index) positions gives sum 4:
{i0,i1}, {i0,i2}, {i1,i2}. Equal values still count as distinct subsets by index.
```

### Example 3
```
Input:  nums = [1, -1, 2], target = 0
Output: 2
Explanation: The empty subset {} sums to 0, and {1, -1} sums to 0. Total = 2.
```

## Hint

Enumerating all `2^40` subsets to count matches is too slow. Split into halves, tabulate
each half's subset sums with their multiplicities, and combine — **Meet in the Middle**.
