# Longest Increasing Subsequence

**Difficulty:** Medium

**Source:** LeetCode 300 — Longest Increasing Subsequence

## Description

Given an integer array `nums`, return the length of the **longest strictly increasing
subsequence**.

A subsequence is a sequence derived from the array by deleting some or no elements without changing
the order of the remaining elements. For example, `[3, 6, 2, 7]` is a subsequence of
`[0, 3, 1, 6, 2, 2, 7]`.

The optimal solution runs in `O(n log n)` time.

## Constraints

- `1 <= nums.length <= 2500`
- `-10^4 <= nums[i] <= 10^4`

## Examples

### Example 1
```
Input:  nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Explanation: One longest strictly increasing subsequence is [2, 3, 7, 101],
             which has length 4. (Another is [2, 3, 7, 18].)
```

### Example 2
```
Input:  nums = [0, 1, 0, 3, 2, 3]
Output: 4
Explanation: The longest strictly increasing subsequence is [0, 1, 2, 3],
             which has length 4.
```

### Example 3
```
Input:  nums = [7, 7, 7, 7, 7, 7, 7]
Output: 1
Explanation: All elements are equal. A STRICTLY increasing subsequence can
             contain only one of them, so the answer is 1.
```

## Hint

Maintain a `tails` array where `tails[i]` is the smallest possible tail of any increasing
subsequence of length `i + 1`. For each number, replace the first tail that is `>= num` — that
position is the **lower bound** of `num`. Use a **Lower/Upper Bound (bisect)** search to find it in
`O(log n)`.
