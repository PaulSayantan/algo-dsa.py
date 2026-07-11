# Rotate Array

**Difficulty:** Medium

**Source:** LeetCode 189 — Rotate Array

## Description

Given an integer array `nums`, rotate the array to the **right** by `k` steps,
where `k` is non-negative. The rotation must be done **in place**.

Rotating right by one step moves the last element to the front. Rotating by `k`
steps repeats that `k` times (but you should not literally shift `k` times — aim
for an efficient method). Try to solve it with `O(1)` extra space.

## Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

## Examples

### Example 1

```
Input:  nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation: Rotating right by 3 moves the last three elements [5,6,7] to the
front and the first four [1,2,3,4] to the back.
```

### Example 2

```
Input:  nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: With k = 2, the last two elements [3,99] move to the front and the
first two [-1,-100] move to the back.
```

## Hint

Use the **Reverse Words / String** technique: this is the double/triple reversal
identity. Reduce `k` modulo the length, reverse the whole array, then reverse the
two pieces (the first `k` and the remaining `n - k`) individually.
