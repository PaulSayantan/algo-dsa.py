# Longest Continuous Subarray With Absolute Diff ≤ Limit

**Difficulty:** Medium

**Source:** LeetCode 1438

## Description

Given an array of integers `nums` and an integer `limit`, return the size of the
**longest non-empty contiguous subarray** such that the absolute difference between the
**maximum** and **minimum** element of that subarray is less than or equal to `limit`.

Formally, find the maximum `r - l + 1` over all `0 <= l <= r < n` such that

```
max(nums[l..r]) - min(nums[l..r]) <= limit
```

While this problem has a classic monotonic-deque / sliding-window solution, it can also
be solved cleanly by making the range max and range min queryable in O(1) with two
Sparse Tables and then binary-searching the answer length.

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `0 <= limit <= 10^9`

## Examples

### Example 1

```
Input:  nums = [8, 2, 4, 7], limit = 4
Output: 2
```

Explanation: All subarrays and their `max - min`:
- `[8]`, `[2]`, `[4]`, `[7]` → diff 0 (length 1)
- `[8,2]` → 6, `[2,4]` → 2 (ok), `[4,7]` → 3 (ok)
- `[8,2,4]` → 6, `[2,4,7]` → 5
- `[8,2,4,7]` → 6

The longest with diff `<= 4` is `[2,4]` or `[4,7]`, length **2**.

### Example 2

```
Input:  nums = [10, 1, 2, 4, 7, 2], limit = 5
Output: 4
```

Explanation: `[2, 4, 7, 2]` has `max - min = 7 - 2 = 5 <= 5`, length 4. No length-5
window satisfies the limit.

### Example 3

```
Input:  nums = [4, 2, 2, 2, 4, 4, 2, 2], limit = 0
Output: 3
```

Explanation: With `limit = 0` every element in the window must be equal. The run
`[2, 2, 2]` (indices 1..3) has length 3, the longest such block.

## Hint

Build **two Sparse Tables** — one for range max and one for range min — so any window's
`max - min` is O(1). The property "there exists a valid window of length L" is monotone
in L (if a length-L window is valid, some length-(L-1) window is too), so **binary
search** the longest feasible length and validate each candidate length by scanning all
windows in O(n).
