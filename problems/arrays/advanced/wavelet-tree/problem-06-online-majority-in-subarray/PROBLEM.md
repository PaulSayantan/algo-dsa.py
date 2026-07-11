# Online Majority Element in Subarray

**Difficulty:** Hard

Source: **LeetCode 1157** — "Online Majority Element In Subarray".

## Description

Design a data structure that, given a fixed integer array `arr`, efficiently
answers many online queries. Implement the class:

- `MajorityChecker(arr: List[int])` — initializes the object with the array
  `arr`.
- `query(left, right, threshold) -> int` — returns the element that occurs
  **at least `threshold`** times in the subarray `arr[left..right]` (both bounds
  **inclusive**). If no such element exists, return `-1`. It is guaranteed that
  `2 * threshold > right - left + 1`, i.e. `threshold` is more than half the
  subarray length, so at most one element can qualify.

## Constraints

- `1 <= arr.length <= 2 * 10^4`
- `1 <= arr[i] <= 2 * 10^4`
- `0 <= left <= right < arr.length`
- `threshold <= right - left + 1`
- `2 * threshold > right - left + 1`
- At most `10^4` calls to `query`.

## Examples

Let `arr = [1, 1, 2, 2, 1, 1]` (indices `0..5`).

### Example 1
```
Input:  query(0, 5, 4)
Output: 1
Explanation: In arr[0..5] = [1, 1, 2, 2, 1, 1], the value 1 occurs 4 times,
             which is >= threshold 4 -> return 1.
```

### Example 2
```
Input:  query(0, 3, 3)
Output: -1
Explanation: In arr[0..3] = [1, 1, 2, 2], the most frequent value (1 or 2)
             occurs only 2 times, which is < threshold 3 -> return -1.
```

### Example 3
```
Input:  query(2, 3, 2)
Output: 2
Explanation: In arr[2..3] = [2, 2], the value 2 occurs 2 times,
             which is >= threshold 2 -> return 2.
```

## Hint

Build a **Wavelet Tree**. Because a qualifying element must appear in more than
half the range, it must be the **median** of `arr[left..right]` — find it with a
single k-th-smallest descent (`k = (len // 2) + 1`). Then verify its true
frequency in the range with a `rank`/range-count query and compare to
`threshold`.
