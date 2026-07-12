# Next Smaller Element

**Difficulty:** Easy

**Source:** Classic — Next Smaller Element (to the right)

## Description

Given an integer array `nums`, return an array `answer` of the same length where `answer[i]` is the first element to the right of `nums[i]` that is strictly smaller than `nums[i]`. If no smaller element exists to its right, use `-1`.

Constraints: `1 <= len(nums) <= 10^5`, `-10^9 <= nums[i] <= 10^9`.

## Examples

### Example 1

```
Input:  nums = [4,8,5,2,25]
Output: [2,5,2,-1,-1]
```

**Explanation:** To the right of `4` the first strictly smaller value is `2`; to the right of `8` it is `5`; `2` and `25` have no smaller value to their right, so they map to `-1`.

## Hint

Mirror the next-greater scan: keep an increasing stack of pending values and, when a strictly smaller value arrives, it resolves every larger value waiting on top.
