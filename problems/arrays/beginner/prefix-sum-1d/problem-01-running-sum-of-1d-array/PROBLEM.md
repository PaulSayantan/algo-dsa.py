# Running Sum of 1d Array

**Difficulty:** Easy

**Source:** LeetCode 1480 — Running Sum of 1d Array

## Description

Given an array `nums`, define a running sum of the array as
`runningSum[i] = sum(nums[0] ... nums[i])`.

Return the running sum of `nums`.

In other words, each output position holds the total of every element from the
start of the array up to and including the current position. This is precisely
the (inclusive) prefix-sum array, and building it correctly is the foundation
for every other problem in this folder.

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
Explanation: Each new element adds 1 to the previous running total.
```

### Example 3

```
Input:  nums = [3, 1, 2, 10, 1]
Output: [3, 4, 6, 16, 17]
Explanation: 3, then 3+1=4, then 4+2=6, then 6+10=16, then 16+1=17.
```

## Hint

Use the **Prefix Sum (1D)** idea: keep a running total and, at each index, add
the current element to the total from the previous index.
