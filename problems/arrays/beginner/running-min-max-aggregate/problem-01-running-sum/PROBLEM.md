# Running Sum of 1d Array

**Difficulty:** Easy

**Source:** LeetCode 1480 — Running Sum of 1d Array

## Description

Given an array `nums`, you must compute the *running sum* of the array. The
running sum is defined as `runningSum[i] = nums[0] + nums[1] + ... + nums[i]`;
that is, each output position holds the sum of every element up to and
including that index.

Return the running-sum array.

## Constraints

- `1 <= nums.length <= 1000`
- `-10^6 <= nums[i] <= 10^6`
- You should aim to produce the result in a single left-to-right pass.

## Examples

### Example 1

```
Input:  nums = [1, 2, 3, 4]
Output: [1, 3, 6, 10]
Explanation: Running sum = [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].
```

### Example 2

```
Input:  nums = [1, 1, 1, 1, 1]
Output: [1, 2, 3, 4, 5]
Explanation: Each new element adds 1 to the previous running total,
so the totals climb 1, 2, 3, 4, 5.
```

### Example 3

```
Input:  nums = [3, 1, 2, 10, 1]
Output: [3, 4, 6, 16, 17]
Explanation: Running sum = [3, 3+1, 3+1+2, 3+1+2+10, 3+1+2+10+1]
           = [3, 4, 6, 16, 17].
```

## Hint

Keep a **Running Aggregate** (a cumulative sum) as you sweep once through the
array; each output element is the previous cumulative total plus the current
value.
