# Maximum Average Subarray I

**Difficulty:** Easy

**Source:** LeetCode 643 — Maximum Average Subarray I

## Description

You are given an integer array `nums` consisting of `n` elements, and an integer `k`.

Find a **contiguous** subarray whose length is **exactly** `k` that has the maximum
average value, and return this maximum average value. Any answer within `10^-5` of
the true answer is accepted.

The average of a subarray is the sum of its elements divided by its length.

## Constraints

- `n == nums.length`
- `1 <= k <= n <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Examples

### Example 1

```
Input:  nums = [1, 12, -5, -6, 50, 3], k = 4
Output: 12.75
Explanation: The subarray [12, -5, -6, 50] has the largest sum, 51.
             Its average is 51 / 4 = 12.75. No other length-4 window beats it.
```

### Example 2

```
Input:  nums = [5], k = 1
Output: 5.0
Explanation: Only one window of length 1 exists: [5]. Its average is 5 / 1 = 5.0.
```

### Example 3

```
Input:  nums = [0, 4, 0, 3, 2], k = 1
Output: 4.0
Explanation: With k = 1 the best window is the single largest element, 4.
             Its average is 4 / 1 = 4.0.
```

## Hint

Use the **Sliding Window** technique: keep a running sum of exactly `k` consecutive
elements, and update it in O(1) as the window slides by one position.
