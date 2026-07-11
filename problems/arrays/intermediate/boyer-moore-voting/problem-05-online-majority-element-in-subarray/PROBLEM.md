# Online Majority Element in Subarray

**Difficulty:** Hard

**Source:** LeetCode 1157 — Online Majority Element in Subarray

## Description

Design a data structure that efficiently answers **subarray majority** queries.

Implement the `MajorityChecker` class:

- `MajorityChecker(int[] arr)` — initializes the structure with the array `arr`.
- `int query(int left, int right, int threshold)` — returns the element in the subarray
  `arr[left..right]` (inclusive) that occurs **at least `threshold` times**, or `-1` if no
  such element exists.

You are guaranteed that for every query `threshold` is strictly greater than half the length
of the queried subarray, i.e. `2 * threshold > right - left + 1`. This means the answer, if it
exists, is the **strict majority** of the subarray — and is therefore unique.

## Constraints

- `1 <= arr.length <= 2 * 10^4`
- `1 <= arr[i] <= 2 * 10^4`
- `0 <= left <= right < arr.length`
- `2 * threshold > right - left + 1`
- Up to `10^4` calls to `query`.

## Examples

### Example 1

```
Input:  arr = [1, 1, 2, 2, 1, 1]
        query(0, 5, 4)
Output: 1
```

Explanation: In `arr[0..5] = [1,1,2,2,1,1]`, the value `1` occurs 4 times which is
`>= threshold = 4`, so the answer is `1`.

### Example 2

```
Input:  arr = [1, 1, 2, 2, 1, 1]
        query(0, 3, 3)
Output: -1
```

Explanation: In `arr[0..3] = [1,1,2,2]`, both `1` and `2` occur only 2 times, which is below
`threshold = 3`. No element qualifies, so the answer is `-1`.

### Example 3

```
Input:  arr = [1, 1, 2, 2, 1, 1]
        query(2, 3, 2)
Output: 2
```

Explanation: In `arr[2..3] = [2,2]`, the value `2` occurs 2 times which is `>= threshold = 2`,
so the answer is `2`.

## Hint

The Boyer–Moore vote is **associative** — the (candidate, count) result of two adjacent
segments can be merged in O(1). Build a **segment tree** where each node stores the
Boyer–Moore majority of its range; a range query merges nodes to get the only possible
majority candidate, then verify its true frequency in the subarray (e.g. via per-value sorted
index lists and binary search).
