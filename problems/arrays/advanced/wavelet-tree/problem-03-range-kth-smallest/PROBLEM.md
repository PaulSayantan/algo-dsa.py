# Range K-th Smallest (MKTHNUM)

**Difficulty:** Medium

Source: SPOJ **MKTHNUM** ("K-th Number"), also Codeforces/POJ 2104. The canonical
range order-statistic problem.

## Description

You are given a **static** integer array `arr` of length `n`. Answer `q` queries
of the form:

> `kthSmallest(l, r, k)` — consider the subarray `arr[l..r)` (0-based, right-
> **exclusive**). If its elements were sorted in non-decreasing order, return the
> `k`-th one (1-based `k`).

For example, if `arr[l..r) = [5, 2, 6, 3]`, its sorted form is `[2, 3, 5, 6]`, so
the 1st smallest is `2`, the 2nd is `3`, the 3rd is `5`, the 4th is `6`.

Preprocess `arr` once and answer each query in `O(log sigma)` time.

## Constraints

- `1 <= n <= 10^5`
- `-10^9 <= arr[i] <= 10^9`
- `1 <= q <= 5 * 10^4`
- `0 <= l < r <= n` and `1 <= k <= r - l` for every query.

## Examples

Let `arr = [1, 5, 2, 6, 3, 7, 4]` (indices `0..6`).

### Example 1
```
Input:  kthSmallest(1, 5, 3)
Output: 5
Explanation: arr[1..5) = [5, 2, 6, 3]. Sorted: [2, 3, 5, 6].
             The 3rd smallest is 5.
```

### Example 2
```
Input:  kthSmallest(0, 7, 2)
Output: 2
Explanation: The whole array sorted is [1, 2, 3, 4, 5, 6, 7].
             The 2nd smallest is 2.
```

### Example 3
```
Input:  kthSmallest(2, 3, 1)
Output: 2
Explanation: arr[2..3) = [2], a single element; its 1st smallest is 2.
```

## Hint

Build a **Wavelet Tree**. To find the `k`-th smallest in `arr[l..r)`, descend
from the root: at each node let `leftCount` be how many of the window's elements
went to the left (lower-value) child. If `k <= leftCount`, the answer is in the
left child; otherwise subtract `leftCount` from `k` and go right. The leaf you
land on is the answer value.
