# Top K Frequent Elements

**Difficulty:** Medium

**Source:** LeetCode 347 — Top K Frequent Elements

## Description

Given an integer array `nums` and an integer `k`, return the `k` **most
frequent** elements. You may return the answer in **any order**.

It is guaranteed that the answer is unique — the set of the `k` most frequent
elements is well defined for the given inputs.

The interesting challenge is to design an algorithm that runs in better than
`O(n log n)` time.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, number of distinct elements in nums]`.
- The answer is guaranteed to be unique.

## Examples

### Example 1

```
Input:  nums = [1, 1, 1, 2, 2, 3], k = 2
Output: [1, 2]
Explanation: 1 appears three times, 2 appears twice, 3 appears once. The two
most frequent elements are 1 and 2. [2, 1] is also accepted.
```

### Example 2

```
Input:  nums = [1], k = 1
Output: [1]
Explanation: There is only one element, and it is trivially the most frequent.
```

### Example 3

```
Input:  nums = [4, 4, 4, 5, 5, 6, 7], k = 3
Output: [4, 5, 6]
Explanation: Frequencies are 4 -> 3, 5 -> 2, 6 -> 1, 7 -> 1. The top two (4 and
5) are unambiguous. For the third slot 6 and 7 tie at frequency 1; the problem
guarantees a unique answer for its test data, and any valid top-k set is
accepted, e.g. [4, 5, 7].
```

## Hint

An element's frequency is an integer between `1` and `n`. Build an array of
`n + 1` buckets indexed by frequency, place each distinct value into the bucket
matching its count, then read buckets from highest frequency downward until you
have collected `k` elements. This **Bucket Sort** by frequency achieves `O(n)`.
