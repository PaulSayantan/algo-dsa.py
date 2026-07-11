# Contains Duplicate III

**Difficulty:** Hard

**Source:** LeetCode 220 — Contains Duplicate III

## Description

You are given an integer array `nums` and two integers `indexDiff` and
`valueDiff`.

Find whether there exists a pair of indices `(i, j)` such that:

- `i != j`,
- `abs(i - j) <= indexDiff`, and
- `abs(nums[i] - nums[j]) <= valueDiff`.

Return `true` if such a pair exists and `false` otherwise.

## Constraints

- `2 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `1 <= indexDiff <= nums.length`
- `0 <= valueDiff <= 10^9`

## Examples

### Example 1

```
Input:  nums = [1, 2, 3, 1], indexDiff = 3, valueDiff = 0
Output: true
Explanation: Pick i = 0 and j = 3. abs(0 - 3) = 3 <= 3 and
abs(nums[0] - nums[3]) = abs(1 - 1) = 0 <= 0. Both conditions hold.
```

### Example 2

```
Input:  nums = [1, 5, 9, 1, 5, 9], indexDiff = 2, valueDiff = 3
Output: false
Explanation: Every pair of indices within distance 2 differs in value by at
least 4 (e.g. |1 - 5| = 4, |5 - 9| = 4), which exceeds valueDiff = 3. The equal
values (the two 1s, the two 5s, the two 9s) are always 3 indices apart, which
exceeds indexDiff = 2. No pair satisfies both constraints.
```

### Example 3

```
Input:  nums = [7, 2, 8], indexDiff = 2, valueDiff = 1
Output: true
Explanation: Pick i = 0 and j = 2. abs(0 - 2) = 2 <= 2 and
abs(nums[0] - nums[2]) = abs(7 - 8) = 1 <= 1. Both conditions hold.
```

## Hint

Map each value into a **bucket** of width `valueDiff + 1` (bucket id =
`num // (valueDiff + 1)`). Any two numbers within `valueDiff` of each other must
land in the same bucket or in adjacent buckets. Maintain a sliding window of
buckets over the last `indexDiff` indices — this **Bucket Sort** style
partitioning turns the check into `O(1)` per element and `O(n)` overall.
