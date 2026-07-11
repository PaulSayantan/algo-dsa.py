# Subset Sum Exists

**Difficulty:** Medium

Source: Classic subset-sum decision problem (CLRS 34.5.5 / competitive-programming staple).

## Description

You are given an array of integers `nums` and an integer `target`. Determine whether
there exists **any subset** of `nums` (a subset chosen by index, possibly empty) whose
elements sum to exactly `target`.

Return `True` if such a subset exists and `False` otherwise. The empty subset sums to `0`.

The twist that rules out the textbook `O(n · target)` dynamic-programming solution:
`n` is small (up to 40) but the values — and therefore the target — can be enormous
(up to `10^14` in magnitude), so a table indexed by sum is impossible. The numbers may
be negative, zero, or positive.

## Constraints

- `1 <= len(nums) <= 40`
- `-10^9 <= nums[i] <= 10^9`
- `-10^14 <= target <= 10^14`

## Examples

### Example 1
```
Input:  nums = [3, 34, 4, 12, 5, 2], target = 9
Output: True
Explanation: The subset {4, 5} sums to 9 (so does {3, 4, 2}).
```

### Example 2
```
Input:  nums = [3, 34, 4, 12, 5, 2], target = 30
Output: False
Explanation: The largest reachable sum that avoids 34 is 3+4+12+5+2 = 26, and any
subset containing 34 is already at least 34. No subset totals exactly 30.
```

### Example 3
```
Input:  nums = [-7, 2, 5, 12], target = -5
Output: True
Explanation: The subset {-7, 2} sums to -5.
```

## Hint

`2^40` subsets is far too many to enumerate, but `2^20` is not. Split the array into two
halves and combine their partial sums — this is the **Meet in the Middle** technique.
