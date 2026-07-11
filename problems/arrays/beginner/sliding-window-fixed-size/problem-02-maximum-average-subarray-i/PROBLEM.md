# Maximum Average Subarray I

**Difficulty:** Easy

**Source:** LeetCode 643 — "Maximum Average Subarray I"

## Description

You are given an integer array `nums` consisting of `n` elements and an integer `k`.

Find a **contiguous** subarray whose length is exactly `k` that has the **maximum
average value**, and return that maximum average. Any answer within `10^-5` of the true
value is accepted.

## Constraints

- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Examples

### Example 1

```
Input:  nums = [1, 12, -5, -6, 50, 3], k = 4
Output: 12.75000
```

**Explanation:** The length-4 windows have sums `2, 51, 42`, giving averages
`0.5, 12.75, 10.5`. The maximum average is `12.75`, from the window `[12, -5, -6, 50]`
(sum `51`, `51 / 4 = 12.75`).

### Example 2

```
Input:  nums = [5], k = 1
Output: 5.00000
```

**Explanation:** There is only one window, the element `5` itself, so the maximum
average is `5.0`.

### Example 3

```
Input:  nums = [0, 4, 0, 3, 2], k = 1
Output: 4.00000
```

**Explanation:** With `k = 1` every element is its own window, so the maximum average
equals the maximum element, `4`.

## Hint

Use a **Sliding Window (fixed size)**. Because `k` is fixed, the average is just the
window **sum** divided by `k`, so maximizing the average is the same as maximizing the
sum. Maintain the window sum incrementally and divide by `k` only at the end.
