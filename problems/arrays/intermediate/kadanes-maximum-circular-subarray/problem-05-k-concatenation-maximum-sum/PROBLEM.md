# K-Concatenation Maximum Sum

**Difficulty:** Hard (Medium on LeetCode)

**Source:** LeetCode 1191 — K-Concatenation Maximum Sum

## Description

Given an integer array `arr` and an integer `k`, form a new array by
**concatenating `arr` with itself `k` times**. For example, if
`arr = [1, 2]` and `k = 3`, the new array is `[1, 2, 1, 2, 1, 2]`.

Return the **maximum sub-array sum** of this length-`n·k` array. The subarray
may be **empty**, in which case its sum is `0` (so the answer is never
negative).

Because the answer can be large, return it **modulo `10^9 + 7`**.

## Constraints

- `1 <= arr.length <= 10^5`
- `1 <= k <= 10^5`
- `-10^4 <= arr[i] <= 10^4`

## Examples

### Example 1

```
Input: arr = [1, 2], k = 3
Output: 9
Explanation: The concatenation is [1, 2, 1, 2, 1, 2], whose total (the best
subarray) is 9. Because the array's own sum (3) is positive, repeating it k
times keeps adding value.
```

### Example 2

```
Input: arr = [1, -2, 1], k = 5
Output: 2
Explanation: arr sums to 0, so extra copies add nothing. The best subarray sits
across at most two adjacent copies: [1, ... , 1] spanning a copy boundary gives
sum 2.
```

### Example 3

```
Input: arr = [-1, -2], k = 7
Output: 0
Explanation: Every element is negative, so the best choice is the empty
subarray, sum = 0.
```

## Hint

You never need to build all `k` copies. Whatever a subarray gains from the
"middle" copies is just `(k − 2) · sum(arr)` when that sum is positive; the
wrap across a copy boundary is captured by running Kadane over just **two**
concatenated copies. This is the repeated-array face of Kadane's — Maximum
Circular Subarray.
