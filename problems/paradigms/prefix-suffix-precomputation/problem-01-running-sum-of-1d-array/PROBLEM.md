# Running Sum of 1d Array

**Difficulty:** Easy

**Source:** LeetCode 1480 — Running Sum of 1d Array

## Description

Given an array `nums`, define a *running sum* of the array as
`runningSum[i] = sum(nums[0] ... nums[i])`.

Return the running sum of `nums`.

In other words, each output position holds the total of every element up to and
including that position. This is exactly the **prefix-sum** array (kept inclusive
of the current element), the foundational building block of the prefix
precomputation paradigm.

## Constraints

- `1 <= nums.length <= 1000`
- `-10^6 <= nums[i] <= 10^6`

## Examples

### Example 1

```
Input:  nums = [1, 2, 3, 4]
Output: [1, 3, 6, 10]
Explanation: Running sum is obtained as follows:
             [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].
```

### Example 2

```
Input:  nums = [1, 1, 1, 1, 1]
Output: [1, 2, 3, 4, 5]
Explanation: Each new element adds 1 to the previous running total:
             [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1] = [1, 2, 3, 4, 5].
```

### Example 3

```
Input:  nums = [3, 1, 2, 10, 1]
Output: [3, 4, 6, 16, 17]
Explanation: [3, 3+1, 3+1+2, 3+1+2+10, 3+1+2+10+1] = [3, 4, 6, 16, 17].
```

## Hint

Use **Prefix / Suffix Precomputation**: sweep left to right maintaining a running
total, writing each cumulative value as you go. Each position depends only on the
previous cumulative result.
