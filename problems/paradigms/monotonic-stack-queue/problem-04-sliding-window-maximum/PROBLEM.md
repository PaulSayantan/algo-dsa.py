# Sliding Window Maximum

**Difficulty:** Hard

**Source:** LeetCode 239 — Sliding Window Maximum

## Description

You are given an array of integers `nums` and an integer `k`. There is a sliding window of
size `k` that moves from the very left of the array to the very right. You can only see the
`k` numbers in the window. Each time the window moves right by one position.

Return an array of the **maximum** value in each window as it slides across `nums`. The
output has length `len(nums) - k + 1`.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`

## Examples

### Example 1

```
Input:  nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [3, 3, 5, 5, 6, 7]
```

**Explanation:** The windows and their maxima:
```
[1  3  -1] -3  5  3  6  7   ->  3
 1 [3  -1  -3] 5  3  6  7   ->  3
 1  3 [-1  -3  5] 3  6  7   ->  5
 1  3  -1 [-3  5  3] 6  7   ->  5
 1  3  -1  -3 [5  3  6] 7   ->  6
 1  3  -1  -3  5 [3  6  7]  ->  7
```

### Example 2

```
Input:  nums = [1], k = 1
Output: [1]
```

**Explanation:** There is one window `[1]`, whose maximum is `1`.

## Hint

Use a **Monotonic Stack / Queue** — specifically a monotonic **deque** of indices in
decreasing value order. The front always holds the index of the current window's maximum;
pop from the back to maintain order and pop from the front when an index leaves the window.
