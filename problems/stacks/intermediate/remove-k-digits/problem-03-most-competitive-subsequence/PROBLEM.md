# Most Competitive Subsequence

**Difficulty:** Medium

**Source:** LeetCode 1673 — Find the Most Competitive Subsequence

## Description

Given an integer array `nums` and a positive integer `k`, return the most competitive subsequence of `nums` of size `k`. A subsequence is obtained by deleting some (possibly zero) elements without changing the order of the rest. Subsequence `a` is more competitive than `b` (both size `k`) if at the first index where they differ, `a` has the smaller value. Return the result as a list.

## Examples

### Example 1

```
Input:  nums = [3, 5, 2, 6], k = 2
Output: [2, 6]
```

**Explanation:** Among the size-2 subsequences, `[2, 6]` is the most competitive.

### Example 2

```
Input:  nums = [2, 4, 3, 3, 5, 4, 9, 6], k = 4
Output: [2, 3, 3, 4]
```

**Explanation:** Greedily dropping larger earlier values (while enough remain to fill `k` slots) yields the smallest sequence.

## Hint

Monotonic increasing stack: pop a larger top when a smaller value arrives, but only while `len(stack) + remaining > k` so you can still keep exactly `k` elements.
