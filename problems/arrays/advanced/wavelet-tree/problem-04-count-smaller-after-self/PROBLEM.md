# Count of Smaller Numbers After Self

**Difficulty:** Hard

Source: **LeetCode 315** — "Count of Smaller Numbers After Self".

## Description

You are given an integer array `nums`. Return an integer array `counts` where
`counts[i]` is the number of elements to the **right** of `nums[i]` that are
strictly smaller than `nums[i]`. Formally:

```
counts[i] = |{ j : i < j < n  and  nums[j] < nums[i] }|
```

## Constraints

- `1 <= n == nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Examples

### Example 1
```
Input:  nums = [5, 2, 6, 1]
Output: [2, 1, 1, 0]
Explanation:
  - For 5, the elements to its right are [2, 6, 1]; smaller than 5 -> {2, 1} = 2.
  - For 2, the elements to its right are [6, 1]; smaller than 2 -> {1}      = 1.
  - For 6, the elements to its right are [1];    smaller than 6 -> {1}      = 1.
  - For 1, there is nothing to its right                                    = 0.
```

### Example 2
```
Input:  nums = [-1, -1]
Output: [0, 0]
Explanation:
  - For the first -1, the element to its right is [-1]; strictly smaller? no -> 0.
  - For the second -1, nothing to its right                                 -> 0.
```

### Example 3
```
Input:  nums = [3]
Output: [0]
Explanation: A single element has nothing to its right -> 0.
```

## Hint

Build a **Wavelet Tree** over the whole array once. For each index `i`, the
answer is the count of values `< nums[i]` inside the suffix `nums[i+1 .. n)` —
exactly a "range count of values `<= nums[i] - 1`" query, answerable in
`O(log sigma)` per index.
