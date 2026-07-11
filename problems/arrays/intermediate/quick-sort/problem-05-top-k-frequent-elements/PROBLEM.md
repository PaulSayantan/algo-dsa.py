# Top K Frequent Elements

**Difficulty:** Medium

**Source:** LeetCode 347 — Top K Frequent Elements

## Description

Given an integer array `nums` and an integer `k`, return the `k` most frequent
elements. You may return the answer in **any order**.

First tally how many times each distinct value appears. You now have a list of
`(value, frequency)` pairs, and you need the `k` pairs with the highest frequency.
Sorting all `m` distinct values by frequency is O(m log m), but — as with the k-th
largest element — you only need the top `k`, not a total order. **Quickselect** on the
frequency key finds the `k` most frequent values in average O(m) time.

The problem's follow-up explicitly asks for an algorithm better than O(n log n), which
this achieves.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is guaranteed that the answer is unique.

## Examples

### Example 1

```
Input:  nums = [1, 1, 1, 2, 2, 3], k = 2
Output: [1, 2]
Explanation: Frequencies are {1: 3, 2: 2, 3: 1}. The two most frequent values are 1
(appears 3 times) and 2 (appears 2 times).
```

### Example 2

```
Input:  nums = [1], k = 1
Output: [1]
Explanation: Only one distinct value exists, and it is the most frequent.
```

### Example 3

```
Input:  nums = [4, 4, 4, 6, 6, 2, 2, 2, 2], k = 1
Output: [2]
Explanation: Frequencies are {4: 3, 6: 2, 2: 4}. The single most frequent value is 2
(appears 4 times).
```

## Hint

Build a frequency map, then run **Quickselect** over the distinct values using their
frequency as the partition key. Place the `k` highest-frequency values at one end of
the array and return them — no need to sort the rest.
