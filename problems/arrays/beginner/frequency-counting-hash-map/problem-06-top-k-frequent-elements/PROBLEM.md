# Top K Frequent Elements

**Difficulty:** Medium

**Source:** LeetCode 347 (https://leetcode.com/problems/top-k-frequent-elements/)

## Description

Given an integer array `nums` and an integer `k`, return the `k` **most
frequent** elements. You may return the answer in any order.

This problem builds directly on frequency counting: first tally how often each
value appears, then select the `k` values with the largest counts. The
counting step is the easy part; the interesting decision is how to extract the
top `k` efficiently — using a heap or bucket sort — rather than fully sorting.

The problem is a well-known follow-up target because a full sort by frequency is
`O(n log n)`, and you are challenged to do better.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`.
- The answer is guaranteed to be unique.

## Examples

### Example 1

```
Input:  nums = [1, 1, 1, 2, 2, 3], k = 2
Output: [1, 2]
Explanation: 1 appears 3 times and 2 appears 2 times, the two highest counts.
3 appears only once and is excluded.
```

### Example 2

```
Input:  nums = [1], k = 1
Output: [1]
Explanation: There is only one distinct value, and it is the single most
frequent element.
```

### Example 3

```
Input:  nums = [4, 4, 4, 6, 6, 2, 2, 2, 2], k = 1
Output: [2]
Explanation: 2 appears 4 times, more than 4 (3 times) and 6 (2 times), so the
single most frequent element is 2.
```

## Hint

Use **Frequency Counting with a Hash Map** to tally counts, then pick the top
`k` with a heap of size `k` or with bucket sort by frequency (avoiding a full
`O(n log n)` sort).
