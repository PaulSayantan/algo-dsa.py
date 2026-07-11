# Subarray Sum Equals K

**Difficulty:** Medium

**Source:** LeetCode 560 (Subarray Sum Equals K)

## Description

Given an integer array `nums` and an integer `k`, return the **total number of
contiguous subarrays** whose elements sum to exactly `k`.

A subarray is a contiguous, non-empty slice of the array. The array may contain
negative numbers and zeros, so a sliding window does **not** work directly.

## Constraints

- `1 <= nums.length <= 2 * 10^4`
- `-1000 <= nums[i] <= 1000`
- `-10^7 <= k <= 10^7`

## Examples

### Example 1

```
Input:  nums = [1, 1, 1], k = 2
Output: 2
Explanation: The subarrays nums[0..1] = [1, 1] and nums[1..2] = [1, 1] each sum
to 2. They overlap but are counted separately, giving 2.
```

### Example 2

```
Input:  nums = [1, 2, 3], k = 3
Output: 2
Explanation: [1, 2] (indices 0..1) sums to 3 and [3] (index 2) sums to 3, so the
count is 2.
```

### Example 3

```
Input:  nums = [1, -1, 0], k = 0
Output: 3
Explanation: [1, -1] (0..1), [1, -1, 0] (0..2), and [0] (index 2) each sum to 0.
Because negatives are present, a window-based method would miss some of these.
```

## Hint

Use **Hashing**: track the running prefix sum and keep a hash map from each prefix
sum to how many times it has occurred. A subarray ending at the current index sums
to `k` exactly when some earlier prefix sum equals `current_prefix - k`.
